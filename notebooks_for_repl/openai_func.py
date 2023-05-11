import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')
openai.api_type = "azure"
openai.api_base = "https://atl-neo-openai-1.openai.azure.com/"
openai.api_version = "2022-12-01"

def hello_gpt(prompt, engine="gpt-35-turbo", temperature=0, max_tokens=1000, return_raw=False):
    response = openai.Completion.create(
        engine=engine,
        prompt = prompt,
        temperature=temperature, # degree of randomness
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
        )
    if return_raw:
        return response
    return response.choices[0].text


import ipywidgets as widgets
from IPython.display import display

# Define the callback function
def on_dropdown_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print(f"Selected option: {change['new']}")

# Define the dropdown widget
options = ['Option 1', 'Option 2', 'Option 3']
dropdown = widgets.Dropdown(options=options)

# Add the callback function to the dropdown widget
dropdown.observe(on_dropdown_change)

# Display the dropdown widget
display(dropdown)