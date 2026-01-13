from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from rate_limiter import TokenBucketLimiter

app = FastAPI()

limiter = TokenBucketLimiter(
    capacity=5,
    refill_rate=5 / 60
)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host

    if not limiter.allow_request(client_ip):
        return JSONResponse(
            status_code=429,
            content={"detail": "Too Many Requests"}
        )

    return await call_next(request)

@app.get("/")
def home():
    return {"message": "Request allowed"}
