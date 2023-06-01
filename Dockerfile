FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update

# RUN apt install -y libgl1-mesa-glx
# RUN pip install boto3 tensorflow Flask==2.2.2 requests==2.28.1 gunicorn opencv-python
RUN pip install boto3 Flask==2.2.2 gunicorn
COPY . /home/app

CMD flask run -p $PORT -h 0.0.0.0