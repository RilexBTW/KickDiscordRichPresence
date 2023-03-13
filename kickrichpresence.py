from pypresence import Presence
import time


channel_name = "CHANGE_ME" # kick channel name goes here
client_id = "CHANGE_ME" # discord application ID - Create an app @ https://discord.com/developers/applications/
refresh_time = 120 # how often the rich presence is updated in seconds (make sure to not make it too often, don't mess with this unless you make this script do more than what it already does)


RPC = Presence(client_id)

RPC.connect()



RPC.update(
    state="Streaming on kick.com/"+channel_name,
    large_image="logo",
    buttons=[{"label": "Watch on Kick", "url": "https://www.kick.com/"+channel_name}]
    )

while True:
    time.sleep(refresh_time)















