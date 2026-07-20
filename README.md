# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

The system will use content-based filtering instead of collaborative-filtering, since this system does not have the data of other users. This simple music recommender will use the features of the data, such as genre, mood, acousticness, and energy to score individual songs. There will be weights tailored to each feature, with more important features having heavier weights, such as genre. Since the user already has its own data of preferences, exact matching with preferred types of genre and mood are strong positive indicators. The Song object and UserProfile object will both use genre, mood, and energy since both objects carries these four attributes. 

flowchart TD
    Start(("●")) --> A(["Load user_prefs<br/>(genre, mood, target_energy)"])
    A --> B(["load_songs(csv_path)<br/>→ list of songs"])
    B --> C(["Get next song from list"])
    C --> D(["score_song(user_prefs, song)<br/>→ (score, reasons)"])
    D --> E(["Add (song, score, reasons)<br/>to results list"])
    E --> F{"More songs<br/>left?"}
    F -->|yes| C
    F -->|no| G(["Sort results by score,<br/>descending"])
    G --> H(["Take top K results"])
    H --> End(("◎"))

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

The recommender may over favor one genre due to its weight, thus likely not recommending a diverse set of songs that are different compared to the user's usual go-to playlist and preferred genres.
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



