# FROM nvcr.io/nvidia/cuda:12.0.1-devel-ubuntu22.04
FROM nvcr.io/nvidia/cuda:12.3.1-devel-ubi8


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
RUN make LLAMA_CUBLAS=1

# Set environment variables
ENV PATH /usr/src/app/llama.cpp:$PATH

# Create a directory for models
WORKDIR /usr/src/app/models


RUN nvcc --version
# RUN python3 --version

# # Command to run the server
CMD ["../llama.cpp/server", "-m", "llava-ggml-model-q4_k.gguf", "--mmproj", "mmproj-model-f16.gguf", "-ngl", "30", "-c", "2048"]