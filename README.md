## Building and Running the Llama-CPP Server Docker Container

### Prerequisites

- Docker installed on your system.
- NVIDIA GPU with CUDA support (if you intend to use GPU acceleration).

### Steps

#### 1. Build the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run:

```bash
docker build -t llava-cpp-server .
```

#### 2. Download Required Model Files

Download the required model and project files from the following Hugging Face repository: [ggml_llava-v1.5-7b](https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main).

Place the downloaded files in your models directory, for example, `/home/random/private/models`.

#### 3. Run the Docker Container

To run the Docker container, use the following command:

```bash
docker run -v "/home/random/private/models:/usr/src/app/models" --network=host -p 8080:8080 llava-cpp-server
```

Replace `"/home/random/private/models"` with the unique path to your models directory.

### GPU Support (Optional)

If you have an NVIDIA GPU and wish to use it, ensure you have the NVIDIA Container Toolkit installed and run the container with the `--gpus all` flag:

```bash
docker run --gpus all -v "/home/random/private/models:/usr/src/app/models" --network=host -p 8080:8080 llava-cpp-server
```

### Cleanup Docker (Optional)

To remove all Docker images and containers to free up storage, follow these steps:

1. **Remove all containers:**

   ```bash
   docker stop $(docker ps -a -q)
   docker rm $(docker ps -a -q)
   ```

2. **Remove all images:**

   ```bash
   docker rmi $(docker images -a -q)
   ```

3. **Remove unused volumes (Optional):**
   ```bash
   docker volume prune
   ```

**Warning:** These commands will permanently delete all Docker containers, images, and volumes. Ensure you have backups of important data.

### Additional Notes

- On Linux, you may need to use `sudo` for Docker commands, or add your user to the `docker` group.
- Ensure that you have no important containers or images before running cleanup commands.
