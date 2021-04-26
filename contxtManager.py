from contextlib import contextmanager
from datetime import datetime

@contextmanager

def customLog(*args):
    print ("This is start of context manager!\n")
    try:
        myFile=open(*args)
        myFile.write("################### Start Date: {} ################\n".format(datetime.now()))
        yield myFile

    finally:
        myFile.write("################### End Date: {} ################\n".format(datetime.now()))
        myFile.close()


with customLog('index.txt', 'a') as customfile:
    customfile.write('This is going to fail!\n')
    customfile.write('This is going to fail!\n')
    customfile.write('This is going to fail!\n')
    customfile.write('This is going to fail!\n')
    customfile.write('This is going to fail!\n')


class customLogger(object):
    def __init__(self, file, mode):
        self.mode = mode
        self.file = file

    def __enter__(self):
        self.openfile = open(self.file, self.mode)
        self.openfile.write('############# Start Date: {} ############\n'.format(datetime.now()))
        return self.openfile
    def __exit__(self, *args):
        self.openfile.write('############# End Date: {} ############\n'.format(datetime.now()))
        self.openfile.close()

with customLogger('customloggerfromClass.txt', 'a') as fromclass:
    fromclass.write('This is coming from class!\n')
    fromclass.write('This is coming from class!\n')
    fromclass.write('This is coming from class!\n')
    fromclass.write('This is coming from class!\n')
    fromclass.write('This is coming from class!\n')