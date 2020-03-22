import grpc
import logging
from concurrent import futures
from database import PetStoreDB
from gen.pets_pb2 import Pet, Owner
from gen.pets_pb2_grpc import PetStoreServicer, add_PetStoreServicer_to_server


class PetsServicer(PetStoreServicer):

    def __init__(self, dbfile: str):
        self.db = PetStoreDB(dbfile)

    def GetPets(self, request, context):
        pets = self.db.get_pets()
        for pet in pets:
            yield Pet(name=pet['name'], species=pet['species'], age=pet['age'])

    def GetOwners(self, request, context):
        owners = self.db.get_owners()
        for owner in owners:
            yield Owner(name=owner['name'])

    def GetOwner(self, request, context):
        owner = self.db.get_owner(request.id)
        return Owner(name=owner['name'])

    def GetOwnedPets(self, request, context):
        owner = self.db.get_owner_by_name(request.name)
        logging.debug(owner)
        pets_ids = owner['pets']
        for pet_id in pets_ids:
            pet = self.db.get_pet(pet_id)
            yield Pet(name=pet['name'], species=pet['species'], age=pet['age'])


def serve(port: int = 3000):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PetStoreServicer_to_server(
        PetsServicer("database.json"), server
    )
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.getLogger().setLevel("DEBUG")
    serve(3000)
