FROM ubuntu:latest

WORKDIR /api
COPY . /api/

RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip python3-venv

# Crear un entorno virtual y activar
RUN python3 -m venv /api/venv
ENV VIRTUAL_ENV=/api/venv
ENV PATH="/api/venv/bin:$PATH"

# Configuración de lib para mysqlclient
RUN apt install pkg-config -y  

# Instalar dependencias de mysqlclient
RUN apt install default-libmysqlclient-dev build-essential -y

# Instalar dependencias
RUN pip install mysqlclient==2.2.0
RUN pip install -r requirements.txt


ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV FLASK_RUN_PORT=5000


EXPOSE 5000

CMD /bin/bash -c "flask run --host 0.0.0.0 --port 5000"
