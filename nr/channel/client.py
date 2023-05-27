from ..configs.config import settings
from .message import Message

import requests


class ChannelOpenApiClient():
    def __init__(self):
        self._headers = {
            "x-access-key": settings.channel_open_api_access_key,
            "x-access-secret": settings.channel_open_api_access_secret
        }
        self._url = settings.channel_open_api_base_url
        self._version = settings.channel_open_api_version
        self._group_id = settings.channel_group_id

    def send_teamchat_message(self, message: Message):
        url = f"{self._url}/open/{self._version}/groups/{self._group_id}/messages?botName=NewReleases.io"
        requests.post(
            url=url,
            headers=self._headers,
            json=message.to_dict()
        )
