HELP_1 = """<b><u>Admin Commands :</b></u>

Just add <b>c</b> in the streaming of the command to use it for channel.


/pause : Pause the current playing stream.

/resume : Resume the paused stream.

/skip : Skip the current playing music.

/end or /stop : Stop the playing musi.

/player : Get an interactive player pannel.

/queue :Check Queue List of Music..
"""

HELP_2 = """
<b><u>Auth Users :</b></u>

Auth users can use admin commands of bot without admin in the group

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group
/authusers :  Check AUTH LIST of the group
"""

HELP_3 = """
🌐<u><b>BROADCAST FUNCTION</b></u> [Only for Sudoers] :

/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>Options for broadcast :</u>
<b>-pin</b> :  This will pin your messag
<b>-pinloud</b> : This will pin your message with loud notification
<b>-user</b> : This will broadcast your message to the users who have started your bot
<b>-assistant</b> : This will broadcast your message from assistant account of your bot.
<b>-nobot</b> : his will force your bot to not broadcast message

<b>Example:</b> <code>/broadcast -user -assistant -pin Hello Testing</code>
"""

HELP_4 = """<u><b>BLACKLIST CHAT FUNCTION:</b></u> [Only for Sudoers]

Restrict chat to use our bots.

/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat  [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat : Check all blacklisted chats.
"""

HELP_5 = """
<u><b>Block Users:</b></u> [Only for Sudoers]

Starts ignoring the block users and prevent them from using the bot.

/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers : Check blocked Users Lists
"""

HELP_6 = """
<u><b>Channel Play Commands:</b></u>

You can stream audio/video in channel

/cplay : Bot will start playing your given query on voice chat or Stream live links on voice chats in channels.
/cvplay : Bot will start playing your given query on videochat or Stream live links on video chats.
/cplayforce or /cvplayforce : stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.
"""

HELP_7 = """
<u><b>Global Ban Function</b></u> [Only for Sudoers] :

/gban[Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban  [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers : Check Gbanned Users Lists
"""

HELP_8 = """
<b><u>Loop Stream :</b></u>

<b>Starts streamming the ongoing streams on loop</b>

/loop [enable/disable] :  When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.
/loop [1, 2, 3, ...] : Enables loop for given value.
"""

HELP_9 = """
<u><b>Maintenance Mode</b></u> [Only for Sudoers] :

/logs :  Get log of your bot.

/logger [enable / disable] - Bot logs the searched queries in logger group

/maintenance [enable / disable] : Enables or disables the maintenance
"""

HELP_10 = """
<b><uPing and Stats :</b></u>

/start : Starts the bot.
/help : Get help menu with the command details.

/ping : Ping the Bot and check Ram, Cpu etc stats of Bot.

/stats : Check Bots Stats
"""

HELP_11 = """
<u><b>Play Commands:</b></u>

<b>v :</b> Stands for video play.
<b>force :</b> Stands fof force play.

/play ᴏʀ /vplay :Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce ᴏʀ /vplayforce : stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
"""

HELP_12 = """
<b><u>Shuffle and Queue :</b></u>

/shuffle : Randomly shuffles the queued playlist.
/queue : Shows the shuffled queue.
"""

HELP_13 = """
<b><u>Seek Stream:</b></u>

/seek [Duration in seconds] : Forward Seek the music to your duration
/seekback [Duration in seconds] : Backward Seek the music to your duration.
"""

HELP_14 = """
<b><u>Song Download</b></u>

/song [Track Name] or [YT Link]: Download any track from youtube in mp3 or mp4 formats.

/player - Get a interactive Playing Panel.
"""

HELP_15 = """
<b><u>Speed Commands :</b></u>

You can control the playback speed of the stream. [Admins only]

/speed or /playback : For adjusting audio playback in group.
/cspeed or /cplayback : For adjusting audio playback in channel.
"""
