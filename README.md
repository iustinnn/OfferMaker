# OfferMaker

## Descriere

Modelul finetuned: [Hugging Face - Test Model](https://huggingface.co/iustinnn/test-model)

Adaptoarele: [Hugging Face - Lora Model](https://huggingface.co/iustinnn/lora_model)

Dataset: [Hugging Face - Antrenare](https://huggingface.co/datasets/iustinnn/antrenare)

În Google Colab se află modelul antrenat încărcat, pentru care putem oferi cerințe și vom primi răspunsul într-un fișier docx. Acesta va fi parsat și vom fi notificați dacă respectă structura necesară (toate detaliile și explicațiile sunt în link-ul de mai jos).

Totodată, acolo avem întregul proces prin care am antrenat modelul Meta-Llama-3-8B, cu toate detaliile necesare.

[Google Colab - Finetuning process](https://colab.research.google.com/drive/174tEYjyFTCIzXRf64ugZcbXMdNaLHrVl#scrollTo=QmUBVEnvCDJv)


Pentru a rula modelul local (nerecomandat având în vedere că dureaza foarte mult):

## Rulare
    python test.py


## Dependențe

Pentru a rula programul, instalați următoarele pachete:

1. **Transformers**
   ```bash
   pip install transformers


1. **Torch (PyTorch)**
   ```bash
   pip install torch

1. **python-docx**
   ```bash
   pip install python-docx

1. **PEFT (Parameter Efficient Fine-Tuning)**
   ```bash
   pip install peft

