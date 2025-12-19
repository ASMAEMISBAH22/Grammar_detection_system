import os
from django.conf import settings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Chemin vers le dossier où tu as téléchargé les fichiers

MODEL_PATH = os.path.join(settings.BASE_DIR, 'grammar_checker/model_local')

class GECModel:
    _tokenizer = None
    _model = None

    @classmethod
    def load(cls):
        """ Charge le modèle en RAM une seule fois """
        if cls._model is None:
            print("💾 Chargement du modèle depuis le disque... (Cela peut prendre 30s)")
            try:
                # On charge depuis le dossier local
                cls._tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
                cls._model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
                print("✅ Modèle chargé en mémoire RAM !")
            except Exception as e:
                print(f"❌ Erreur de chargement : {e}")
                print(f"Vérifie que le dossier existe bien ici : {MODEL_PATH}")
        
        return cls._tokenizer, cls._model

    @staticmethod
    def correct(text):
        tokenizer, model = GECModel.load()
        
        if model is None:
            return "Erreur technique : Le modèle n'a pas pu être chargé."

        # Préparation du texte
        # On ajoute "grammar: " car c'est souvent utile pour T5
        inputs = tokenizer("grammar: " + text, return_tensors="pt", padding=True, truncation=True, max_length=128)
        
        # Génération de la correction
        outputs = model.generate(
            **inputs, 
            max_length=128, 
            num_beams=2, # On met 2 pour que ce soit plus rapide (5 est trop lent sur CPU)
            early_stopping=True
        )

        # Décodage
        corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_text