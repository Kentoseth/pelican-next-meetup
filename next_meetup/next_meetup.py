"""Pelican plugin to get info on your next meetup."""
import requests
import json
from pelican import signals


def get_next_meetup(generator, metadata):
    """Fetch information about next meetup as per MEETUP_URL variable."""
    if 'MEETUP_URL' in generator.settings.keys():
        URL = "https://api.meetup.com/2/events"
        payload = {
            "sign": True,
            "photo-host": "public",
            "group_urlname": generator.settings['MEETUP_URL'],
            "page": 1  # retrieve only the next event
        }
        response = requests.get(URL, params=payload)
        if response.raise_for_status() == None:
            data = response.json()["results"][0]
            generator.context["next_meetup"] = {
                "name": data["name"],
                "url": data["event_url"],
                "time": data["time"],
                "utc_offset": data["utc_offset"]
            }


def register():
    """Register with Pelican."""
    signals.page_generator_context.connect(get_next_meetup)
