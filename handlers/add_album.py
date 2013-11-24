from google.appengine.api.datastore_types import Blob

__author__ = 'Binnie'

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
from models import Album, Image
from google.appengine.api import images

path = os.path.join(os.path.dirname(__file__), '../templates/add_album.html')


class AddAlbumHandler(webapp2.RequestHandler):
    def get(self):
        album, photos = None, None
        try:
            album_key = ndb.Key(urlsafe=self.request.get('key'))
            photos = Image.query(ancestor=album).fetch()
            album = album_key.get()
        except:
            pass

        upload_new_photo_url = blobstore.create_upload_url('/add-photo')
        upload_new_thumbnail_url = blobstore.create_upload_url('/add-thumbnail')

        template_values = {'album': album,
                           'photos': photos,
                           'upload_new_photo_url': upload_new_photo_url,
                           'upload_new_thumbnail_url': upload_new_thumbnail_url}
        self.response.out.write(template.render(path, template_values))

    def post(self):
        try:
            key = ndb.Key(urlsafe=self.request.get('key'))
            album = key.get()
        except:
            album = Album()

        album.populate(name=self.request.get('name'),
                       description=self.request.get('description'))
        album.put()

        self.redirect("/add-album?key=" + album.ukey())

