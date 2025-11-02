CREATE DATABASE IF NOT EXISTS portfolio_db;
USE portfolio_db;

CREATE TABLE projects (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100),
  description TEXT,
  tech_stack VARCHAR(255),
  github_link VARCHAR(255)
);

INSERT INTO projects (title, description, tech_stack, github_link) VALUES
('Text-to-Speech Converter', 'A web app that converts written text into speech using HTML, CSS, and JS.', 'HTML, CSS, JavaScript', 'https://github.com/ravi/text-to-speech-converter'),
('WhatsApp Chat Analyzer', 'Python-based tool that analyzes WhatsApp chats for insights and user activity.', 'Python, Pandas, Matplotlib', 'https://github.com/ravi/whatsapp-chat-analyzer'),
('Car Rental System', 'Java-based project for booking and managing car rentals efficiently.', 'Java, MySQL', 'https://github.com/ravi/car-rental-system'),
('AI Portfolio', 'An AI-driven interactive portfolio that responds to user queries using Flask and MySQL.', 'Flask, MySQL, HTML, CSS, JavaScript', 'https://github.com/ravi/ai-portfolio');
