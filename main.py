from google.appengine.ext import blobstore
from google.appengine.api import images

import webapp2
import json

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({ 'status': 'ok' }))

class Image(webapp2.RequestHandler):
    def get(self):
        imageFile = self.request.get('file')
        gskey = blobstore.create_gs_key('/gs/uletit/' + imageFile)
        imageUrl = images.get_serving_url(gskey)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({ 'url': imageUrl }))

app = webapp2.WSGIApplication([('/', Main),
                               ('/image', Image)], debug=True)
