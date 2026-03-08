# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
The game did not work functionally the first time I ran it. The following problems were noticed:
- The hints were backwards. For example, should be "GO HIGER" instead of "GO LOWER" if the guess number was lower than the target.
- The range did not match the difficulty level. For example, the range was 1 - 100 for Normal and the range was 1 - 50 for Hard.
- The target number could be larger than the max in the range.
- The NEW GAME button did not function normally.
- Attemps allowed and attempts left did not match.
- Hardcoded range in the info message.
- Secret was converted to string on even attempts.
- Score formula off by one (points = 100 - 10 * (attempt_number + 1))
- Score carries over on new games
- On even-numbered "Too high" attempts, the player gains 5 points.




## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - All AI suggestions given so far were verified to be correct. For example, for the "attempts in total and attempts left not match" error, Claude identified in app.py Line 80 changed to 
    st.session_state.attempts = 0 instead of 1 and fixed this error.
In addition, Claude suggested to change Line 77 on app.py to random.randint(low, high) to generate secrete in the range of low and high to fix the error that secret was not between low and high in the beginning. All suggestions were verified to be correct. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - So far all suggestions given by AI were correct.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - First, I manually went through the code, where the suggested fix was and make sure it make sense. Then I rerun the app and test it manually to make sure the bug was really fixed. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran manually to test all fixes to all the problems I found out. I also asked Claude to write a test case in tests/test_game_logic.py to test whether the hint given was correct. 
- Did AI help you design or understand any tests? How?
  - Yes, I asked Claude to design a test in tests/test_game_logic.py to test whether the hint backwards error was fixed or not.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - Streamlit reruns the entire script from top to bottom every time a user interacts with the app. Every rerun would hit random.randint(low, high) again, so the secret number kept changing in the original app and the player would never win. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit refreshes the app on every click, however, if with session state, it can store values and can be retrieved later. 
- What change did you make that finally gave the game a stable secret number?
  - Add st.session_state. if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
Only generate a new secret if one does not exist yet. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
To let AI help write testing scripts and open a new window of AI for each new problems that you want to fix in the code.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Refer to the correct file or lines of code as reference when asking questions to AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - For all the problems I found out, Claude gave correct and clear suggestions on how to fix them in the code. 
