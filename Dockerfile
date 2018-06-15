FROM centos

ADD app.py requirements.txt /app/
RUN yum install -y epel-release && \
    yum install -y python2-pip && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    yum remove -y epel-release python2-pip && \
    yum clean all && \
    rm -rf /var/cache/yum

CMD PYTHONPATH=/app gunicorn --access-logfile - -w 4 -b 0.0.0.0:8080 app:app
