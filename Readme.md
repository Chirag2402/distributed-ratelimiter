# Distributed Rate Limiter using FastAPI

## Overview
This project implements a **distributed rate limiter** using **FastAPI** and **Redis**.
The rate limiter works correctly even when multiple FastAPI instances are running
---
## Distributed Rate Limiting
This project uses **Redis as a shared data store**, ensuring that rate limits
are enforced consistently across all FastAPI instances.

---

## Rate Limiting Algorithm

### Token Bucket Algorithm
- Each client has a bucket containing a fixed number of tokens.
- Tokens refill gradually over time.
- Each request consumes one token.
- If no tokens are available, the request is rejected with HTTP `429`.

---

## Technology Stack
- Python 3.11
- FastAPI
- Redis (running via Docker)
- Uvicorn

---

## Project Structure
distributor
├── main.py
├── rate_limiter.py
└── .venv/

---

## How It Works
1. A FastAPI middleware intercepts every incoming request.
2. The client IP address is used as the rate-limit key.
3. Token bucket state (token count and last refill time) is stored in Redis.
4. If tokens are available, the request is allowed.
5. If tokens are exhausted, the server returns HTTP `429 Too Many Requests`.

---

# Running with Docker Compose (Recommended)

Start Redis and FastAPI together:

```bash
docker-compose up --build
```
## Running Redis for local (seperate redis run)
Redis is started using Docker:

```bash
docker run -d -p 6379:6379 --name redis-server redis
```

## Running the Application(sepearte api run)
```
python -m uvicorn main:app --reload
```



## Access the API at:
```
http://127.0.0.1:8000
```
