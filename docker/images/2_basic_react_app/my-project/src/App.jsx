import { motion } from "framer-motion";
import "./App.css";

function App() {
  return (
    <section className="relative hero bg-gradient-to-r from-blue-100 via-white to-blue-50 h-screen flex flex-col justify-center items-center text-center overflow-hidden">
      {/* Background Decorative Shapes */}
      <div className="absolute -top-20 -left-20 w-72 h-72 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
      <div className="absolute -bottom-20 -right-20 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>

      {/* Hero Content */}
      <motion.h1
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="text-6xl font-extrabold text-gray-900 mb-4 drop-shadow-lg"
      >
        Welcome to My Website
      </motion.h1>

      <motion.p
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 1 }}
        className="text-xl text-gray-600 mb-6 max-w-xl"
      >
        For Create Docker Image and Container.
      </motion.p>

      <motion.h4
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className="px-8 py-4 bg-blue-600 text-white text-lg font-medium rounded-xl shadow-md hover:bg-blue-700 transition"
      >
        Hosna Mobarak Nizum
      </motion.h4>
    </section>
  );
}

export default App;
