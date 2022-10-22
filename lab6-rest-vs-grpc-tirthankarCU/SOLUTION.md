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

# Python Update in VM and git pull 
sudo add-apt-repository universe

sudo apt update

sudo apt install python3-pip

pip3 install Flask

pip3 install jsonpickle

pip3 install pillow

pip3 install numpy

git clone https://github.com/tirthankar95/lab6CSCI_5253.git

|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|-----------|-----------|---------------|-----------------------|
|   REST add	|   2.55	|   3.25	|  	   |
|   gRPC add	|   0.75	|   	|    	|
|   REST rawimg	|   4.77	|   33.16	|   	|
|   gRPC rawimg	|   10.66    |   	|   	|
|   REST dotproduct	|   3.23	|   4.15	|  	|
|   gRPC dotproduct	|   0.81	|   	|    	|
|   REST jsonimg	|  78.01 	|   98.17	|   	|
|   gRPC jsonimg	|  24.91     |   	|   	|
|   PING        |   0.042    |      |       |
| | | | |


You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.