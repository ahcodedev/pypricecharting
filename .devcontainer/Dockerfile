# See here for image contents: https://github.com/devcontainers/images/tree/main/src

# Image version 3.3.2, Python 3.14, Debian bookworm. Tag and digest are updated by Dependabot.
FROM mcr.microsoft.com/vscode/devcontainers/python:3.3.2-3.14-bookworm@sha256:94053b777943a4eda40e83d5386f7c5befb72f5bb778878ac527bb9491adcd42

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Just Installation
COPY --from=ghcr.io/casey/just:1.59.0@sha256:014cbe6e6de678864004e2fd8b0405f77ce43b20b225e816feb330f2fb575c01 /just /usr/local/bin/

# uv Installation
COPY --from=ghcr.io/astral-sh/uv:0.13.7@sha256:96f40d3904aad8d0bd010539001d36c8e2188b981e1334471a90c4a1d93bb490 /uv /uvx /usr/local/bin/

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
