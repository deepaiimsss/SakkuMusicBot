from SakkuMusic.core.bot import Sakku
from SakkuMusic.core.dir import dirr
from SakkuMusic.core.git import git
from SakkuMusic.core.userbot import Userbot
from SakkuMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sakku()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
