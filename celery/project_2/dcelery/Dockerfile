# Docker to use the official Python 3.13 Alpine image as the base image.
# “Alpine” is a very lightweight Linux distribution
FROM python:3.13-alpine

# working directory inside the container.
WORKDIR /usr/src/app

# Prevent Python From Writing .pyc files.  This keeps the container clean and lightweight.
ENV PYTHONDONTWRITEBYTECODE=1

# Makes Python output (like print()) appear immediately in the terminal.
# Without this, Python buffers output, and logs might not appear in real time.
# Ensure python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Updates pip (Python’s package installer) to the latest version before installing dependencies.
RUN pip install --upgrade pip

# Copies your local requirements.txt file (from the project folder) into the container.
COPY ./requirements.txt /usr/src/app/requirements.txt

# Installs all Python packages listed in requirements.txt.
RUN pip install -r requirements.txt

# Copies your entrypoint script into the container.
# This script usually handles tasks like waiting for the database or running migrations before starting the app.
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copies the entire project directory (your Django code, etc.) into the container at /usr/src/app/.
COPY . /usr/src/app/


# Sets the entrypoint of the container.
# This means whenever the container starts, it will first execute entrypoint.sh.
# That script usually runs the Django server or any setup commands.
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]