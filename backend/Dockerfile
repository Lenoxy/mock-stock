FROM python:3.9.1

WORKDIR /python-flask

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 5000

CMD [ "python", "src/app.py"]
