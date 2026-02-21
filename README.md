# Smart-Playlist-Intelligence-System

## Description
Playlist analysis and recommendation

## How the Program Works

1. The program first asks the user to enter the number of songs and their durations.
2. It checks whether any duration is invalid (less than or equal to zero).
3. If the playlist is valid, it calculates the total duration and number of songs.
4. Then it applies logical conditions to determine the playlist category.
5. Finally, it prints the total duration, number of songs, detected category, and recommendation.

---

## Categories Used

- Too Short Playlist → Total duration less than 300 seconds
- Too Long Playlist → Total duration greater than 3600 seconds
- Repetitive Playlist → Same duration appears more than once
- Balanced Playlist → Proper duration with no repetition
- Irregular Playlist → Does not fit other categories

---

## Example Input

Enter number of songs: 4  
Enter duration in seconds: 180  
Enter duration in seconds: 200  
Enter duration in seconds: 220  
Enter duration in seconds: 210  

---

## Example Output

Total Duration: 810 seconds  
Songs: 4  
Category: Balanced Playlist  
Recommendation: Good listening session  

---

## Learning Outcome

This program helped me understand how to take user input, use lists to store data, and apply loops and conditions to analyze values. It also improved my logical thinking while solving a real-world style problem in Python.

---

## Constraints Followed

- Used list as main data structure
- Implemented logical checks using loops and conditions
- No hard-coded outputs
- Works for different valid inputs

---

## Files Included

playlist_program.py → Python source code  
README.md → Documentation
