import urllib
import urllib2
import re

class Player:
	
    def __init__(self, baseUrl, name):
        self.baseURL = baseUrl
        real_name = name.split( )[0].lower() + '_' + name.split( )[1].lower()
        self.name = real_name
		

    def getPage(self):
    	try:
    		url = self.baseURL + self.name + '/'
    		request = urllib2.Request(url)
    		response = urllib2.urlopen(request)
    		print response.read()
    		return response
    	except urllib2.URLError, e:
    		if hasattr(e,"reason"):
    		    print u"fail:", e.reason
    		    return None
    
   

baseURL = 'http://www.nba.com/playerfile/'
name = raw_input('Enter player\'s name:')
player = Player(baseURL, name)
player.getPage()
