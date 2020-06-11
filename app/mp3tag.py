import os
import eyed3
import urllib.request
from app.words import remove_words


class MP3File:
    filename = ''
    meta = {}

    def __init__(self, filename):
        if filename[-4:] != '.mp3':
            raise ValueError('file must be of type mp3')

        self.audio = eyed3.load(filename)
        self.filename = filename

    def load_meta(self, cover_url):

        urllib.request.urlretrieve(cover_url, 'cover.jpg')
        cover = open('cover.jpg', 'rb').read()

        self.meta = {
            'artist': self.filename.split('-')[0].lstrip(),
            'title': self.clear_title(self.filename.split('-', 1)[1].lstrip()),
            'cover': cover
        }

    def save(self):
        self.audio.tag.artist = self.meta['artist']
        self.audio.tag.title = self.meta['title']
        self.audio.tag.images.set(3, self.meta['cover'], 'image/jpeg')

        os.remove('cover.jpg')
        self.audio.tag.save()

    @staticmethod
    def clear_title(title):
        words = remove_words()
        for word in words:
            title = title.replace(word, '')

        return title
