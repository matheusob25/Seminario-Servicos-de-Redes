FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall --yes Werkzeug
RUN pip install --force-reinstall Werkzeug>=2.0
RUN pip install --upgrade Flask
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]

# sudo docker build -t service_web -f service_web.dockerfile .
