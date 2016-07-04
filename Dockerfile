FROM hypriot/rpi-alpine-scratch:edge
MAINTAINER feelingfree-me <feelingfree.co.nr@gmail.com>
RUN apk --update add python3 tzdata && \
    pip3 install requests --no-cache-dir && \
    cp /usr/share/zoneinfo/Asia/Bangkok /etc/localtime && \
    mkdir -p /app && \
    rm -rf /var/cache/apk/* 

COPY update.py /app/update.py 
WORKDIR /app

CMD [ "python3", "-u", "./update.py" ]