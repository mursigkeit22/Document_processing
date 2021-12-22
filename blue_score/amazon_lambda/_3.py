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
        print("changed")

        from nltk.translate.bleu_score import corpus_bleu
        from nltk.tokenize import word_tokenize
        body = event['body']
        body = json.loads(body)
        for el in body:
            print(el)  # arrayRawMT	arrayReference

        # придется здесь токенизировать каждый элемент. и регистр тоже здесь тогда

        print(body["arrayReference"])
        print("===========================")
        print(body["arrayHypothesis"])

        reference_tokenized = body["arrayReference"]
        candidate_tokenized = body["arrayHypothesis"]
        result = corpus_bleu(reference_tokenized, candidate_tokenized)

        return respond(result)

    except Exception as ex:
        print("Exception: ", str(ex))
        return respond(str(ex))
