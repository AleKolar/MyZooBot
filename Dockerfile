FROM python:3.12.0
ENV PYTHONUNBUFFERED=1
WORkDIR = bot
FROM openjdk:17-alpine
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "__main__.py"]

