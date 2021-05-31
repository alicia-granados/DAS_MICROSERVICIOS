FROM python:3.8

COPY . /usr/src/scrapper
COPY scrapper.py /usr/src/scrapper

WORKDIR /usr/src/scrapper

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "scrapper.py", "--host=0.0.0.0", "--port=5000"]