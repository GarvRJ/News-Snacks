import nltk
from nltk.corpus import wordnet


def paraphrase_paragraph(paragraph):
    # Tokenize the paragraph into sentences
    sentences = nltk.sent_tokenize(paragraph)

    # Initialize an empty list to store paraphrased paragraphs
    paraphrased_paragraphs = []

    # Iterate over each sentence and paraphrase it
    for sentence in sentences:
        paraphrased_sentences = paraphrase_sentence(sentence)
        paraphrased_paragraphs.extend(paraphrased_sentences)

    return paraphrased_paragraphs


def paraphrase_sentence(sentence):
    # Tokenize the sentence
    words = nltk.word_tokenize(sentence)

    # Identify the part of speech (POS) for each word
    pos_tags = nltk.pos_tag(words)

    # Initialize an empty list to store paraphrased sentences
    paraphrased_sentences = []

    # Iterate over each word and find synonyms for nouns and verbs
    for word, pos in pos_tags:
        if pos.startswith('NN') or pos.startswith('VB'):
            # Get synonyms for the word
            synonyms = wordnet.synsets(word)

            if synonyms:
                # Get the first synonym and replace the word in the sentence
                paraphrased_word = synonyms[0].lemmas()[0].name()
                paraphrased_sentence = sentence.replace(word, paraphrased_word)

                # Add the paraphrased sentence to the list
                paraphrased_sentences.append(paraphrased_sentence)

    return paraphrased_sentences
