import random
import hangman_stages
import words

lives = 6
chosen_word = random.choice(words.word)

# Create blanks
display = []
for _ in chosen_word:
    display += "_"

print("Welcome to Hangman! 🎉")
print(" ".join(display))

game_over = False
guessed_letters = []

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    # Check if already guessed
    if guessed_letter in guessed_letters:
        print(f"⚠️ You already guessed '{guessed_letter}'. Try another letter.")
        continue
    guessed_letters.append(guessed_letter)

    # Reveal guessed letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(" ".join(display))

    # Wrong guess
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")
        print(hangman_stages.stages[lives])
        if lives == 0:
            game_over = True
            print(f"You lose! The word was '{chosen_word}'.")

    # Check win
    if "_" not in display:
        game_over = True
        print("🎉 Congratulations, you won! 🏆")