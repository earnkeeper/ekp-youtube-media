from pprint import pprint

from app.features.embeds.embed_tile import embed_tile
from db.game_repo import GameRepo
from db.youtube_repo import YoutubeRepo


class EmbedsService:

    def __init__(
            self,
            youtube_repo: YoutubeRepo,
            game_repo: GameRepo,
    ):
        self.game_repo = game_repo
        self.youtube_repo = youtube_repo

    async def get_embeds(self):
        videos = self.youtube_repo.list_videos_ordered_by_publish_time(100)
        
        games = self.game_repo.find_all()
        
        games_map = {}
        
        for game in games:
            games_map[game['id']] = game
            
        rank = 0
        embeds = []

        for video in videos:
            
            game_id = video["game_id"]
            
            if game_id not in games_map:
                continue
            
            game = games_map[game_id]
            
            if game['disable']:
                continue
            
            rank += 1
            
            video["rank"] = rank
            
            video["game_name"] = game['name']

            if len(video["title"]) > 80:
                video["title"] = video["title"][:78] + "..."


            video["page"] = f'/game/all/info/{video["game_id"]}'

            embed = {
                "id": f'youtube_{rank}',
                "size": 'tile',
                "element": embed_tile(),
                "data": [video],
            }

            embeds.append(embed)
            
            if rank == 10:
                break

        return embeds
