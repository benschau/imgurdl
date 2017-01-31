import pytest
from sample.client import Client

def test_clientinit():
    client = Client()
    
    cpath = expanduser('~/.imgur_cred') 
    imgurcred = [line.rstrip('\n') for line in open(truepath)] 

    assert client.id == imgurcred[0]
    assert client.secret == imgurcred[1]
