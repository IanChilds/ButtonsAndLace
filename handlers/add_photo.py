__author__ = 'Binnie'

import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from models import Album, Image
from google.appengine.api import images


class AddPhotoHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        album_key = ndb.Key(urlsafe=self.request.get('key'))
        upload_files = self.get_uploads()  # 'file' is file upload field in the form
        blob_info = upload_files[0]
        photo = Image(parent=album_key, image_blob=blob_info.key(), index=1)
        photo.populate(serving_url=images.get_serving_url(blob_info.key()))
        photo.put()

        self.redirect('/add-album?key=%s' % album_key.urlsafe())