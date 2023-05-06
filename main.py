import asyncio

from src import Website

app = Website(docs_url="/docs", redoc_url="/redoc")
loop = asyncio.get_event_loop()
loop.create_task(app.on_startup())


if __name__ == "__main__":
    app.run()
