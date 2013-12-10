__author__ = 'Binnie'

import webapp2
import os
from models import Album, Image
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import images, users

path = os.path.join(os.path.dirname(__file__), '../templates/album_slideshow.html')


class AlbumSlideshowHandler(webapp2.RequestHandler):
    def get(self):
        album_key = ndb.Key(urlsafe=self.request.get('key'))
        photos = Image.query(ancestor=album_key).fetch()
        blob_keys = []
        for photo in photos:
            blob_keys.append(images.get_serving_url(photo.image_blob))

        template_values = {'is_admin': users.is_current_user_admin(),
                           'album': album_key.get(),
                           'blob_keys': blob_keys,
                           'photos': photos}
        self.response.out.write(template.render(path, template_values))
