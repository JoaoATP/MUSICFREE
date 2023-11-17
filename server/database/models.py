from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    class Meta:
        database = db


class Music(BaseModel):
    title = CharField(null=False)
    artist = CharField(null=False)
    duration = IntegerField(null=False)
    audio_data = BlobField(null=False)


class User(BaseModel):
    name = CharField(null=False)
    username = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)
    birthdate = DateField(null=False)
    password = CharField(null=False)
    favourites = TextField(null=True)


class Playlist(BaseModel):
    user = ForeignKeyField(User, backref='playlists')
    name = CharField(null=False)
    stats = BooleanField(default=False)


class PlaylistAddUser(BaseModel):
    user = ForeignKeyField(User)
    playlist = ForeignKeyField(Playlist)


class PlaylistAddMusic(BaseModel):
    playlist = ForeignKeyField(Playlist)
    music = ForeignKeyField(Music)
    user = ForeignKeyField(User)
