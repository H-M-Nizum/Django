# Use official node image
FROM node:22-slim

# Set working directory inside container
WORKDIR /app

# Copy the rest of the project
COPY . .

# Install Dependancy(nmp install = npm ci)
RUN npm ci

# Need For Production - build react project
RUN npm run build

# Expose Port
EXPOSE 5173

CMD [ "npm", "run", "dev" ]


#1) Image Create Command >>> docker build -t basic-react-app:v1.0 .
#2) Container Create and Run >>> docker run -p 5173:5173 --name bc-react-c1 basic-react-app:v1.0
#3) Run Existing Container >>> docker start bc-react-c1 and docker stop bc-react-c1