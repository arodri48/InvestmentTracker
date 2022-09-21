FROM python:3.9.12

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["python", "src/execute_tracker.py"]