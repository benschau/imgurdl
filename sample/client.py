from imgurpython import ImgurClient
from os.path import expanduser

class Client(object):
    
    def __init__(self, path="~/.imgur_cred"):
        truepath = expanduser(path) 
        imgurcred = [line.rstrip('\n') for line in open(truepath)] 
        
        self.id = imgurcred[0]
        self.secret = imgurcred[1]
        # self.client = ImgurClient(self.id, self.secret)
    
