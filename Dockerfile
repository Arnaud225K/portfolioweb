#import python
FROM python:3.7

#specify the buffer to 1 to avoid usage of memoru cach
ENV PYTHONBUFFERD 1

# avoid writing byte code 
ENV PYTHONDONTWRITEBYTECODE 1

# create a repectory
RUN mkdir /app

#our working directory
WORKDIR /app

#copy all our file in/app/
COPY . /app/

#virtual environnmement for the app to separate with the docker conteneur
RUN python -m venv /env

#activate the virtual env : path mean that we will put the activation script  in shell file
ENV PATH="/env/bin/:$PATH"

# our shell file
COPY entrypoint.sh /app/entrypoint.sh

#run python
RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt