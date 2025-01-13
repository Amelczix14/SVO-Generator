function handleSubjectTypeChange() {
    const subjectType = document.getElementById('subjectType');
    const subjectSelect = document.getElementById('subject');
    const button = document.getElementById('button');

    // if (subjectType.options[0].value === "") {
    //     subjectType.remove(0);
    // }

    subjectSelect.innerHTML = '';
    subjectSelect.disabled = true;
    fetch(`/get_subjects?subject_type=${subjectType.value}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                subjectSelect.innerHTML = data.map(subject =>
                    `<option value="${subject}">${subject}</option>`
                ).join('');

                subjectSelect.disabled = false;
                button.disabled = false;
            }
            document.getElementById('subjectOptions').style.display = "flex";
        });

    document.getElementById('determinerOptions').style.display = "none";
    document.getElementById('verbOptions').style.display = "none";
    document.getElementById('complementOptions').style.display = "none";
    document.getElementById('generatedSentence').textContent = '';
}

function handleSubject() {
    const subjectType = document.getElementById('subjectType').value;

    document.querySelector('.options').style.display = "none";
    document.getElementById('subjectOptions').style.display = "none";

    if (subjectType === "noun") {
        document.getElementById('numberOptions').style.display = "flex";
    } else {
        handleVerb()
    }

    generateSentence();
}

async function handleNumber() {
    const number = document.getElementById('number').value;
    const subjectSelect = document.getElementById('subject');
    const subject = subjectSelect.value;

    let updatedSubject = subject;
    if (number === "plural") {
        updatedSubject = await pluralize(subject); 
    }

    const updatedOption = document.createElement('option');
    updatedOption.value = updatedSubject;
    updatedOption.textContent = updatedSubject;
    subjectSelect.innerHTML = '';
    subjectSelect.appendChild(updatedOption);
    subjectSelect.value = updatedSubject;

    document.getElementById('numberOptions').style.display = "none";

    fetch(`/get_determiners?number=${number}&subject=${updatedSubject}`)
        .then(response => response.json())
        .then(data => {
            const determinerSelect = document.getElementById('determiner');

            const emptyOption = document.createElement('option');
            emptyOption.value = '';
            emptyOption.textContent = '-';
            determinerSelect.appendChild(emptyOption);

            determinerSelect.innerHTML += data.map(determiner =>
                `<option value="${determiner}">${determiner}</option>`
            ).join('');

            determinerSelect.disabled = false;

            document.getElementById('determinerOptions').style.display = "flex";
        })
        .catch(error => {
            console.error('Error fetching determiners:', error);
        });

    generateSentence();
}

async function pluralize(word) {

    const response = await fetch(`/get_subjects?exceptions=true`);
    const data = await response.json();

    if (data.hasOwnProperty(word)) {
        const value = data[word];
        console.log(`Wartość dla klucza "${word}":`, value);
        return value;
    } else if (word.endsWith('s') || word.endsWith('x') || word.endsWith('z') || word.endsWith('ch') || word.endsWith('sh')) {
        return word + 'es';
    } else if (word.endsWith('y') && !"aeiou".includes(word[word.length - 2])) {
        return word.slice(0, -1) + 'ies';
    } else {
        return word + 's';
    }
}

function handleDeterminer() {
    const determiner = document.getElementById('determiner').value;

    if (determiner === '') {
        console.log('Determiner is None');
    } else {
        console.log('Selected determiner:', determiner);
    }

    document.getElementById('determinerOptions').style.display = "none";

    fetch('/get_adjectives') 
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const adjectiveSelect = document.getElementById('adjective');
        adjectiveSelect.innerHTML = ''; 
        adjectiveSelect.disabled = true;

        adjectiveSelect.innerHTML = data.map(adjective =>
            `<option value="${adjective}">${adjective}</option>`
        ).join('');

        adjectiveSelect.disabled = false;
        document.getElementById('adjectiveOptions').style.display = "flex"; 
    })
    .catch(error => {
        console.error('Error fetching adjectives:', error);
    });



    generateSentence();
}

function handleAdjective() {
    document.getElementById('adjectiveOptions').style.display = "none"; 
    handleVerb()
    document.getElementById('verbOptions').style.display = "flex";
    document.getElementById('tenseOptions').style.display = "flex";
    generateSentence();
}



function handleVerb() {
    const verbSelect = document.getElementById('verb');
    verbSelect.innerHTML = '';
    verbSelect.disabled = true;

    fetch('/get_verbs')
        .then(response => response.json())
        .then(data => {
            verbSelect.innerHTML = data.map(verb =>
                `<option value="${verb}">${verb}</option>`
            ).join('');

            verbSelect.disabled = false;

            document.getElementById('verbOptions').style.display = "flex";
            document.getElementById('tenseOptions').style.display = "flex";
            
        })
        .catch(error => {
            console.error('Error fetching verbs:', error);
        });
}

function handleVerbChange() {
    const selectedVerb = document.getElementById('verb').value;
    const selectedTense = document.getElementById('tense').value;

    document.getElementById('verbOptions').style.display = "none";
    document.getElementById('tenseOptions').style.display = "none";

    document.getElementById('complementOptions').style.display = "flex";

    fetch(`/get_complements?verb=${selectedVerb}`)
        .then(response => response.json())
        .then(data => {
            const complementSelect = document.getElementById('complement');

            complementSelect.innerHTML = data.map(complement =>
                `<option value="${complement}">${complement}</option>`
            ).join('');

            complementSelect.disabled = false;
        })
        .catch(error => {
            console.error('Error fetching complements:', error);
        });

    generateSentence()
}

function handleComplement() {
    const selectedComplement = document.getElementById('complement').value;

    document.getElementById('complementOptions').style.display = "none";

    const resetButton = document.querySelector('button[onclick="handleReset()"]');
    resetButton.style.display = "block";

    generateSentence();
}

function generateSentence() {
    const subject = document.getElementById('subject').value;
    const verb = document.getElementById('verb').value;
    const determiner = document.getElementById('determiner') ? document.getElementById('determiner').value : '';
    const adjective = document.getElementById('adjective') ? document.getElementById('adjective').value : '';
    const complement = document.getElementById('complement') ? document.getElementById('complement').value : '';
    const number = document.getElementById('number').value;
    const tense = document.getElementById('tense').value;

    console.log(subject);

    const data = {
        subject, verb, determiner, adjective, complement, number, tense
    };
    console.log(data);

    fetch('/generate_sentence', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('generatedSentence').textContent = data.sentence;
    });
}

function handleReset() {
    location.reload();
    document.getElementById('subject').disabled = false;
    document.getElementById('subjectType').options[0].selected = true;

}

