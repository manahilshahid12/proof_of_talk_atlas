from embeddings import generate_embedding
from scoring import strategic_alignment_score, complementary_score, estimated_meeting_value
from summary import generate_summary

def match_profiles(profile1, profile2):

    embed1 = generate_embedding(profile1)
    embed2 = generate_embedding(profile2)

    strategic = strategic_alignment_score(embed1, embed2)
    complementary = complementary_score(profile1, profile2)
    meeting_value = estimated_meeting_value(strategic, complementary)

    summary = generate_summary(profile1, profile2, meeting_value)

    recommendation = (
        "Strong Match – Schedule 1:1"
        if meeting_value > 0.5
        else "Moderate Match – Consider Meeting"
    )

    return {
        "profile_1": profile1.name,
        "profile_2": profile2.name,
        "strategic_alignment": round(strategic, 3),
        "complementary_score": round(complementary, 3),
        "meeting_value": round(meeting_value, 3),
        "summary": summary,
        "recommendation": recommendation,
        "actions": ["Send Invite", "Quick Call"]
    }
