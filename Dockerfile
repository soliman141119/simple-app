FROM python:3.11.6-alpine3.17
COPY area-app.py ./
CMD [ "python", "./area-app.py"]
