#Q2.Python program that accepts a word from the user and reverses it.

class WordReverser:
    def __init__(self, word):
        self.word = word

    def reverse_word(self):
        return self.word[::-1]

word = input("Enter a word: ")

word_reverser = WordReverser(word)

reversed_word = word_reverser.reverse_word()

print(f"The reversed word is: {reversed_word}")



