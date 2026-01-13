import time
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

class TokenBucketLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate

    def allow_request(self, key: str) -> bool:
        now = time.time()
        redis_key = f"tb:{key}"

        data = redis_client.hgetall(redis_key)

        tokens = float(data.get("tokens", self.capacity))
        last_refill = float(data.get("last_refill", now))

        tokens = min(
            self.capacity,
            tokens + (now - last_refill) * self.refill_rate
        )

        if tokens < 1:
            redis_client.hset(
                redis_key,
                mapping={"tokens": tokens, "last_refill": now}
            )
            return False

        tokens -= 1
        redis_client.hset(
            redis_key,
            mapping={"tokens": tokens, "last_refill": now}
        )
        return True
