FROM python:3.6
COPY . /tracker
WORKDIR /tracker
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
