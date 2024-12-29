pronouns = ["I", "you", "he", "she", "it", "we", "they"]

nouns_s = {
    "exceptions": {
        "man": "men",
        "woman": "women",
        "child": "children",
    },
    "regulars": {
        "people": [
            "boy", "girl", "teacher", "doctor", "student", "policeman", "driver", "musician", "lawyer", "friend",
            "brother", "sister", "father", "mother", "uncle", "aunt", "cousin"
        ],
        "animals": [
            "dog", "cat", "fox", "rabbit", "rat"
        ]
    }
}

# adjectives = [
#     "tall", "short", "big", "small", "little", "strong", "weak", "pretty", "ugly", "young", "old",
#     "friendly", "shy", "lazy", "intelligent", "smart", "stupid", "funny", "happy", "sad", "angry",
#     "excited", "noisy", "quiet", "good", "scary"
# ]


determiners_singular = ["this", "that", "the"]
determiners_plural = ["these", "those"]
possessives = ["my", "your", "his", "her", "its", "our", "their"]

regular_verbs = [
    "watch", "play", "cook", "use", "climb", "paint", "wash", "carry", "fix", "bake", "open", "close"
]

irregular_verbs = {
    "eat": "ate",
    "drink": "drank",
    "read": "read",
    "write": "wrote",
    "drive": "drove",
    "ride": "rode",
    "draw": "drew",
    "take": "took",
    "break": "broke",
    "buy": "bought",
    "throw": "threw",
    "wear": "wore",
    "steal": "stole",
    "feed": "fed"
}

verbs = {
    "regular": regular_verbs,
    "irregular": irregular_verbs
}


verb_completions = {
    "eat": ["an apple", "pizza", "dinner", "fish", "candy", "a banana", "a sandwich", "soup", "pasta", "a burger"],
    "read": ["a book", "the newspaper", "a magazine", "an article", "a letter", "a novel", "a comic", "a poem"],
    "watch": ["a movie", "TV", "a video", "a show", "football", "a concert", "volleyball", "tennis", "a match"],
    "write": ["a letter", "an email", "an essay", "a report", "a note", "a message", "an article", "a story"],
    "play": ["football", "tennis", "basketball", "chess", "the guitar", "the piano", "drums", "video games"],
    "cook": ["a meal", "dinner", "lunch", "breakfast", "a dish", "soup", "pasta"],
    "drink": ["water", "juice", "coffee", "tea", "milk", "soda", "beer", "wine"],
    "drive": ["a car", "a bus", "a truck", "a van", "a scooter", "a tractor", "a jeep", "a limousine", "an ambulance"],
    "ride": ["a bike", "a horse", "a motorcycle", "a bus", "a train", "a rollercoaster", "a skateboard"],
    "draw": ["a picture", "a portrait", "a landscape", "a cartoon", "a sketch"],
    "take": ["a photo", "a shower", "medicine", "a break", "a train", "a bus"],
    "break": ["a glass", "a window", "a rule", "a plate"],
    "use": ["a phone", "a computer", "a microwave", "tools", "the internet"],
    "climb": ["a mountain", "a tree", "a ladder", "stairs", "a rock", "a wall"],
    "buy": ["clothes", "groceries", "shoes", "a car", "food", "books"],
    "paint": ["a house", "a picture", "a wall", "nails", "artwork"],
    "wash": ["hands", "a car", "clothes", "dishes", "windows"],
    "carry": ["a bag", "luggage", "a box", "a book", "a child", "items"],
    "throw": ["a ball", "a stone", "paper", "garbage", "a rock"],
    "wear": ["clothes", "a hat", "glasses", "shoes", "socks"],
    "steal": ["money", "a car", "a bag", "jewels", "food", "a phone"],
    "fix": ["a car", "a computer", "a phone", "furniture", "a problem"],
    "bake": ["a cake", "bread", "cookies", "pizza", "a pie"],
    "open": ["a door", "a window", "a book", "a box", "an email"],
    "close": ["a door", "a window", "a book", "a file", "eyes"],
    "feed": ["a cat", "a dog", "a bird", "a baby", "fish"]
}


