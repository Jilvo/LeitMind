# Start the microservices
# This command builds and starts all the services defined in the docker-compose.yml file.
docker-up:
    sudo docker-compose up --build

# Stop the microservices
# This command stops all the running services and removes orphan containers.
docker-down:
    docker-compose down --remove-orphans

# Recreate the microservices
# This command stops and then starts all the services, effectively recreating them.
docker-recreate:
    just docker-down && just docker-up

# Builds the Docker image for the stockage service.
# This command navigates to the stockage_service directory, builds the Docker image, and then returns to the previous directory.
docker-build-stockage-service:
    cd stockage_service && docker build -t stockage_service . && cd ..

# Builds the Docker image for the generation service.
# This command navigates to the generation_service directory, builds the Docker image, and then returns to the previous directory.
docker-build-generation-service:
    cd generation_service && docker build -t generation_service . && cd ..

# Builds the Docker image for the Vue.js front-end service.
# This command navigates to the front_service directory, builds the Docker image, and then returns to the previous directory.
docker-build-vue-front-service:
    cd front_service/ && docker build -t vue_front_service . && cd ..

# Builds all Docker images for the services.
# This command sequentially builds the Docker images for the stockage and generation services.
build-all:
    just docker-build-stockage-service
    just docker-build-generation-service

# Builds all Docker images and starts the microservices.
# This command builds all the Docker images and then starts all the services.
build-and-run:
    just build-all
    just docker-up

# Merges changes from the main branch.
# This command fetches the latest changes from the main branch and merges them into the current branch.
merge-from-main:
    git fetch origin main && git merge origin/main

# Updates the documentation for the stockage service.
# This command generates the documentation, exports the requirements, cleans the previous build, and builds the new documentation.
uptdoc-stockage-service:
    cd stockage_service && python generate_docs.py && poetry export -f requirements.txt --output requirements.txt --without-hashes && cd stockage_service/docs && make clean && make html

# Commits and pushes changes with a lazy commit message.
# This command stages all changes, commits them with a provided message, and pushes to the remote repository.
lazycommit commit_message:
    git add . && git commit -m "{{commit_message}}" && git push

# Initializes the project.
# This command runs the install script to set up the project.
init-project:
    ./scripts/install.sh

# Shows the open ports.
# This command lists all the open ports that are currently listening.
show-port:
    netstat -tuln | grep LISTEN

# Lists the processes using a specific port.
# This command shows the processes using the specified port.
lsof PORT:
    sudo lsof -i :{{PORT}}

# Kills the process using a specific port.
# This command terminates the process using the specified port.
kill-port PORT:
    sudo kill -9 $(sudo lsof -t -i:{{PORT}})

pre-commit:
    poetry run pre-commit run --all-files

venv:
    poetry shell
