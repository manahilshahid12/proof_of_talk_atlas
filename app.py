import streamlit as st
from data_loaders import load_profiles
from matchers import match_profiles

def run_matching():
    profiles = load_profiles()
    results = {}
    for i, profile in enumerate(profiles):
        matches = []
        for j, other_profile in enumerate(profiles):
            if i == j:
                continue
            match = match_profiles(profile, other_profile)
            matches.append(match)
        matches_sorted = sorted(matches, key=lambda x: x["meeting_value"], reverse=True)[:2]
        results[profile.name] = matches_sorted
    return results

st.title("Proof of Talk Atlas - Top Matches Viewer")

if st.button("Run Matching"):
    top_matches = run_matching()
    for profile_name, matches in top_matches.items():
        st.header(f"Top 2 matches for {profile_name}")
        for idx, m in enumerate(matches, 1):
            st.subheader(f"Rank {idx} match:")
            st.write("---")
            for k, v in m.items():
                st.write(f"**{k}**: {v}")
