FROM python:3.8.10-slim
COPY . ./prediction_app
WORKDIR /prediction_app
RUN pip install -r requirements.txt
EXPOSE 5000
VOLUME /prediction_app/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
