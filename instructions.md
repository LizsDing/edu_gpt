# How to set everything up
## active a vitual env

```
python -m venv .genai_venv
```



## launch jupyter notebook without token or password
```
jupyter notebook --NotebookApp.token=''
```

## make the venv available to your jupyter as a selectable kernel
in jupyter notebook, run
```
!pip install ipykernel
!python -m ipykernel install --name= .genai_venv
```

## launch local web server

```
python -m http.server  
```

## find local jupyter setting to allow access from local web server
- assuming local web server is on 8000 port:
- open C:\Users\neo.zhou\.jupyter\jupyter_notebook_config.py
- find tornado_settings and change that to
```
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' 'http://localhost:8000/' * "
  }
}
```

## add .env file under folder notebooks_for_repl and add the following contents
replace 12345 with your openai api key from azure
```
OPENAI_API_KEY=12345
```