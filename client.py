import grpc
from gen.pets_pb2 import Void
from gen.pets_pb2_grpc import PetStoreStub


def connect_channel(host: str, port: int):
    return grpc.insecure_channel(f"{host}:{port}")


if __name__ == '__main__':
    channel = connect_channel("localhost", 3000)
    stub = PetStoreStub(channel)

    owners = list(stub.GetOwners(Void()))
    print("OWNERS")
    print(owners)

    pets = list(stub.GetPets(Void()))
    print("PETS")
    print(pets)

    owner = owners[1]
    print(f"Pets of {owner.name}")
    for pet in stub.GetOwnedPets(owner):
        print(pet)
