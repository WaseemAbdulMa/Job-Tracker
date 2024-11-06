# Step 1: Use Python image as base
FROM python:3.9.13

# Step 2: Set the working directory inside the container (set it to the project folder where manage.py is located)
WORKDIR /app/Job_Tracker

# Step 3: Copy requirements.txt into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the entire project into the container
COPY . .

# Step 5: Set the environment variable for Django (production environment)
ENV PYTHONUNBUFFERED=1

# Step 6: Run migrations (optional: you may want to run this during deployment)
RUN python manage.py migrate

# Step 7: Expose the port that the app will run on (default Django port 8000)
EXPOSE 8000

# Step 8: Set the default command to run the application using gunicorn
CMD ["gunicorn", "Job_Tracker.wsgi:application", "--bind", "0.0.0.0:8000"]
