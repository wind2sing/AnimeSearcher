FROM python:3.8
WORKDIR /app
COPY ./ /app
RUN python3.8 -m pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]