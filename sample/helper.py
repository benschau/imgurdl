from os.path import expanduser
import tarfile

def compress_dir(path, title):
    dir = tarfile.open(path + ".tgz", "w:gz")
    dir.add(path, arcname=title)
    dir.close()

             
