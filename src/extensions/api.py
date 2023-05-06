from __future__ import annotations

import random
import typing

import fastapi

from src.utils.paths import ROUTES

from . import Extension, route


class Trivia(Extension):
    @route(path="/trivia", method="GET", response_model=fastapi.responses.JSONResponse)
    async def trivia(
        self, request: fastapi.Request, endpoint: typing.Optional[ROUTES] = None
    ) -> fastapi.responses.JSONResponse:
        if endpoint is None:
            return fastapi.responses.JSONResponse(
                status_code=404,
                content={"endpoints": [i for i in ROUTES]},
            )
        data = random.choice(self.app.data[endpoint.value])
        data["specific"]["image"] = f"{request.url.scheme}://{request.url.netloc}{data['specific']['image']}"
        return data
