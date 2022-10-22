grpc:
	protoc --python_out=. lab6.proto
	python3 -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ lab6.proto

clean:
	rm -rf lab6_pb2.py lab6_pb2_grpc.py