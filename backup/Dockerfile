FROM python:3.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY app.py /app
COPY weights24.h5 /app
CMD ["python", "app.py"]~