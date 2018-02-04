FROM python:2.7-alpine3.7 AS builder

# Get custom version of django-reversion
COPY django-reversion-1.3.3.zip /django-reversion-1.3.3.zip
RUN pip install /django-reversion-1.3.3.zip

RUN apk add --no-cache build-base git py-mysqldb
RUN git clone https://github.com/dndtools/dndtools.git /dndtools

WORKDIR /dndtools/
ARG revision=master
RUN git checkout --detach $revision
RUN pip install mysql-python
RUN pip install -r requirements.txt

COPY local.py dndtools/dndproject/local.py

FROM python:2.7-alpine3.7

WORKDIR /dndtools/dndtools/
ENTRYPOINT ["/usr/local/bin/python2.7", "manage.py"]
CMD ["runserver"]
EXPOSE 8000

COPY --from=builder /dndtools/ /dndtools/
COPY --from=builder /usr/local/lib/python2.7/site-packages/ /usr/local/lib/python2.7/site-packages/
