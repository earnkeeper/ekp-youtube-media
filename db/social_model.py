from typing import TypedDict

class SocialModel(TypedDict):
    id: str
    game_id: str
    timestamp: int
    twitter_followers: int
    telegram_members: int
    discord_members: int
    discord_online: int
