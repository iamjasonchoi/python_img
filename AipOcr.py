from aip import AipOcr
from file import makidir
imgfile = makidir()

APP_ID = '10154059'
API_KEY = 'EdAOqHFAbhxS1BFC7cdmpA1V'
SECRET_KEY = 'uQg7HlZCYFsLCSbXZQq3LGhuqSViTtxG'

class aip(object):
    def __init__(self):
        super().__init__()

    def getAipocr(self):
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        return aipOcr

    def aipOcrGeneral(self, filepath):
        result = self.getAipocr().basicGeneral(imgfile.get_file_content(filepath))
        return result
