FROM python:3.7

RUN mkdir /time
WORKDIR /time
ADD . /time/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/time/main.py"]