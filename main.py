from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    file_path = "word.txt"
    with open(file_path, "r+") as file:
        word = file.read()
        file.seek(0)  
        file.truncate()
        print(word)
        if word == "" or word == "WORLD":
            word = "HELLO" 
            file.write(word)
        else:
            word = "WORLD"
            file.write(word)

    html_content = f"""
        <html>
        <head>
            <title>Webserver for Datenna</title>
        </head>
        <body>
            <h1>{word}</h1>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
