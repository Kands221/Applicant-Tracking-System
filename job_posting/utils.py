import spacy
from django.conf import settings
import os

# Load the spaCy model
model_path = os.path.join(settings.BASE_DIR, 'ML_models', 'model-best')
print(model_path)
nlp = spacy.load(model_path)

def parse_cv(cv_text):
    doc = nlp(cv_text)
    # Your parsing logic here
    # Example: Extract entities or other information from CV
    formatted_entities = '\n'.join([f'{ent.text} -> {ent.label_}' for ent in doc.ents])
    return formatted_entities
