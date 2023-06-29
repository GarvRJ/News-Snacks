from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarizer(text):
    sum_up = LexRankSummarizer()

    # Parse the article text and tokenize it into sentences
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Summarize the article and get the top N sentences
    summary_sentences = sum_up(parser.document, 4)

    # Join the summary sentences into a single string
    summary = ' '.join(str(sentence) for sentence in summary_sentences)

    return summary
