# Use an official NVIDIA runtime as a parent image
FROM nvidia/cuda:11.2.2-base-ubuntu20.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Clone the llama.cpp repository
RUN git clone https://github.com/ggerganov/llama.cpp
WORKDIR /usr/src/app/llama.cpp

# Build the llama.cpp with CUDA support
RUN make

# Set environment variables
ENV PATH /usr/src/app/llama.cpp:$PATH

# Create a directory for models
WORKDIR /usr/src/app/models

# Command to run the server
CMD ["../llama.cpp/server", "-m", "llava-ggml-model-q4_k.gguf", "--mmproj", "mmproj-model-f16.gguf", "-ngl", "30", "-c", "2048"]