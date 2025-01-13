from data.subjects import (nouns_s, verbs, irregular_verbs, pronouns,
                           determiners_singular, determiners_plural, verb_completions)


class SentenceGenerator:
    def __init__(self):
        self.subject = None
        self.verb = None
        self.determiner = None
        self.number = None
        self.tense = None
        self.complement = None

    def choose_subject(self):
        print("Choose a subject type:")
        print("1. Pronoun")
        print("2. Noun")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.choose_pronoun()
        elif choice == "2":
            self.choose_noun()
        else:
            print("Invalid choice. Please start over.")
            return self.choose_subject()

    def choose_pronoun(self):
        print("Available pronouns:")
        for i, pronoun in enumerate(pronouns, start=1):
            print(f"{i}. {pronoun}")
        pronoun_choice = int(input("Choose a pronoun (enter the number): "))
        self.subject = pronouns[pronoun_choice - 1]

    def choose_noun(self):
        all_nouns = self.get_all_nouns()

        print("Available nouns:")
        for i, noun in enumerate(all_nouns, start=1):
            print(f"{i}. {noun}")

        noun_choice = int(input("Choose a noun (enter the number): "))
        noun = all_nouns[noun_choice - 1]
        print(f"Chosen noun: {noun}")

        self.choose_number(noun)

    def get_all_nouns(self):
        all_nouns = []
        for category, nouns_list in nouns_s["regulars"].items():
            all_nouns.extend(nouns_list)
        all_nouns.extend(nouns_s["exceptions"].keys())
        return all_nouns

    def choose_number(self, noun):
        print("Choose number:")
        print("1. Singular")
        print("2. Plural")
        number_choice = input("Enter the number of your choice: ")

        if number_choice == "2":
            self.number = "plural"
            self.subject = self.pluralize(noun)
        else:
            self.number = "singular"
            self.subject = noun
        print(f"Chosen subject: {self.subject}")

    def pluralize(self, word):
        if word in nouns_s["exceptions"]:
            return nouns_s["exceptions"][word]

        elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return word + "es"

        elif word[-1] == "y" and word[-2] not in "aeiou":
            return word[:-1] + "ies"

        else:
            return word + "s"

    def choose_determiner(self):
        if self.number == "singular":
            determiners = determiners_singular
            if self.subject[0] in "aeiou":
                determiners.append("an")
            else:
                determiners.append("a")
        elif self.number == "plural":
            determiners = determiners_plural
        else:
            return None

        possessives = ["my", "your", "his", "her", "its", "our", "their"]
        options = determiners + possessives
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print(f"{len(options) + 1}. No determiner or possessive")

        choice = int(input("Enter the number of your choice: "))
        if choice == len(options) + 1:
            self.determiner = None
        else:
            self.determiner = options[choice - 1]

    def choose_verb(self):
        all_verbs = verbs["regular"] + list(verbs["irregular"].keys())

        print("Available verbs:")
        for i, verb in enumerate(all_verbs, start=1):
            print(f"{i}. {verb}")
        verb_choice = int(input("Choose a verb (enter the number): "))
        self.verb = all_verbs[verb_choice - 1]

        return self.choose_tense()

    def choose_tense(self):
        print("Choose the verb tense:")
        print("1. Present")
        print("2. Past")
        print("3. Future")
        tense_choice = input("Enter the number of your choice: ")

        if tense_choice == "1":
            self.tense = "present"
        elif tense_choice == "2":
            self.tense = "past"
        elif tense_choice == "3":
            self.tense = "future"
        else:
            print("Invalid choice. Please choose again.")
            return self.choose_tense()

        verb = self.conjugate_verb()
        return verb

    def conjugate_verb(self):
        if self.tense == "present":
            if self.number == "singular" and self.subject not in ["I", "you"]:
                return self.verb + "s"
            return self.verb

        elif self.tense == "past":
            verb = self.get_past_tense()
            return verb

        elif self.tense == "future":
            return f"will {self.verb}"

    def get_past_tense(self):
        if self.verb in irregular_verbs:
            return irregular_verbs[self.verb]

        elif self.verb.endswith("e"):
            return self.verb + "d"
        else:
            return self.verb + "ed"

    def choose_complement(self):
        if self.verb in verb_completions:
            complements = verb_completions[self.verb]
            print(f"Choose a complement for the verb '{self.verb}':")
            for i, complement in enumerate(complements, start=1):
                print(f"{i}. {complement}")
            complement_choice = int(input("Enter the number of your choice: "))
            self.complement = complements[complement_choice - 1]
            print(f"Chosen complement: {self.complement}")
        else:
            print(f"No complements available for '{self.verb}'.")

    def construct_sentence(self, verb):
        if self.determiner:
            sentence = f"{self.determiner} {self.subject} {verb} {self.complement}"
        else:
            sentence = f"{self.subject} {verb} {self.complement}"

        return sentence

    def main(self):
        self.choose_subject()
        self.choose_determiner()
        verb = self.choose_verb()
        self.choose_complement()

        print("\nGenerated Sentence: ")
        print(self.construct_sentence(verb))


if __name__ == "__main__":
    generator = SentenceGenerator()
    generator.main()
