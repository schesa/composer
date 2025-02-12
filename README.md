# 🤖 AISpace

A collection of AI-powered tools and assistants. Currently featuring an interactive programming assistant built with Python and Docker.

## 🌟 Features

- Interactive command-line interface with colored output
- Responses for common programming languages and tools
- Simple and extensible conversation system
- Docker containerization for easy deployment
- Simulated typing for more natural interaction
- Command history tracking
- Clear screen functionality

## 🚀 Quick Start

### Prerequisites

- Docker installed on your system
- Git (for cloning the repository)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/schesa/composer.git
   cd composer
   ```

2. Make the run script executable:
   ```bash
   chmod +x composer/run.sh
   ```

3. Start the chatbot:
   ```bash
   ./composer/run.sh
   ```

## 💬 Usage

Once running, you can interact with the chatbot using these commands:

- Type `help` to see available topics
- Type `clear` to reset the screen
- Type `bye` to exit

Example questions:
- "Tell me about Python"
- "What is Docker?"
- "How does Git work?"
- "Can you help me with JavaScript?"

## 🛠️ Project Structure

```
composer/
├── chatbot.py      # Core chatbot logic
├── main.py         # CLI interface
├── Dockerfile      # Docker configuration
├── requirements.txt # Python dependencies
└── run.sh          # Startup script
```

## 🔧 Customization

You can extend the chatbot's capabilities by modifying the `programming_responses` dictionary in `chatbot.py`. Add new topics and responses in this format:

```python
self.programming_responses = {
    "your_topic": "Your detailed response here!",
}
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python 3.9
- Containerized with Docker
- Inspired by interactive programming assistants

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the existing issues or create a new one
2. Provide detailed information about your environment
3. Include steps to reproduce the problem

---
Made with 🤖