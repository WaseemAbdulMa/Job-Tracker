# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app/

# Step 4: Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y libmysqlclient-dev

# Step 5: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Run migrations (optional: you may want to run this during deployment)
RUN python manage.py migrate

# Step 7: Expose the port that the app will run on (default Django port 8000)
EXPOSE 8000

# Step 8: Define environment variable
ENV PYTHONUNBUFFERED 1

# Step 9: Run the application
CMD ["gunicorn", "Job_Tracker.wsgi:application", "--bind", "0.0.0.0:8000"]
