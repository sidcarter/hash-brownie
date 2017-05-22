FROM python:3.6-alpine
ADD . /www
WORKDIR /www
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
