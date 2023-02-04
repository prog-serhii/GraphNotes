from fastapi import FastAPI

from config.container import Container


container = Container()


app = FastAPI(debug=container.config.DEBUG)
app.container = container
