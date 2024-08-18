import redis


class RedisService:
    def __init__(self, host='LOCALHOST', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def add_song(self, song):
        self.client.sadd('downloaded_songs', song)

    def is_song_downloaded(self, song):
        return self.client.sismember('downloaded_songs', song)

    def get_all_songs(self):
        return [song.decode('utf-8') for song in self.client.smembers('downloaded_songs')]
