__author__ = 'Binnie'

import webapp2
from google.appengine.api import users


class LoginScreenHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.write('Hello, ' + user.nickname() + ' you are an administrator of this website')
            else:
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.write('Hello, ' + user.nickname() + ' you are not an administrator so logging in ' + \
                                    'has had no effect')
        else:
            self.redirect(users.create_login_url(self.request.uri))
