FROM ubuntu
RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install flask requests pyyaml
COPY ./app /app
WORKDIR /app