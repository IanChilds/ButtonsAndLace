__author__ = 'Binnie'

import webapp2
import os
from models import Image, Thumbnail
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import images, users

path = os.path.join(os.path.dirname(__file__), '../templates/album_page.html')


class AlbumPageHandler(webapp2.RequestHandler):
    def get(self):
        album_key = ndb.Key(urlsafe=self.request.get('key'))
        photos = Image.query(ancestor=album_key).fetch()
        thumbnails = Thumbnail.query(ancestor=album_key).fetch()
        thumbnail = thumbnails[0] if len(thumbnails) > 0 else None

        template_values = {'album': album_key.get(),
                           'photos': photos,
                           'thumbnail': thumbnail,
                           'is_admin': users.is_current_user_admin()}
        self.response.out.write(template.render(path, template_values))
