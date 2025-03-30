import ray
from ray import serve

@serve.deployment
class HelloWorld:
    async def __call__(self):
        return "Hello from Ray Serve!"

if __name__ == "__main__":
    ray.init(address="auto")
    serve.start(http_options={"host": "0.0.0.0"})
    serve.run(HelloWorld.bind(), blocking=True, route_prefix="/hello")
