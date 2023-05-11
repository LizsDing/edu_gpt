import ipywidgets as widgets
from IPython.display import display

# Define the callback function
def on_dropdown_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print(f"Selected option: {change['new']}")

# Define the dropdown widget
def set_gpt_role(options=['brief', 'detailed']):

    options = ['Option 1', 'Option 2', 'Option 3']
    dropdown = widgets.Dropdown(options=options)

    # Add the callback function to the dropdown widget
    dropdown.observe(on_dropdown_change)

    # Display the dropdown widget
    display(dropdown)
    return dropdown.value