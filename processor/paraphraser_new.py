import nltk
from nltk.corpus import wordnet


def paraphrase_paragraph(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    paraphrased_paragraphs = []
    for sentence in sentences:
        paraphrased_sentences = paraphrase_sentence(sentence)
        paraphrased_paragraphs.extend(paraphrased_sentences)

    return paraphrased_paragraphs


def paraphrase_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    paraphrased_sentences = []
    for word, pos in pos_tags:
        if pos.startswith('NN') or pos.startswith('VB'):
            synonyms = wordnet.synsets(word)

            if synonyms:
                paraphrased_word = synonyms[0].lemmas()[0].name()
                paraphrased_sentence = sentence.replace(word, paraphrased_word)
                paraphrased_sentences.append(paraphrased_sentence)

    return paraphrased_sentences
