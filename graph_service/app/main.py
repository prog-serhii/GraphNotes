import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from neo4j import basic_auth, AsyncGraphDatabase

app = FastAPI()

uri = os.getenv('NEO4J_URI')
username = os.getenv('NEO4J_USERNAME')
password = os.getenv('NEO4J_PASSWORD')
database = os.getenv('NEO4J_DATABASE')

driver = AsyncGraphDatabase.driver(uri, auth=basic_auth(username, password))


@asynccontextmanager
async def get_db():
    async with driver.session(database=database) as session:
        yield session


@app.get("/graph")
async def get_graph(limit: int = 100):
    async def work(tx):
        result = await tx.run(
            "MATCH (m:Movie)<-[:ACTED_IN]-(a:Person) "
            "RETURN m.title AS movie, collect(a.name) AS cast "
            "LIMIT $limit",
            {"limit": limit}
        )
        return [record_ async for record_ in result]

    async with get_db() as db:
        results = await db.execute_read(work)
        nodes = []
        rels = []
        i = 0
        for record in results:
            nodes.append({"title": record["movie"], "label": "movie"})
            target = i
            i += 1
            for name in record["cast"]:
                actor = {"title": name, "label": "actor"}
                try:
                    source = nodes.index(actor)
                except ValueError:
                    nodes.append(actor)
                    source = i
                    i += 1
                rels.append({"source": source, "target": target})
        return {"nodes": nodes, "links": rels}
