FROM hypriot/rpi-alpine-scratch:edge
MAINTAINER feelingfree-me <feelingfree.co.nr@gmail.com>
RUN apk --update add python3 && \
    pip3 install requests --no-cache-dir && \
    mkdir -p /app && \
    rm -rf /var/cache/apk/* 

COPY update.py /app/update.py 
WORKDIR /app

ENV username=username
ENV password=password
ENV hostname=name.ddns.com
ENV delay=15

CMD [ "python3", "./update.py" ]