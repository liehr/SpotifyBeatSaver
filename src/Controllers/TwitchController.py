from src.Services.TwitchService import TwitchService


class TwitchController:
    def __init__(self, twitch_service: TwitchService):
        self.twitch_service = twitch_service

    def run(self):
        self.twitch_service.run()
