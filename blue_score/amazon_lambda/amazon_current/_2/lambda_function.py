import json


def respond(res):
    return {

        'statusCode': '200',
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },

    }


def lambda_handler(event, context):
    try:
        print('Loading function')
        import os
        print(os.path.dirname(os.path.realpath(__file__)))
        print(os.getcwd())

        import nltk
        nltk.data.path.append("/var/task/nltk_data")
        from nltk.translate.bleu_score import corpus_bleu
        from nltk.tokenize import word_tokenize

        body = event['body']
        body = json.loads(body)
        for el in body:
            print(el)  # arrayRawMT	arrayReference

        print(body["arrayReference"])
        print("===========================")
        print(body["arrayHypothesis"])

        reference_tokenized = [[word_tokenize(i.lower())] for i in body["arrayReference"]]
        candidate_tokenized = [word_tokenize(i.lower()) for i in body["arrayHypothesis"]]

        result = corpus_bleu(reference_tokenized, candidate_tokenized)
        result = round(result*100, 2)

        return respond(result)

    except Exception as ex:
        print("Exception: ", str(ex))
        return respond(str(ex))
