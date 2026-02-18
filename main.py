from data_loaders import load_profiles
from matchers import match_profiles

def run_matching():
    profiles = load_profiles()

    results = []

    for i in range(len(profiles)):
        for j in range(i + 1, len(profiles)):
            match = match_profiles(profiles[i], profiles[j])
            results.append(match)

    return results

if __name__ == "__main__":
    matches = run_matching()

    for m in matches:
        print("\n==============================")
        for k, v in m.items():
            print(f"{k}: {v}")
