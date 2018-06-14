FROM centos

ADD app.py requirements.txt /app/
RUN yum install -y epel-release && \
    yum install -y python2-pip && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    yum remove -y epel-release && \
    yum clean all && \
    rm -rf /var/cache/yum

CMD PYTHONPATH=/app FLASK_APP=app.py flask run --host=0.0.0.0 --port 8080
