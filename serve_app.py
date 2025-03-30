from ray import serve
import ray
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello from Ray Serve!"

@serve.deployment
@serve.ingress(app)
class HelloWorld:
    pass

if __name__ == "__main__":
    ray.init(address="auto")
    serve.start(http_options={"host": "0.0.0.0", "port": 8000})
    serve.run(HelloWorld.bind(), blocking=True, route_prefix="/")