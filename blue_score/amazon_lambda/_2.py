import json
import base64
import ast
import unicodedata

print('Loading function')


def respond(res):
    return {

        'statusCode': '200',
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },

    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.


    '''
    body = event['body']
    body = json.loads(body)
    for el in body:
        print(el)  # arrayRawMT	arrayReference

    # пусть первый всегда будет референсом, а второй всегда гипотезой - сразу как при подсчете

    # for el in body["arrayReference"][:10]:
    #     print(el)
    # for el in body["arrayHypothesis"][:10]:
    #     print(el)

    # придется здесь токенизировать каждый элемент. и регистр тоже здесь тогда уберем

    print(body["arrayReference"])
    print("===========================")
    print(body["arrayHypothesis"])
    # print(unicodedata.normalize("NFKD", el[0]))
    # text = [unicodedata.normalize("NFKD", i[0]) for i in body["arrayRawMT"]]
    # print(text)

    # body = body.decode("utf-8")
    # body = body.decode("utf-8")
    # body = ast.literal_eval(body)
    # print(str(body["arrayRawMT"]))
    # body = ast.literal_eval(body)

    # print("arrayReference: ", body["arrayReference"])

    # body = body.decode("utf-8")
    # print("type(body): ", type(body))

    # print("BODY arrayRawMT ", body["arrayRawMT"])
    # print("BODY arrayReference ", body["arrayReference"])

    # print("Received event: " + json.dumps(event, indent=2))
    a = json.dumps(event, indent=2)

    return respond("hop")

    # if operation in operations:
    #     payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    #     return respond(None, operations[operation](dynamo, payload))
    # else:
    #     return respond(ValueError('Unsupported method "{}"'.format(operation)))
