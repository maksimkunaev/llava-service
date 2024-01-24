

```docker build -t llama-cpp-server .```

```docker run -v "<unique-path-to-your-models>:/usr/src/app/models/" --network=host -p 8080:8080 llama-cpp-server```

```docker run --gpus all -v "/home/random/models/:/usr/src/app/models/" --network=host -p 8080:8080 llama-cpp-server
```

To remove all Docker images and containers to free up storage, you can follow these steps:

1. Remove all containers: Run the following command to stop and remove all containers:

   ```
   docker stop $(docker ps -a -q)
   docker rm $(docker ps -a -q)
   ```

2. Remove all images: Execute the following command to delete all images:

   ```
   docker rmi $(docker images -a -q)
   ```

3. (Optional) Remove unused volumes: If you want to remove unused volumes as well (which can also occupy storage), run the following command:
   ```
   docker volume prune
   ```

Note: Be cautious while executing these commands as they will permanently delete all Docker containers, images, and volumes.

If you are running Docker on Linux, ensure that you have the necessary privileges to run Docker commands. You may need to use `sudo` before the commands, or add your user to the `docker` group.

Make sure you have no important containers or images that you wish to keep before running these commands.
