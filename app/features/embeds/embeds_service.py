from pprint import pprint

from app.features.embeds.embed_tile import embed_tile
from db.youtube_repo import YoutubeRepo


class EmbedsService:

    def __init__(
            self,
            youtube_repo: YoutubeRepo,
    ):
        self.youtube_repo = youtube_repo

    async def get_embeds(self):
        videos = self.youtube_repo.list_videos_ordered_by_publish_time()

        rank = 0
        embeds = []

        for video in videos:
            rank += 1

            video["rank"] = rank

            video["page"] = f'/game/all/info/{video["game_id"]}'

            embed = {
                "id": f'youtube_{rank}',
                "size": 'tile',
                "element": embed_tile(),
                "data": [video],
            }

            embeds.append(embed)

        return embeds
