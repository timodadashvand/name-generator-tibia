import requests

class NameGenerator:
    list_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    list_vowels = ["a", "e", "i", "o", "u", "y"]
    URL = "https://www.tibia.com/community/?subtopic=characters&name="

    for i in list_consonants:
        for j in list_vowels:
            tempName = list_consonants[i] + list_vowels[j]
            resp = requests.get(URL + tempName)
            data = resp.json()
            print(data)
            break
