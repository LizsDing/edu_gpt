###################################
# active a vitual env
python -m venv .genai_venv

###################################
# launch local server

python -m http.server  

jupyter notebook --NotebookApp.token=''

###################################
# make a venv available to your jupyterlab
!pip install ipykernel
!python -m ipykernel install --name= .genai_venv


###################################
# in the website, enable GPT
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = "10cc2870a5a04bd6914904c551eeeaf2" #os.getenv('OPENAI_API_KEY')


###################################

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into 3 points.
```{text}```
"""
response = get_completion(prompt)
print(response)