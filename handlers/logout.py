__author__ = 'Binnie'

import webapp2
from google.appengine.api import users


class LogoutScreenHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
