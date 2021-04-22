FROM python
COPY chatbot.py ./
COPY requirements.txt ./
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN=1663811015:AAFh1HmZ04FAXQznTj8A8kF1MwbIaKCck9I
ENV HOST=redis-11288.c93.us-east-1-3.ec2.cloud.redislabs.com
ENV PASSWORD=Cq40u0ENJAlfOFzJZnybGc1DelwXq8tB
ENV REDISPORT=11288
CMD python chatbot.py
