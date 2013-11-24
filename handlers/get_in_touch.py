__author__ = 'Binnie'

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), '../templates/get_in_touch.html')


class GetInTouchScreenHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template.render(path, template_values))