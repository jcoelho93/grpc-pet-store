# Pet store web service with gRPC

## Generate gRPC interfaces

1. Install `grpcio-tools`:
```console
> pip install grpcio-tools
```

2. Use the following command to generate the missing classes:
```console
> mkdir gen
> python3 -m grpc_tools.protoc -I . --python_out=gen --grpc_python_out=gen pets.proto
```

3. Launch the server:
```console
> python3 server.py
```

4. Launch the client:
```console
> python3 client.py
```