from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

"""
The API loads the HTML page
Objective: 
Every time the page is visited, or reloaded, the function will read the file word.txt (by default with only one word HELLO)
The function will then replace the current word in the .txt, for instance from HELLO to WORLD
Finally, it prints the word in HTML 
"""
@app.get("/", response_class=HTMLResponse)
def read_root():

    file_path = "word.txt"
    with open(file_path, "r+") as file:
        word = file.read()
        file.seek(0)  
        file.truncate()
        if word == "" or word == "WORLD":
            word = "HELLO" 
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
