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
        # Sort matches by meeting_value descending and take top 2
        matches_sorted = sorted(matches, key=lambda x: x["meeting_value"], reverse=True)[:2]
        results[profile.name] = matches_sorted
    return results

if __name__ == "__main__":
    top_matches = run_matching()
    for profile_name, matches in top_matches.items():
        print(f"\nTop 2 matches for {profile_name}:")
        for idx, m in enumerate(matches, 1):
            print(f"\nRank {idx} match:")
            print("------------------------------")
            for k, v in m.items():
                print(f"{k}: {v}")
