from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("1. Téléchargement du modèle en cours... (Cela peut prendre quelques minutes)")
MODEL_NAME = "gotutiyan/gec-t5-large-clang8"

# Cela va télécharger les fichiers dans le cache de ton PC
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("2. Modèle chargé ! Test d'une phrase...")

input_text = "I has a car and I likes it."
input_ids = tokenizer.encode(input_text, return_tensors="pt")

outputs = model.generate(
    input_ids, 
    max_length=128, 
    num_beams=5, 
    early_stopping=True
)

corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Original : {input_text}")
print(f"Corrigé  : {corrected}")