from natasha_parser import Natasha_Parser
from generate_rus_vocab import vocab
from re import search

def give_suggestion(misspelled_one, vocab_one):
    if abs(len(misspelled_one) - len(vocab_one)) > 1: # no suggestions if the word lens differ a lot
        return None

    same_char_count = 0
    min_len = min(len(misspelled_one), len(vocab_one))
    for i in range(min_len):
        same_char_count += (misspelled_one[i] == vocab_one[i])

    if min_len - same_char_count <= 1: # return the suggestion (vocabulary word) if few differences
        return vocab_one
    else:
        return None


def spelling_corrector(filename):
    # Step 1: Identify misspelled words
    nap = Natasha_Parser(filename)
    nap.segmentation()
    nap.morphology()
    nap.lemmatization()

    words = [_.text for _ in nap.doc.tokens 
    if (_.text.isalpha() or bool(search(r"[А-я+][-][А-я+]", _.text))) and len(_.text) > 1] # only letter-words (including hyphen-connected ones)

    misspelled = [word for word in words if word.lower() not in vocab and word.title() not in vocab]
    
    # Step 2: Provide with possible correct versions for each misspelled word
    for misspelled_one in misspelled:
        suggestions = []
        for vocab_one in vocab:
            suggestion = give_suggestion(misspelled_one, vocab_one)
            if suggestion != None:
                suggestions.append(suggestion)

        print(f'Suggestions for {misspelled_one}: {suggestions}')

    

filename = './test/test.txt'
spelling_corrector(filename)