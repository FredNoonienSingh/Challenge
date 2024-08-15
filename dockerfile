FROM python:3.12
WORKDIR /

COPY . /
RUN python3.12 -m pip install --upgrade pip
RUN pip3 install -e .
RUN touch database.db
EXPOSE 8080

RUN useradd app

CMD flask run 
