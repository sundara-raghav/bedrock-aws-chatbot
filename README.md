# AWS Bedrock Chatbot 🤖

A simple, interactive chatbot powered by AWS Bedrock and Claude 3 Sonnet.

## Features

- 💬 Interactive command-line chat interface
- 🧠 Powered by Claude 3 Sonnet via AWS Bedrock
- 📝 Maintains conversation history
- 🔄 Reset conversation anytime
- 🔒 Secure API key management with environment variables

## Prerequisites

- Python 3.8 or higher
- AWS Bedrock API access
- AWS Bedrock API Key

## Setup

1. **Clone or navigate to this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   
   Your API key is already configured in the `.env` file. If you need to update it:
   ```
   BEDROCK_API_KEY=your_api_key_here
   AWS_REGION=us-east-1
   ```

## Usage

Run the chatbot:
```bash
python chatbot.py
```

### Commands

- Type your message and press Enter to chat with the AI
- Type `reset` to clear the conversation history
- Type `quit`, `exit`, or `bye` to end the conversation
- Press `Ctrl+C` to exit at any time

## Example Conversation

```
You: Hello! What can you help me with?

🤖 Assistant: Hello! I'm an AI assistant powered by AWS Bedrock. I can help you with:
- Answering questions on various topics
- Writing and explaining code
- Creative writing and brainstorming
- Problem-solving and analysis
- And much more!

What would you like to talk about today?

You: Tell me a joke

🤖 Assistant: Why don't scientists trust atoms?

Because they make up everything! 😄
```

## Project Structure

```
bedrock-aws-chatbot/
├── chatbot.py          # Main chatbot application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API key)
└── README.md          # This file
```

## Security Note

⚠️ **Important**: The `.env` file contains your API key. Make sure to:
- Never commit `.env` to version control
- Add `.env` to your `.gitignore` file
- Keep your API key confidential

## Troubleshooting

**Connection Issues:**
- Verify your API key is correct in the `.env` file
- Check your internet connection
- Ensure you have access to AWS Bedrock services

**Module Not Found:**
- Run `pip install -r requirements.txt` to install dependencies

## License

MIT License - Feel free to use and modify as needed!

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.