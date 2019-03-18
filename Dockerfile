FROM python:3.7-slim

ENV PORT=8080

EXPOSE $PORT
CMD exec gunicorn --bind 0.0.0.0:$PORT -c gunicorn.conf main:app