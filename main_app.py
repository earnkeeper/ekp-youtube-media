import logging
from decouple import AutoConfig
from ekp_sdk import BaseContainer
from app.features.embeds.embeds_controller import EmbedsController
from app.features.embeds.embeds_service import EmbedsService

from db.game_repo import GameRepo
from db.youtube_repo import YoutubeRepo


class AppContainer(BaseContainer):
    def __init__(self):
        config = AutoConfig(".env")

        super().__init__(config)

        # DB

        self.game_repo = GameRepo(
            mg_client=self.mg_client
        )        
        
        self.youtube_repo = YoutubeRepo(
            mg_client=self.mg_client
        )

        # FEATURES - EMBEDS

        self.embeds_service = EmbedsService(
            game_repo=self.game_repo,
            youtube_repo=self.youtube_repo
        )

        self.embeds_controller = EmbedsController(
            client_service=self.client_service,
            embeds_service=self.embeds_service,
        )


if __name__ == '__main__':
    container = AppContainer()

    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    container.client_service.add_controller(container.embeds_controller)

    logging.info("🚀 App started")

    container.client_service.listen()
