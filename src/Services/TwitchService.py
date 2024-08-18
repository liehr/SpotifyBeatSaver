import re
from twitchio.ext import commands
from config import TWITCH_ACCESS_TOKEN
from src.Services.BeatSaverService import BeatSaverService
from src.Services.PastebinService import PastebinService
from src.Services.RedisService import RedisService


class TwitchService(commands.Bot):
    def __init__(self, beat_saver_service: BeatSaverService,
                 paste_bin_service: PastebinService, redis_service: RedisService):
        super().__init__(
            token=TWITCH_ACCESS_TOKEN,
            prefix='!',
            nick='YOUR_BOTS_NICK',
            initial_channels=['YOUR_TWITCH_CHANNELS']
        )
        self.beat_saver_service = beat_saver_service
        self.pastebin_service = paste_bin_service
        self.redis_service = redis_service

    async def event_ready(self):
        print(f'Ready | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        print(f'{message.author.name}: {message.content}')

        await self.handle_commands(message)

    @commands.command(name='bs')
    @commands.cooldown(1, 180, commands.Bucket.user)
    async def search_and_download(self, ctx, *, search_query: str):
        if not search_query:
            await ctx.send("Invalid search query format. Use: !bs <artist> - <songname>")
            return

        match = re.match(r'(.+?)\s*-\s*(.+)', search_query)
        if match:
            artist, songname = match.groups()
            search_query = f"{artist} {songname}"

            result = self.beat_saver_service.search_and_download_with_query(search_query)

            if result:
                await ctx.send(f"Downloaded {search_query}")
            else:
                await ctx.send(f"Failed to download {search_query}")

        else:
            await ctx.send("Invalid search query format. Use: !bs <artist> - <songname>"
                           "\nExample: !bs Imagine Dragons - Believer"
                           "\nExample: !bs TheFatRat - Unity"
                           "\nCurrent download status: !status")

    @commands.command(name='status')
    async def status(self, ctx):
        await ctx.send(f"Downloaded songs: \n{await self.create_paste()}")

    async def create_paste(self):
        songs = self.redis_service.get_all_songs()
        song_list = "\n".join(songs)

        paste_url = self.pastebin_service.create_paste("Downloaded Songs", song_list)

        return paste_url

    async def event_command_error(self, context: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.ArgumentParsingFailed):
            await context.send(error.message)

        elif isinstance(error, commands.CommandOnCooldown):
            await context.send(f"Command is on cooldown. Try again in {error.retry_after:.2f} seconds")

        else:
            print(error)
