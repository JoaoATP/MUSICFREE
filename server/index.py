from flask import *
from helpers import *

app = Flask('API-MUSICFREE')

db.connect()
db.create_tables([Music, User, Playlist, PlaylistAddUser, PlaylistAddMusic], safe=True)

@app.route('/api/music', methods=['POST', 'GET'])
def music_route():
    if request.method == 'POST':
        return create_item(Music, request.get_json())
    elif request.method == 'GET':
        return get_all_items(Music)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/music/<int:music_id>', methods=['GET', 'DELETE'])
def music_id_route(music_id):
    if request.method == 'GET':
        return get_item_by_id(Music, music_id)
    elif request.method == 'DELETE':
        return delete_item(Music, music_id)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/user', methods=['POST', 'GET'])
def user_route():
    if request.method == 'POST':
        return create_item(User, request.get_json())
    elif request.method == 'GET':
        return get_all_items(User)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/user/<int:user_id>', methods=['GET', 'DELETE'])
def user_id_route(user_id):
    if request.method == 'GET':
        return get_item_by_id(User, user_id)
    elif request.method == 'DELETE':
        return delete_item(User, user_id)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlists', methods=['POST', 'GET'])
def playlists_route():
    if request.method == 'POST':
        return create_item(Playlist, request.get_json())
    elif request.method == 'GET':
        return get_all_items(Playlist)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlists/<int:playlist_id>', methods=['GET', 'DELETE'])
def playlist_id_route(playlist_id):
    if request.method == 'GET':
        return get_item_by_id(Playlist, playlist_id)
    elif request.method == 'DELETE':
        return delete_item(Playlist, playlist_id)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlistaddusers', methods=['POST', 'GET'])
def playlistaddusers_route():
    if request.method == 'POST':
        return create_item(PlaylistAddUser, request.get_json())
    elif request.method == 'GET':
        return get_all_items(PlaylistAddUser)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlistaddusers/<int:playlistadduser_id>', methods=['GET', 'DELETE'])
def playlistadduser_id_route(playlistadduser_id):
    if request.method == 'GET':
        return get_item_by_id(PlaylistAddUser, playlistadduser_id)
    elif request.method == 'DELETE':
        return delete_item(PlaylistAddUser, playlistadduser_id)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlistaddmusics', methods=['POST', 'GET'])
def playlistaddmusics_route():
    if request.method == 'POST':
        return create_item(PlaylistAddMusic, request.get_json())
    elif request.method == 'GET':
        return get_all_items(PlaylistAddMusic)
    else:
        return jsonify({"error": "Invalid method."}), 404


@app.route('/api/playlistaddmusics/<int:playlistaddmusic_id>', methods=['GET', 'DELETE'])
def playlistaddmusic_id_route(playlistaddmusic_id):
    if request.method == 'GET':
        return get_item_by_id(PlaylistAddMusic, playlistaddmusic_id)
    elif request.method == 'DELETE':
        return delete_item(PlaylistAddMusic, playlistaddmusic_id)
    else:
        return jsonify({"error": "Invalid method."}), 404


if __name__ == '__main__':
    app.run(host='api.localhost', port=8080)