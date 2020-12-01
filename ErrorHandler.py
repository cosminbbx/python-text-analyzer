import json

f = open('ErrorMesseges.json',)

errorMessages = json.load(f)

def handleError(errorType):
    if errorMessages[errorType]:
        print(errorMessages[errorType])
    else:
        print(errorMessages["GenericError"])