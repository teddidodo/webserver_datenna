FROM python:3.10-alpine3.13

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# 

COPY ./word.txt /code/word.txt
COPY ./main.py /code/

EXPOSE 80
# 
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]