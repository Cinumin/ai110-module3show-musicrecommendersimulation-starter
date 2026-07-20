"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    
    # Starter example profile
    user_prefs =  {"genre": "pop", "mood": "happy", "energy": 1.6}
    """
    [{"genre": "Pop", "mood": "Happy", "energy": 0.8},
    {"genre": "jazz", "mood": "sad", "energy": 0.95},
    {"genre": "pop", "mood": "happy", "energy": 1.6}]
    """
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 40)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']}  (Score: {score:.2f})")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print()


if __name__ == "__main__":
    main()
