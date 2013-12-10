__author__ = 'Binnie'

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from models import Thumbnail
from google.appengine.api import images


class AddThumbnailHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        album_key = ndb.Key(urlsafe=self.request.get('key'))
        if album_key is not None:
            previous_thumbnails = Thumbnail.query(ancestor=album_key).fetch()
            for previous_thumbnail in previous_thumbnails:  # should be one of these at most.
                previous_thumbnail_key = ndb.Key(urlsafe=previous_thumbnail.ukey())
                previous_thumbnail_key.delete()
            upload_files = self.get_uploads()  # 'file' is file upload field in the form
            blob_info = upload_files[0]
            thumbnail = Thumbnail(parent=album_key, image_blob=blob_info.key())
            thumbnail.populate(serving_url=images.get_serving_url(blob_info.key()))
            thumbnail.put()

            album = album_key.get()
            album.thumbnail_serving_url = thumbnail.serving_url
            album.put()

            album_key = ndb.Key(urlsafe=self.request.get('key'))  # No idea why I have to add this line in again
            self.redirect('/add-album?key=%s' % album_key.urlsafe())

        else:
            #raise some error here.
            self.redirect('/')