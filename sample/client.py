from imgurpython import ImgurClient
from os.path import expanduser

class Client(object):
    
    def __init__(self, path="~/.imgur_cred"):
        if not path:
           path = "~/.imgur_cred"
        
        try:
            truepath = expanduser(path) 
            imgurcred = [line.rstrip('\n') for line in open(truepath)] 
        except IOError as error:
            logger.error(error)
            raise 
        
        self.__id = imgurcred[0]
        self.__secret = imgurcred[1]
        self.client = ImgurClient(self.__id, self.__secret)

    def valid_path():
        print("filler")
