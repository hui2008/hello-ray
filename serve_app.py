from ray import serve
@serve.deployment
class HelloWorld:
    async def __call__(self):
        return "Hello from Ray Serve!"

if __name__ == "__main__":
    serve.run(HelloWorld.bind(), blocking=True, route_prefix="/hello")
