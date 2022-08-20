FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]