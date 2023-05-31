#we need two files configuration file and py file which will be rendering a content to a particular path which will betold by configuration file which here is test.py#
import webapp2   #servering content to a particular request webapp2 is imported because whatever the request is going to come from browser so what content is to be send how it is send is decided by the webapp2#
class MainPage(webapp2.RequestHandler):   #class which server the data inherting handeler from webapp2 in this class#
	def get(self):   # get method is defined comes to main pg then what response is to back is hello world#
		self.response.write("Hello World!")

app=webapp2.WSGIApplication([('/', MainPage)], debug=True)   #we create application where the WSGI Server which will route that request to this particular application it receives the argumnets as folows which class it is going to send the data and the next argument ids debug = true so it tell us what mistakes we have made will help to get app running#