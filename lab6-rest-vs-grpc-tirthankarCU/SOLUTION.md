# Curl Commands
curl -v http://localhost:5000/api/add/13/12

curl -v -d '{ "a" : [2,1], "b" : [1,1]}' -H 'Content-Type: application/json' http://127.0.0.1:5000/api/dotproduct

curl -v --data-binary @Flatirons_Winter_Sunrise_edit_2.jpg -H 'Content-Type: image/jpg' http://localhost:5000/api/rawimage

# Rest Commands
python rest-server.py

python rest-client.py localhost rawImage 100

python rest-client.py localhost add 100

python rest-client.py localhost dotProduct 100

python rest-client.py localhost jsonImage 100

# GRPC Commands
python grpc-server.py

python grpc-client.py localhost rawImage 100

python grpc-client.py localhost add 100

python grpc-client.py localhost dotProduct 100

python grpc-client.py localhost jsonImage 100

|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	|   	|   	|  	|
|   gRPC add	|   	|   	|    	|
|   REST rawimg	|   	|   	|   	|
|   gRPC rawimg	|       |   	|   	|
|   REST dotproduct	|   	|   	|  	|
|   gRPC dotproduct	|   	|   	|    	|
|   REST jsonimg	|   	|   	|   	|
|   gRPC jsonimg	|       |   	|   	|
|   PING        |       |      |       |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.