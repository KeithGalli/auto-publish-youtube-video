import os
from googleapiclient.discovery import build

from authentication import get_credentials
from helpers import get_channel_subscribers, set_video_status
from schedule import update_schedule_expression, turn_off_function

def lambda_handler(event, context):

    credentials = get_credentials()

    CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID")
    VIDEO_ID = os.environ.get("YOUTUBE_VIDEO_ID")

    youtube = build('youtube', 'v3', credentials=credentials, cache_discovery=False)

    subscribers = get_channel_subscribers(youtube, CHANNEL_ID)
    print("subscribers:", subscribers)

    if subscribers >= 1000:
        set_video_status(youtube, VIDEO_ID, "public")
        print("Video Published!")
        turn_off_function()

    update_schedule_expression(subscribers)







