def get_channel_subscribers(youtube, channel_id):
    request = youtube.channels().list(
        part="statistics", id=f"{channel_id}"
    )
    response = request.execute()
    subscriber_count = int(response['items'][0]['statistics']['subscriberCount'])
    return subscriber_count

def set_video_status(youtube, video_id, status="unlisted"):
    request = youtube.videos().update(
        part="status",
        body={"id": video_id, "status": {"privacyStatus": status}}
    )
    response = request.execute()
    return response