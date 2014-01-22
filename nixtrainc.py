from __future__ import print_function
import json
import subprocess
import blessings
from bottle import route, run, debug, request, post, get


@post('nixtrain/questions')
def get_question():
    question = request.POST.get('question')
    return question


@get('nixtrain/status')
def client_status():
    """ Here will will return status to server """
    pass
 

def process_command(command):
    ret = subprocess.check_call(command, shell=True)
    if ret:
        return False


def send_question():
    """
        Send a new question
    """
    pass


def process_question():
    out = json.loads(get_question())
    questions = out.keys()
    if 'command' in questions:
            if not process_command(out['command']):
                send_question()

    if 'question' in questions:
            terminal_output(out['question'])


def terminal_output(question):
    blessings.Terminal(question)


if __name__ == '__main__':
    run(host='0.0.0.0', port=5454)
