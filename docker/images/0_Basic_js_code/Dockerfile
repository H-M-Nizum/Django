# Use official Node.js image
FROM node:20

# Set working directory inside container
WORKDIR /usr/src/app

# Copy package files first (for caching npm install)
COPY package*.json ./

# Install dependencies (none in this case, but good practice)
RUN npm install

# Copy the rest of the project
COPY . .

# Run app
CMD ["npm", "start"]
