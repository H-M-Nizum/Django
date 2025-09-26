// Load express
const express = require("express");
const app = express();
const PORT = 3000;

// Middleware to parse JSON
app.use(express.json());

// Basic route
app.get("/", (req, res) => {
  res.send("Hello, World! 🚀 Node.js is running.");
});

// Example API route
app.get("/api", (req, res) => {
  res.json({ message: "Welcome to my basic Node.js API!" });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
