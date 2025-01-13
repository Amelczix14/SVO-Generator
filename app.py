from flask import Flask, render_template, request, jsonify
from data.subjects import (nouns_s, verbs, irregular_verbs, pronouns, adjectives,
                           determiners_singular, determiners_plural, possessives, verb_completions)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_subjects', methods=['GET'])
def get_subjects():
    subject_type = request.args.get('subject_type')
    exceptions = request.args.get('exceptions')

    if exceptions == 'true':
        return jsonify(nouns_s["exceptions"])

    if subject_type == 'pronoun':
        return jsonify(pronouns)
    elif subject_type == 'noun':
        all_nouns = []
        for category, nouns_list in nouns_s["regulars"].items():
            all_nouns.extend(nouns_list)
        all_nouns.extend(nouns_s["exceptions"].keys())
        return jsonify(all_nouns)
    return jsonify([])


@app.route('/get_determiners', methods=['GET'])
def get_determiners():
    number = request.args.get('number')
    subject = request.args.get('subject', '')
    determiners = []

    if number == 'singular':
        determiners = determiners_singular.copy()
        if subject:
            if subject[0].lower() in 'aeiou':
                determiners.append('an')
            else:
                determiners.append('a')
    elif number == 'plural':
        determiners = determiners_plural.copy()

    determiners.extend(possessives)

    return jsonify(determiners)


@app.route('/get_adjectives', methods=['GET'])
def get_adjectives():
    return jsonify(adjectives)


@app.route('/get_verbs', methods=['GET'])
def get_verbs():
    all_verbs = verbs["regular"] + list(verbs["irregular"].keys())
    return jsonify(all_verbs)


@app.route('/get_complements', methods=['GET'])
def get_complements():
    verb = request.args.get('verb')
    if verb in verb_completions:
        return jsonify(verb_completions[verb])
    return jsonify([])


@app.route('/generate_sentence', methods=['POST'])
def generate_sentence():
    data = request.json
    subject = data['subject']
    verb = data['verb']
    determiner = data['determiner']
    adjective = data['adjective']
    complement = data['complement']
    number = data['number']
    tense = data['tense']

    sentence = construct_sentence(subject, verb, determiner, adjective, complement, number, tense)
    sentence = sentence.capitalize()

    return jsonify({'sentence': sentence})


def construct_sentence(subject, verb, determiner, adjective, complement, number, tense):
    sentence = (f"{determiner if determiner else ''} {adjective} {subject} "
                f"{conjugate_verb(subject, verb, number, tense) if verb else ''} "
                f"{complement}").strip()

    return sentence


def conjugate_verb(subject, verb, number, tense):
    if verb is not None:
        if tense == "present":
            if number == "singular" and subject not in ["I", "you"]:
                if verb.endswith(('s', 'sh', 'ch', 'x', 'z')):
                    return verb + "es"
                elif verb.endswith('y') and verb[-2] not in "aeiou":
                    return verb[:-1] + "ies"
                else:
                    return verb + "s"
            return verb
        elif tense == "past":
            return get_past_tense(verb)
        elif tense == "future":
            return f"will {verb}"


def get_past_tense(verb):
    if verb in irregular_verbs:
        return irregular_verbs[verb]
    elif verb.endswith("p"):
        return verb + "ped"
    elif verb.endswith("y") and verb[-2] not in "aeiou":
        return verb[:-1] + "ied"
    elif verb.endswith("g"):
        return verb + "ged"
    elif verb.endswith("e"):
        return verb + "d"
    else:
        return verb + "ed"


if __name__ == "__main__":
    app.run(debug=True)
