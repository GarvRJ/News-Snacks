from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.tokenize import sent_tokenize

tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")


def sent_paraphraser(sentence):
    sentence = "paraphrase: " + sentence + " </s>"
    encoding = tokenizer.encode_plus(sentence, padding=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]
    para_sents = model.generate(
        input_ids=input_ids,
        attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1
    )
    para_sent = tokenizer.decode(para_sents[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return para_sent


def paraphraser(input_text):
    output = " ".join([sent_paraphraser(sent) for sent in sent_tokenize(input_text)])
    return output
