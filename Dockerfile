FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app/
RUN python3.8 -m pip install -r requirements.txt

EXPOSE 6001
COPY ./ /app
ENTRYPOINT [ "python", "deploy.py" ]