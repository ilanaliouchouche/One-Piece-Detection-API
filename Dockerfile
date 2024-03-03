FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libgl1-mesa-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app.py /app/app.py
COPY ./templates /app/templates
COPY ./static /app/static

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
