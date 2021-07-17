FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

copy ks_api /ks_api

CMD ["uvicorn", "ks_api.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
