FROM python:3.12.0

ENV PYTHONUNBUFFERED=1
WORKDIR /bot

COPY requirements.txt .
RUN pip3 install --upgrade setuptools && \
    pip3 install -r requirements.txt

COPY . .

CMD ["python", "__main__.py"]

