FROM apache/airflow:2.9.2

# Copy your requirements file into the image
COPY requirements.txt /requirements.txt

# Install the python dependencies as the airflow user
RUN pip install --no-cache-dir -r /requirements.txt