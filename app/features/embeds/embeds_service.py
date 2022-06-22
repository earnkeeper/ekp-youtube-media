from datetime import datetime

from app.features.embeds.embed_tile import embed_tile
from app.utils.proxy_image import proxy_image
from db.game_repo import GameRepo
from db.social_repo import SocialRepo


class EmbedsService:

    def __init__(
        self,
        game_repo: GameRepo,
        social_repo: SocialRepo,
    ):
        self.game_repo = game_repo
        self.social_repo = social_repo

    async def get_embeds(self):

        social_documents = await self.__get_social_documents()

        if not len(social_documents):
            return []

        filtered_documents = filter(
            lambda x: ('change_24h' in x) and (x['change_24h'] is not None),
            social_documents
        )

        sorted_documents = sorted(
            filtered_documents,
            key=lambda x: x['change_24h'],
            reverse=True
        )

        top10_documents = []

        if len(sorted_documents) < 10:
            top10_documents = sorted_documents
        else:
            top10_documents = sorted_documents[0:10]

        embeds = []

        rank = 0

        for document in top10_documents:
            rank += 1

            document["rank"] = rank

            document["page"] = f'/game/all/info/{document["id"]}'

            embed = {
                "id": f'social_{rank}',
                "size": 'tile',
                "element": embed_tile(),
                "data": [document],
            }

            embeds.append(embed)

        return embeds

    async def __get_social_documents(self):
        games = self.game_repo.find_all()

        games_map = {}

        for game in games:
            if not game["disable"]:
                games_map[game["id"]] = game

        records = self.social_repo.group_by_game_id_and_date()

        records.sort(key=lambda record: record["_id"]["date_timestamp"])

        now = datetime.now().timestamp()

        documents_map = {}

        last_records = {}

        for record in records:
            if record["value"] is None:
                continue

            game_id = record["_id"]["game_id"]

            if game_id not in games_map:
                continue

            game = games_map[game_id]

            date_timestamp = record["_id"]["date_timestamp"]

            if game_id not in documents_map:
                documents_map[game_id] = self.__create_document(
                    game,
                    now
                )

            document = documents_map[game_id]

            document["twitter_followers"] = record["value"]

            if game_id in last_records:
                last_record = last_records[game_id]
                
                document["change_24h"] = record["value"] - last_record["value"]
                
                if (last_record["value"]):
                    document["change_24h_pc"] = (
                        record["value"] - last_record["value"]) / last_record["value"]

                document["chart"].append({
                    "timestamp_ms": date_timestamp * 1000,
                    "value": document["change_24h"]
                })

                document["twitter_plus"] = False

                if document["change_24h"] > 0:
                    document["change_24h_color"] = "success"
                    document["twitter_plus"] = True
                if document["change_24h"] < 0:
                    document["change_24h_color"] = "danger"

            last_records[game_id] = record

        return list(documents_map.values())

    def __create_document(self, game, now):
        document = {
            "id": game["id"],
            "updated": now,
            "game_name": game['name'],
            "twitter_followers": None,
            "chart": [],
            "banner_url": proxy_image(game.get('banner_url', None)),
            "change_24h": 0,
            "change_24h_pc": 0,
            "change_24h_color": "normal",
            "twitter_plus": False,
        }

        return document
