from fastapi import FastAPI

from config.container import Container


# dependency injection container
container = Container()


app = FastAPI(debug=container.config.DEBUG)
app.container = container


@app.get('/')
async def root():
    return {'info': 'See /docs for documentation'}
