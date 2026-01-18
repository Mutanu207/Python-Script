## AI Text Generator Python Script 

A simple Python script to interact with a Hugging Face LLM (MiniMax-M2.1) for generating text based on user prompts.  
I genereated the script as i was learning how use hugging face model with the new inference API,after many tries,debugging and code failures i mangaged to get the code running.
Since its a free model i cant use alot of tokens hence there are alot if limitations to it,but when i get more tokens will try it out.

## Features

- Generate AI responses from a prompt
- Configurable model (`MODEL_ID`) and parameters (`max_tokens`, `temperature`)
- Error handling with traceback for debugging
- Runs from the command line

## Requirements

- Python 3.10+
- `huggingface_hub` Python package
- `python-dotenv` for managing API tokens

#New things Added
- i added abstraction to have backup models using litellm
