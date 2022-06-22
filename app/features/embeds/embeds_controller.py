from ekp_sdk.services import ClientService

from app.features.embeds.embeds_service import EmbedsService

class EmbedsController:
    def __init__(
        self,
        client_service: ClientService,
        embeds_service: EmbedsService,
    ):
        self.client_service = client_service
        self.embeds_service = embeds_service
        
    async def on_connect(self, sid):
        pass
    
    async def on_client_state_changed(self, sid, event):
        
        embeds = await self.embeds_service.get_embeds()
        
        await self.client_service.emit_documents(
            sid,
            "embeds",
            embeds
        )
        

        