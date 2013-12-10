__author__ = 'Binnie'

import webapp2
import os
import models
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import mail, users

path = os.path.join(os.path.dirname(__file__), '../templates/email_details.html')


class EmailDetailsHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('Name')
        email = self.request.get('Email')
        telephone = self.request.get('Telephone')
        comment = self.request.get('Comment')

        subject = "Interest in buttons and lace"
        body = """
Name: %s
Email: %s
Telephone: %s
Comment: %s
""" % (name, email, telephone, comment)

        sender_address = "imbchilds@gmail.com"
        user_address = "imbchilds@gmail.com"
        mail.send_mail(sender_address, user_address, subject, body)

        template_values = {'is_admin': users.is_current_user_admin()}
        self.response.out.write(template.render(path, template_values))
