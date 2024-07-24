from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from docx import Document
from peft import PeftModel

def check_structure_and_provide_feedback(output_text):
    required_sections = [
        "Scopul documentului",
        "Dezvoltare de bază",
        "Sugestii suplimentare",
        "Pret și timp de implementare"
    ]

    section_presence = {section: False for section in required_sections}

    # Split the output into lines
    lines = output_text.split('\n')

    # Check each line to see if it matches a required section
    for line in lines:
        line = line.strip()
        if not line:
            continue
        for section in required_sections:
            if section.lower() in line.lower():
                section_presence[section] = True
                break

    missing_sections = [section for section, present in section_presence.items() if not present]

    if missing_sections:
        feedback = f"Lipsesc: {', '.join(missing_sections)}. Include-l în răspuns."
    else:
        feedback = "Toate secțiunile necesare sunt prezente."

    return feedback, missing_sections

def save_to_docx(text, filename):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)

# Load the fine-tuned model and tokenizer
model_name = "iustinnn/test-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")


# Define instruction
instruction = "Analizează cerințele clientului pentru aplicația dorită si crează o oferta pentru aplicație ce conține toate detaliile. Respectă structura pentru oferte. Descrie scopul documentului, propunere structură, sugestii suplimentare, preț si timp de implementare."

# Input text from console
input_text = input("Please enter the input text: ")
combined_input = f"Instruction: {instruction} Input: {input_text}"
max_length = 2048

inputs = tokenizer(combined_input, return_tensors="pt", padding='max_length', truncation=True, max_length=max_length)

if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

initial_outputs = model.generate(
    inputs['input_ids'],
    attention_mask=inputs['attention_mask'],
    max_length=4096,
    do_sample=True,
    top_p=0.4,  #  adjust
    temperature=1.2  # adjust
)

initial_output_text = tokenizer.decode(initial_outputs[0], skip_special_tokens=True)
print(initial_output_text)

save_to_docx(initial_output_text, "initial_output.docx")

# Verifica structure
feedback, missing_sections = check_structure_and_provide_feedback(initial_output_text)
print(feedback)
