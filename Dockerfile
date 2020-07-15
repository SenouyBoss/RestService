FROM python:3.6.4


COPY . /app
WORKDIR /app
# install requirements
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]

