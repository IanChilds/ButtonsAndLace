__author__ = 'Binnie'

import webapp2
import os
from models import Album, Image
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template


class DeleteAlbumsHandler(webapp2.RequestHandler):
    def get(self):
        photos = Image.query().fetch()
        albums = Album.query().fetch()
        for photo in photos:
            photo_key = ndb.Key(urlsafe=photo.ukey())
            photo_key.delete()
        for album in albums:
            album_key = ndb.Key(urlsafe=album.ukey())
            album_key.delete()
        self.redirect('/')