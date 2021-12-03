from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from openpyxl import load_workbook

workbook = load_workbook(filename="work_docs/blue/_1.xlsx")


reference = [
    'this is a dog'.split(),
    'it is dog'.split(),
    'dog it is'.split(),
    'a dog, it is'.split()
]

candidate = 'it is a dog'.split()

print('BLEU score -> {}'.format(sentence_bleu(reference, candidate)))

# reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
# candidate = ['this', 'is', 'a', 'test']
# score = sentence_bleu(reference, candidate)
# print(score)