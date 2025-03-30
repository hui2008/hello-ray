from ray import serve
import ray
from fastapi import FastAPI

app = FastAPI()

@serve.deployment
@serve.ingress(app)
class HelloWorld:
    @app.get("/hello")
    async def hello(self):
        return "Hello from Ray Serve!"

if __name__ == "__main__":
    ray.init(address="auto")
    serve.start(http_options={"host": "0.0.0.0"})
    serve.run(HelloWorld.bind(), blocking=True, route_prefix="/")
