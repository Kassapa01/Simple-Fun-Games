import time
import random

# Quiz introduction with enhanced visuals
print("🎮" + "="*40 + "🎮")
print("          WELCOME TO THE ULTIMATE QUIZ CHALLENGE!")
print("🎮" + "="*40 + "🎮")
print()

# Ask if player wants to play with more engaging text
playing = input("Are you ready to test your knowledge? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time! 👋")
    quit()

print()
print("Awesome! Let's begin our knowledge adventure! 🚀")
print("Loading questions", end="")
for i in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print()
print()

# Initialize score
score = 0
total_questions = 5

# Question 1
print("1. 🌍 Which planet do we live on?")
answer = input("Your answer: ")
if answer.lower() == "earth":
    print("✅ Correct! You're standing on it right now!")
    score += 1
else:
    print("❌ Sorry, we live on Earth!")
print()

# Question 2
print("2. 🧠 How many brains does an octopus have?")
answer = input("Your answer: ")
if answer.lower() == "nine" or answer.lower() == "9":
    print("✅ Amazing! Octopuses have one central brain and eight mini-brains in their tentacles!")
    score += 1
else:
    print("❌ Actually, octopuses have nine brains!")
print()

# Question 3
print("3. 🔥 What is the hottest planet in our solar system?")
answer = input("Your answer: ")
if answer.lower() == "venus":
    print("✅ Correct! Venus has a surface temperature of about 465°C!")
    score += 1
else:
    print("❌ It's actually Venus, not Mercury as many think!")
print()

# Question 4
print("4. 💧 What percentage of the human body is water?")
answer = input("Your answer: ")
if answer.lower() == "60%" or answer.lower() == "60" or answer.lower() == "sixty percent":
    print("✅ Exactly! About 60% of the human body is water!")
    score += 1
else:
    print("❌ The human body is about 60% water!")
print()

# Question 5
print("5. 🐝 How many eyes does a bee have?")
answer = input("Your answer: ")
if answer.lower() == "five" or answer.lower() == "5":
    print("✅ Wow, you know your insects! Bees have 5 eyes!")
    score += 1
else:
    print("❌ Actually, bees have five eyes - two large compound eyes and three small simple eyes!")
print()

# Calculate final score and provide feedback
percentage = (score / total_questions) * 100

print("📊" + "="*40)
print("             QUIZ RESULTS")
print("📊" + "="*40)
print(f"You got {score} out of {total_questions} questions correct!")
print(f"That's {percentage}%!")

# Personalized feedback based on score
if percentage == 100:
    print("🎉 PERFECT SCORE! You're a genius! 🌟")
elif percentage >= 80:
    print("👍 Excellent job! You really know your stuff!")
elif percentage >= 60:
    print("😊 Good effort! Keep learning!")
else:
    print("👏 Thanks for playing! Keep exploring and learning!")

print("Thanks for playing the Ultimate Quiz Challenge! 🎯")