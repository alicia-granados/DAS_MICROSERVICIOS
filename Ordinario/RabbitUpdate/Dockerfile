FROM python:3.8

COPY . /usr/src/Rabbit
COPY workerUpdate.py /usr/src/Rabbit

WORKDIR /usr/src/Rabbit

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "workerUpdate.py"]