#!/usr/bin/env python3
"""
Simple AWS Bedrock Chatbot
A conversational AI chatbot powered by AWS Bedrock
"""

import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BedrockChatbot:
    def __init__(self):
        """Initialize the Bedrock chatbot"""
        bearer_token = os.getenv('AWS_BEARER_TOKEN_BEDROCK')
        region = os.getenv('AWS_REGION', 'ap-south-1')
        
        if not bearer_token:
            raise ValueError("AWS_BEARER_TOKEN_BEDROCK not found in environment variables")
        
        self.bearer_token = bearer_token
        self.region = region
        
        # Using Claude 3 Haiku as the default model (widely available)
        self.model_id = "anthropic.claude-3-haiku-20240307-v1:0"
        self.conversation_history = []
        
    def chat(self, user_message):
        """Send a message and get a response"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Prepare the request body
            request_body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 2048,
                "messages": self.conversation_history,
                "temperature": 0.7,
                "top_p": 0.9
            }
            
            # Make API request with bearer token
            api_url = f"https://bedrock-runtime.{self.region}.amazonaws.com/model/{self.model_id}/invoke"
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.bearer_token}'
            }
            
            response = requests.post(
                api_url,
                json=request_body,
                headers=headers
            )
            
            if response.status_code != 200:
                return f"Error: API returned status {response.status_code}: {response.text}"
            
            response_body = response.json()
            assistant_message = response_body['content'][0]['text']
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("\n✓ Conversation history cleared!\n")


def main():
    """Main chatbot loop"""
    print("=" * 60)
    print("🤖 AWS Bedrock Chatbot")
    print("=" * 60)
    print("\nCommands:")
    print("  - Type your message and press Enter to chat")
    print("  - Type 'reset' to clear conversation history")
    print("  - Type 'quit' or 'exit' to end the conversation")
    print("\n" + "=" * 60 + "\n")
    
    try:
        chatbot = BedrockChatbot()
        print("✓ Connected to AWS Bedrock successfully!\n")
        
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n👋 Goodbye! Thanks for chatting!\n")
                break
            
            # Check for reset command
            if user_input.lower() == 'reset':
                chatbot.reset_conversation()
                continue
            
            # Skip empty messages
            if not user_input:
                continue
            
            # Get chatbot response
            print("\n🤖 Assistant: ", end="", flush=True)
            response = chatbot.chat(user_input)
            print(response + "\n")
            
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for chatting!\n")
    except Exception as e:
        print(f"\n❌ Error initializing chatbot: {str(e)}\n")
        print("Please check your API key and AWS configuration.\n")


if __name__ == "__main__":
    main()

