FROM python:3.9-slim

WORKDIR /app

# Copy dependency list and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend ./backend

# Expose backend port
EXPOSE 8000

# Start the FastAPI application via Uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
