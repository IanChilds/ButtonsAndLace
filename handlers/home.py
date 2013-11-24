__author__ = 'Binnie'

import webapp2
import os
import models
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), '../templates/home.html')


class HomeScreenHandler(webapp2.RequestHandler):
    def get(self):
        problems_query = models.Album.gql('ORDER BY name')

        template_values = {'albums': problems_query}
        self.response.out.write(template.render(path, template_values))