import ray
from ray import serve
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return "Hello, world!!"

@serve.deployment
@serve.ingress(app)
class Deployment:
    pass

if __name__ == "__main__":
    ray.init(dashboard_host='0.0.0.0')
    serve.run(Deployment.bind(), blocking=True, route_prefix="/")
