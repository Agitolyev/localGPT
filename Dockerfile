# syntax=docker/dockerfile:1
# Build as `docker build . -t localgpt`, requires BuildKit.
# Run as `docker run -it --mount src="$HOME/.cache",target=/root/.cache,type=bind --gpus=all localgpt`, requires Nvidia container toolkit.

FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y software-properties-common curl
RUN apt-get install -y g++-11 make python3 python-is-python3 pip
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
RUN ln -s ~/.local/share/pypoetry/venv/bin/poetry /usr/local/bin/poetry

ENV WORKDIR=/usr/src/localGPT
WORKDIR $WORKDIR
COPY . .

ARG device_type

# Add "--mount=type=cache,target=/root/.cache" to use BuildKit cache mount to drastically reduce redownloading from pip on repeated builds
# Docker BuildKit does not support GPU during *docker build* time right now, only during *docker run*.
# See <https://github.com/moby/buildkit/issues/1436>.
# If this changes in the future you can `docker build --build-arg device_type=cuda  . -t localgpt` (+GPU argument to be determined).
RUN if [ "$device_type" = "cpu" ]; then \
        CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 poetry install --sync --with torch_cpu; \
        poetry run python ingest.py --device_type cpu; \
    elif [ "$device_type" = "cuda" ]; then \
        CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 poetry install --sync --with torch_cuda; \
        poetry run python ingest.py --device_type cpu; \
    else \
        echo "No valid device type specified"; \
        exit 1; \
    fi

CMD poetry run python run_localGPT.py --device_type $device_type
