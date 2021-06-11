FROM python:3.8

COPY . /usr/src/Rabbit
COPY worker.py /usr/src/Rabbit

WORKDIR /usr/src/Rabbit

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "worker.py"]