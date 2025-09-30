# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy Requirements.txt
COPY requirements.txt .

# Install requirements.txt
RUN pip install -r requirements.txt

# copy source code
COPY app.py .

# run source code
CMD [ "python3", "app.py" ]


#1) Build Image >>> docker build -t basic-flask-app:v1.0 .
#2) Container Create and Run >>> docker run -p 5000:5000 --name bc-flask-c1 basic-flask-app:v1.0
#3) Run Existing Container >>> docker start bc-react-c1 and docker stop bc-react-c1