FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt schema.sql init_db.py ./
RUN pip install -r requirements.txt
RUN python init_db.py

COPY . .
ENTRYPOINT [ "python", "app.py" ]
