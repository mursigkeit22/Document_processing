from nltk import word_tokenize
from nltk.translate.bleu_score import corpus_bleu

with open("./texts/RawMT.txt", "r", encoding="utf-8") as f1:
    candidate = f1.readlines()
    candidate_tokenized = [word_tokenize(i.lower()) for i in candidate]
    print(candidate_tokenized)

with open("./texts/MTPostEdited.txt", "r", encoding="utf-8") as f2:
    reference = f2.readlines()
    reference_tokenized = [[word_tokenize(i.lower())] for i in reference]
    print(reference_tokenized)

print(corpus_bleu(reference_tokenized, candidate_tokenized))
