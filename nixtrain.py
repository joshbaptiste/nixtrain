import json
from __future__ import print_function
import blessings
from bottle import route, run, debug, request


@post('nixtrain/questions')
def get_question():
    question = request.POST.get('question','')
    return question


def process_question():
    question = get_question()
    out = json.loads(question)
    for key in out.keys():
        if key == 'question':
            terminal_output(key)


def terminal_output(questiom):
    blessings.Terminal(question)



if __name__ = '__main__':
    run(host='0.0.0.0', port=5454)
