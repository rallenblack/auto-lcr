import urllib2

class ldsSocket():

    def __init__(self):
        self.url = 'https://www.lds.org'
        self.user_agent = 'Mozilla/5.0'

        self.headers = {'User-Agent': self.user_agent}

    def getHomePage(self):
        req = urllib2.Request(self.url, None, self.headers)
        response = urllib2.urlopen(req)
        return response.read()

