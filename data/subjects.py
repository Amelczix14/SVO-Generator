pronouns = ["I", "you", "he", "she", "it", "we", "they"]

nouns_s = {
    "exceptions": {
        "man": "men", "woman": "women", "child": "children", "person": "people", "sheep": "sheep", "deer": "deer",
        "mouse": "mice", "goose": "geese", "fish": "fish", "policeman": "policemen", "wolf": "wolves"
    },
    "regulars": {
        "people": [
            "boy", "girl", "teacher", "doctor", "student", "driver", "musician", "lawyer", "friend", "brother",
            "sister", "father", "mother", "uncle", "aunt", "cousin", "grandfather", "grandmother", "nephew",
            "niece", "colleague"
        ],
        "animals": [
            "dog", "cat", "fox", "rabbit", "rat", "horse", "cow", "bird", "elephant", "lion", "tiger",
            "bear", "monkey", "giraffe", "zebra", "panda"
        ]
    }
}

adjectives = [
    "tall", "short", "big", "small", "little", "strong", "weak", "pretty", "ugly", "young",
    "old", "friendly", "shy", "lazy", "intelligent", "smart", "stupid", "funny", "happy", "sad",
    "angry", "excited", "noisy", "quiet", "good", "scary", "brave", "calm", "bright", "dark",
    "gentle", "kind", "rude", "polite", "generous", "greedy", "honest", "dishonest", "energetic", "creative",
    "curious", "determined", "fearful", "fierce", "graceful", "humble", "jealous", "naive", "optimistic", "pessimistic"
]


determiners_singular = ["this", "that", "the"]
determiners_plural = ["these", "those"]
possessives = ["my", "your", "his", "her", "our", "their"]

regular_verbs = [
    "watch", "play", "cook", "use", "climb", "paint", "wash", "carry", "fix", "bake", "open", "close", "dance",
    "clean", "study", "shop", "travel", "explore", "discover", "repair", "call", "listen", "hug", "share", "visit",
    "celebrate", "enjoy", "organize", "plant", "connect", "follow", "calculate", "jump", "build"
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
    "feed": "fed",
    "swim": "swam",
    "teach": "taught"
}

verbs = {
    "regular": regular_verbs,
    "irregular": irregular_verbs
}


verb_completions = {
    "eat": ["an apple", "pizza", "dinner", "fish", "candy", "a banana", "a sandwich", "soup", "pasta", "a burger"],
    "read": ["a book", "the newspaper", "a magazine", "an article", "a letter", "a novel", "a comic", "a poem"],
    "watch": ["a movie", "TV", "a video", "a show", "football", "the sunrise", "the sunset", "the stars" "a match"],
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
    "paint": ["a house", "a picture", "a wall", "nails", "artwork", "a fence", "a canvas", "a room", "a sculpture"],
    "wash": ["hands", "a car", "clothes", "dishes", "windows"],
    "carry": ["a bag", "luggage", "a box", "a book", "a child", "items"],
    "throw": ["a ball", "a stone", "paper", "garbage", "a rock"],
    "wear": ["clothes", "a hat", "glasses", "shoes", "socks"],
    "steal": ["money", "a car", "a bag", "jewels", "food", "a phone"],
    "fix": ["a car", "a computer", "a phone", "furniture", "a problem"],
    "bake": ["a cake", "bread", "cookies", "pizza", "a pie"],
    "open": ["a door", "a window", "a book", "a box", "an email"],
    "close": ["a door", "a window", "a book", "a file", "eyes"],
    "feed": ["a cat", "a dog", "a bird", "a baby", "a fish"],
    "swim": ["in the pool", "in the sea", "in the lake", "in the ocean"],
    "dance": ["solo","salsa", "ballet", "hip-hop", "waltz", "the tango"],
    "clean": ["the house", "the floor", "the windows", "the kitchen", "the bathroom"],
    "study": ["mathematics", "history", "biology", "languages", "art"],
    "shop": ["for groceries", "for clothes", "for shoes", "for gifts", "online"],
    "travel": ["abroad", "to the mountains", "to the beach", "to a new country", "around the world"],
    "explore": ["a city", "a forest", "a cave", "the countryside"],
    "teach": ["others", "math", "science", "music", "history", "art"],
    "discover": ["a new place", "a hidden talent", "a new hobby", "an invention"],
    "repair": ["a bike", "a computer", "a watch", "a roof", "a fence"],
    "call": ["a friend", "a family member", "customer service", "a taxi", "an ambulance", "the police"],
    "listen": ["to music", "to a podcast", "to the radio", "to an audiobook", "to a lecture"],
    "hug": ["a friend", "a family member", "a pet", "a teddy bear"],
    "share": ["an idea", "a meal", "a story", "a photo", "a video"],
    "visit": ["a friend", "a relative", "a museum", "a park", "a city"],
    "celebrate": ["a birthday", "a holiday", "a promotion", "an anniversary", "a victory"],
    "enjoy": ["the sunset", "a concert", "a meal", "a vacation", "a good book"],
    "organize": ["a party", "a meeting", "a trip", "a closet", "a schedule"],
    "plant": ["a tree", "flowers", "vegetables", "a garden", "a seed"],
    "connect": ["to the internet", "with friends", "with family", "to a device", "with nature"],
    "follow": ["the rules", "instructions", "a map", "a trend", "someone on social media"],
    "calculate": ["the total", "the distance", "the time", "the cost", "the score"],
    "jump": ["over a fence", "into the water", "on a trampoline", "over a puddle", "on a bed", "into the pool"],
    "build": ["a house", "a sandcastle", "a bridge", "a robot", "a treehouse", "a website", "a tower", "a relationship"]
}


