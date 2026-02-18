from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embedding(profile):
    text = f"""
    Name: {profile.name}
    Capital Role: {profile.capital_role}
    Capital Direction: {profile.capital_direction}
    Industry Focus: {', '.join(profile.industry_focus)}
    Regulatory Exposure: {', '.join(profile.regulatory_exposure)}
    Primary Constraint: {profile.primary_constraint}
    Strategic Goal: {profile.strategic_goal}
    Urgency Level: {profile.urgency_level}
    Geography Focus: {', '.join(profile.geography_focus)}
    """
    return model.encode(text)
