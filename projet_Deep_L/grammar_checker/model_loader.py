import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "prithivida/grammar_error_correcter_v1"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("🔄 Chargement du modèle T5...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)

print("✅ Modèle chargé avec succès !")
