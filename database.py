import json
from pathlib import Path


class PetStoreDB:

    def __init__(self, dbfile: str = "database.json"):
        self.file = dbfile
        self.data = self.__load_data(self.file)

    def get_owners(self):
        return self.data['owners']

    def get_pets(self):
        return self.data['pets']

    def get_owner(self, id):
        owners = self.get_owners()
        return owners[id - 1]

    def get_owner_by_name(self, name):
        owners = self.get_owners()
        for owner in owners:
            if owner['name'] == name:
                return owner
        return None

    def get_pet(self, id):
        pets = self.get_pets()
        return pets[id - 1]

    def get_owned_pets(self, owner_id):
        owner = self.get_owner(owner_id)
        pets = self.get_pets()
        pets_ids = owner["pets"]
        return [pets[i] for i in pets_ids]

    def __load_data(self, filepath: str) -> dict:
        with Path(filepath).open(mode='r') as db:
            return json.load(db)
