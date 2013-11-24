__author__ = 'Binnie'

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

path = os.path.join(os.path.dirname(__file__), '../templates/investment.html')


class InvestmentScreenHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template.render(path, template_values))