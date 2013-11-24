__author__ = 'Binnie'

from google.appengine.ext import ndb

# I think these models are pretty much right now.
#
# The tree structure goes like this;
# Album <- Image
# This allows for a lot of flexibility and fast querying


class Album(ndb.Model):
    def ukey(self):                         # To get urlsafe key easily in templates
        return self.key.urlsafe()
    name = ndb.StringProperty()           # Album name
    description = ndb.TextProperty()      # Any text to accompany the album
    start_date = ndb.DateTimeProperty()   # When the photos were taken. This will be used to sort the albums.
    end_date = ndb.DateTimeProperty()     # If the photos were taken over a longer period of time, this might be useful.


class Image(ndb.Model):
    image_blob = ndb.BlobKeyProperty() # or maybe ndb.BlobReferenceProperty, or blobstore.BlobReferenceProperty?
    caption = ndb.TextProperty()
    serving_url = ndb.StringProperty()
    index = ndb.IntegerProperty()
    def ukey(self):                         # To get urlsafe key easily in templates
        return self.key.urlsafe()


class Thumbnail(ndb.Model):
    image_blob = ndb.BlobKeyProperty() # or maybe ndb.BlobReferenceProperty, or blobstore.BlobReferenceProperty?
    serving_url = ndb.StringProperty()
    def ukey(self):                         # To get urlsafe key easily in templates
        return self.key.urlsafe()



