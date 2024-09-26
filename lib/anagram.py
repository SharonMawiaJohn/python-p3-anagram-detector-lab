# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word=word

    def match(self, anagram_options):
        sorted_word = sorted(self.word)
        matches = [anagram for anagram in anagram_options if sorted(anagram) == sorted_word]
        return matches