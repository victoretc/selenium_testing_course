FROM joyzoursky/python-chromedriver:3.8

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

RUN pip install -r requirements.txt
RUN pytest -s -v auth_test.py 

