import ray
from ray import serve

def hello(request):
    return "Hello, world!"

@serve.deployment
def hello():
    return "hello"

if __name__ == "__main__":
    ray.init(dashboard_host='0.0.0.0')
    serve.run(hello.bind(), blocking=True, route_prefix="/hello")
