# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**MusicViber**
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

Intended for classroom exploration, this recommender generates songs based on the user's preferences, including genre, energy, and mood. The model also considers whether or not the user likes acousticness. The songs are hypothetical and are not representative of real songs.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model uses features of each song, including genre, energy, mood, and acousticness and considers any of these user preferences. The model ranks these songs by calculating their scores based on weights given to each feature. Higher scored songs rank higher on the list. The recommender outputs the top five scored songs.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The model has 18 songs in its catalog, representing 15 genres and 14 moods. The dataset is missing genres such as blues, K-pop, afrobeat, gospel, music theater/soundtrack, world/traditional music, funk, Latin, etc. The test profile uses mood as sad, which isn't actually one of the 14 moods in the catalog. The closest label is "melancholic."

15 genres: ambient, classical, country, edm, folk, hip hop, indie pop, jazz, lofi, metal, pop, r&b, reggae, rock, synthwave

14 moods: angry, chill, confident, euphoric, focused, happy, hopeful, intense, melancholic, moody, nostalgic, playful, relaxed, romantic
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system seems to work well when the users' preferences string match to those found in the dataset. For instance, top recommended song satisfied all three preferences of the pop/happy/1.6 user profile.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The energy gap calculation (`energy_closeness = 1 - abs(song["energy"] - user_prefs["energy"])`) assumes the user's target energy is already on the same 0-1 scale as the catalog. Every song in songs.csv has an energy value between 0.22 and 0.97, but nothing stops a user from entering something outside that range, like 1.6. When that happens, the absolute difference goes above 1 and energy_closeness turns negative, so the user gets silently penalized on every single song instead of getting an error or having their input clamped. In effect, anyone whose mental model of "energy" doesn't match the catalog's exact scale is punished rather than helped.

Genre and mood matching is also exact-string and case-sensitive, with no normalization. When I tested a profile with "Pop" and "Happy" (capitalized) instead of "pop" and "happy", it scored zero genre and mood points even though a matching pop/happy song existed in the catalog. Related labels aren't connected either - "indie pop" never counts as a match for "pop", and "chill" never counts as a match for "relaxed", even though they're musically close. This means the system can quietly exclude users just because of how they phrase a preference, not because a good match doesn't exist.

The catalog itself amplifies these issues. Genres like jazz, classical, folk, country, metal, and edm each appear only once in the 18-song dataset, while pop and lofi appear 2-3 times. Since the genre bonus can only ever apply to whichever single song matches, fans of the less-represented genres are structurally limited to one "in-bubble" recommendation, with the rest of their top 5 being energy-driven compromises from more common genres. There's also no artist diversity control, so a user whose target energy lands near several songs by the same artist (LoRoom has 3, Neon Echo has 2) can end up with a top-5 list dominated by just one or two artists.

Finally, the acoustic bonus only rewards users who set likes_acoustic to true - there's no equivalent signal for someone who explicitly wants non-acoustic music, so that preference isn't modeled at all.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested adversial cases and edge cases using three user profiles with the genre not spelt in all lowercase, conflicting user preferences, and high energy score. The second user profile suprised me. With conflicting preferences, high energy and sad mood, it recommended songs like Neon Pulse Overdrive, which is edm and euphoric. This does not resemble closely to jazz or sadness at all. 
user_prefs =  {"genre": "Pop", "mood": "Happy", "energy": 0.8}
Loaded songs: 18

Top Recommendations
========================================
1. Concrete Throne  (Score: 1.00)
     - energy close to target (+1.00)

2. Sunrise City  (Score: 0.98)
     - energy close to target (+0.98)

3. Rooftop Lights  (Score: 0.96)
     - energy close to target (+0.96)

4. Night Drive Loop  (Score: 0.95)
     - energy close to target (+0.95)

5. Storm Runner  (Score: 0.89)
     - energy close to target (+0.89)

{"genre": "jazz", "mood": "sad", "energy": 0.95}
Top Recommendations
========================================
1. Coffee Shop Stories  (Score: 2.42)
     - genre match (+2.0)
     - energy close to target (+0.42)

2. Neon Pulse Overdrive  (Score: 1.00)
     - energy close to target (+1.00)

3. Gym Hero  (Score: 0.98)
     - energy close to target (+0.98)

4. Iron Verdict  (Score: 0.98)
     - energy close to target (+0.98)

5. Storm Runner  (Score: 0.96)
     - energy close to target (+0.96) 

{"genre": "pop", "mood": "happy", "energy": 1.6}
 Top Recommendations
========================================
1. Sunrise City  (Score: 3.22)
     - genre match (+2.0)
     - mood match (+1.0)
     - energy close to target (+0.22)

2. Gym Hero  (Score: 2.33)
     - genre match (+2.0)
     - energy close to target (+0.33)

3. Rooftop Lights  (Score: 1.16)
     - mood match (+1.0)
     - energy close to target (+0.16)

4. Iron Verdict  (Score: 0.37)
     - energy close to target (+0.37)

5. Neon Pulse Overdrive  (Score: 0.35)
     - energy close to target (+0.35)

After changing the weights in the scoring system, such that genre weight is now 1 and energy weight is 2, in the jazz/sad/0.95 user profile, coffee shop stories dropped from first to fifth and was replaced by Neon Pulse Overdrive, which I originally flagged as a poor recommendation based on the user's preferences. These changes in weights worsened the recommendation output.

For the Pop/Happy/0.8 profile, before the top pick was Concrete Throne and after the order remained unchanged because only energy was ever scored here due to the genre Pop not being considered.

For the pop/happy/1.6 user profile, before the top pick was Sunrise City, and afterwards it stayed the same because this song fulfilled three of the user's preferences.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would improve the model by expand the song catalog for greater representation. In addition, I would fix the exact-match bias such that sad would be the same as melancholic.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems are difficult to handle with a user can have a wide variety of diverse tastes. How to weigh different features when a user may prioritize different preferences? A more complex music recommendation system require managing a larger dataset of songs. I used AI tools and the plan mode heavily to understand the implementation of the logic of my code before accepting the changes. This helped me better understand my system. Next time, I would try to fix the edge cases and make the music recommender more interactive, allowing users to inupt their own profiles into the system.
