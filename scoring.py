from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def strategic_alignment_score(embed1, embed2):
    score = cosine_similarity([embed1], [embed2])[0][0]
    return float(score)

def complementary_score(profile1, profile2):
    score = 0.0

    # Example: allocator ↔ builder complementarity
    if profile1.capital_role == "allocator" and profile2.capital_role == "builder":
        score += 0.6
    if profile2.capital_role == "allocator" and profile1.capital_role == "builder":
        score += 0.6

    # Industry overlap
    shared_industry = len(set(profile1.industry_focus).intersection(profile2.industry_focus))
    score += 0.2 * shared_industry

    # Regulatory exposure overlap (as a proxy for skill/experience)
    shared_regulatory = len(set(profile1.regulatory_exposure).intersection(profile2.regulatory_exposure))
    score += 0.1 * (1 - min(shared_regulatory, 1))

    return min(score, 1.0)

def estimated_meeting_value(strategic, complementary):
    # Boost weights for prototype
    return (0.4 * strategic) + (0.5 * complementary) + (0.3 * (strategic * complementary))
