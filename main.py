import requests
from bs4 import BeautifulSoup

class NameGenerator:
    list_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    list_vowels = ["a", "e", "i", "o", "u", "y"]
    URL = "https://www.tibia.com/community/?subtopic=characters&name="

    @classmethod
    def generate_names(cls, output_file="available_names.txt"):
        with open(output_file, "w", encoding="utf-8") as f:
            # Check consonant + vowel
            for consonant in cls.list_consonants:
                for vowel in cls.list_vowels:
                    temp_name = consonant + vowel
                    result, available = cls.check_name(temp_name)
                    print(result)
                    if available:
                        f.write(result + "\n")

            # Check vowel + consonant
            for vowel in cls.list_vowels:
                for consonant in cls.list_consonants:
                    temp_name = vowel + consonant
                    result, available = cls.check_name(temp_name)
                    print(result)
                    if available:
                        f.write(result + "\n")

    @classmethod
    def check_name(cls, name):
        response = requests.get(cls.URL + name)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text().lower()

        if "could not find character" in content:
            return f"{name} ✅ Name is available (not taken)", True
        else:
            return f"{name} ❌ Name is taken", False

# Run the generator
NameGenerator.generate_names()
