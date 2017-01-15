from imgurpython import ImgurClient
from imgurpython import ImgurClientError

class Client(object):
    
    def __init__(self, path):
        imgurcred = [line.rstrip('\n') for line in open(path)] 
        self.id = imgurcred[0]
        self.secret = imgurcred[1]
        self.client = ImgurClient(self.id, self.secret)
    
                
