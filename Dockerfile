from alpine:latest

RUN apk add --no-cache python3-dev\ && apk add py3-pip\
	&& python3 -m pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
