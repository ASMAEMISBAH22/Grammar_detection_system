from .model_loader import tokenizer, model, device
import torch

def correct_text(text):
    inputs = tokenizer(text, return_tensors="pt").to(device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_length=128,
            num_beams=5,
            early_stopping=True
        )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
