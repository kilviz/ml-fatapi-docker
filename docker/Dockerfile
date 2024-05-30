FROM python:3.8.2

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

RUN mkdir -p /src

WORKDIR /src/app

RUN git clone https://github.com/kilviz/ml-fatapi-docker.git /src/app

RUN pip install --upgrade pip

RUN pip install -r /src/app/requirements/test_requirements.txt

RUN chmod +x /src/app/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]