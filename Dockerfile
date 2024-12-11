
FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --no-cache-dir --upgrade -r requirements.txt

COPY src/ src/

CMD ["/bin/bash"]