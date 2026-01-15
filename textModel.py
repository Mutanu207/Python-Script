import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import traceback
load_dotenv()
#creating the handshake between hugging face and my system to be able to use the models and send requests
client=InferenceClient(token=os.getenv("HF_TOKEN"))
MODEL_ID="MiniMaxAI/MiniMax-M2.1"
def generate_text(prompt):#creating a function that when called will execute the code block inside the function
    print("Please wait as we generate the answer...")
    try:
        output= client.chat.completions.create(
                model=MODEL_ID,
                max_tokens=500,
                temperature=0.3,
                messages=[ {"role": "user", "content": prompt}, {"role": "system", "content": "You are a helpful assistant."}])
        return(output.choices[0].message["content"]) #returning the generated text after stripping any leading or trailing whitespace
    except Exception:
        print(f"An error occurred: {traceback.format_exc()}")
        return None
    
if __name__=="__main__": #checks if the current script is being run directly and not being imported as a module,when run
    #directly python sets name="main" so the guarded code runs,when file is imported,the code is not executed 
    if len(sys.argv)<2: #sys.argv lists all words typed in the command line when running the script
        print("Usage: python textModel.py <prompt>")
        sys.exit(1)
    prompt=sys.argv[1] #the first argument after the script name is the prompt
    result=generate_text(prompt) #call the function to generate answer
    if result:
     print("Generated Answer:",result)