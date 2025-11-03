FROM python:3.11-slim 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 
WORKDIR /app 
 
RUN apt-get update && apt-get install -y --no-install-recommends \  
    default-libmysqlclient-dev pkg-config \  
    gcc \  
    libc6-dev \  
    && rm -rf /var/lib/apt/lists/* 
 
COPY requirements.txt /app/
RUN pip install --upgrade pip
# Enable caching to reuse downloaded packages if requirements.txt didn’t change
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
COPY . /app/
 
EXPOSE 8000 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  
