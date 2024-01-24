docker build -t llama-cpp-server .

docker run --gpus all -v "/home/random/private/models/:/usr/src/app/models/" --network=host -p 8080:8080 llama-cpp-server
