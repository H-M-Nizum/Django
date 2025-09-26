# Use official node image
FROM node:20

# Set working directory inside container
WORKDIR /app

# Copy package files first (for caching npm install)
COPY package*.json ./

# Install Dependancy
RUN npm install

# Expose Port
EXPOSE 3000

# Copy the rest of the project
COPY . .

# Run app
CMD [ "npm", "start" ]