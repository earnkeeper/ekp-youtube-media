import logging
import time
from ekp_sdk.db import MgClient


class GameRepo:
    def __init__(
        self,
        mg_client: MgClient
    ):
        self.mg_client = mg_client
        self.collection = self.mg_client.db['master_game_list']
        self.collection.create_index("id", unique=True)
        self.collection.create_index("source")

    def find_all(self):
        start = time.perf_counter()

        results = list(
            self.collection.find()
        )

        logging.info(
            f"⏱  [GameRepo.find_all()] {time.perf_counter() - start:0.3f}s"
        )

        return results

    def update_banner_url(self, game_id, banner_url):
        start = time.perf_counter()

        self.collection.update_one(
            {"id": game_id}, {"$set": {"banner_url": banner_url}})

        logging.info(
            f"⏱  [GameRepo.update_banner_url({game_id})] {time.perf_counter() - start:0.3f}s"
        )

    def update_profile_image_url(self, game_id, profile_image_url):
        start = time.perf_counter()

        self.collection.update_one(
            {"id": game_id}, {"$set": {"profile_image_url": profile_image_url}})

        logging.info(
            f"⏱  [GameRepo.update_profile_image_url({game_id})] {time.perf_counter() - start:0.3f}s"
        )
