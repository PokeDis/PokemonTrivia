from __future__ import annotations

import importlib
import inspect
import json
import typing as t

import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles

from src.extensions import Extension
from src.utils.paths import PATHS

from .logger import Logger

__author__: str = "FallenDeity"
__version__: str = "0.0.1"
__all__: tuple[str, ...] = ("Website",)


class Website(fastapi.FastAPI):
    data: t.Dict[str, t.Any] = {}
    _mounts: t.ClassVar[t.Dict[str, t.Any]] = {
        "/assets": StaticFiles(directory=str(PATHS.ASSETS)),
        "/bin": StaticFiles(directory=str(PATHS.BIN)),
    }

    def __init__(
        self,
        *,
        title: str = __author__,
        debug: bool = False,
        **kwargs: t.Any,
    ) -> None:
        super().__init__(
            title=title,
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
            debug=debug,
            **kwargs,
        )
        self.logger = Logger(name=__name__, file=False)

    def _mount_files(self) -> None:
        self.logger.info("Mounting files")
        for path, file in self._mounts.items():
            self.mount(path, file)
            self.logger.info(f"Mounted {path}")
        with open(PATHS.BIN / "trivia_utf-8.json") as f:
            self.data = json.load(f)
        self.logger.info("Files mounted")

    def _auto_setup(self, path: str) -> None:
        module = importlib.import_module(path)
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Extension) and name != "Extension":
                router = obj(app=self)
                self.include_router(router)
                self.logger.info(f"Loaded {name} extension")

    def _load_files(self) -> None:
        self.logger.info("Loading extensions")
        for file in PATHS.EXTENSIONS.glob("*.py"):
            if file.name.startswith("_"):
                continue
            self._auto_setup(f"{PATHS.EXTENSIONS.parent}.{PATHS.EXTENSIONS.name}.{file.stem}")
        self.logger.info("Extensions loaded")

    async def on_startup(self) -> None:
        self.logger.info("Starting up...")
        self._mount_files()
        self._load_files()
        self.logger.flair("Started up successfully.")

    async def on_shutdown(self) -> None:
        self.logger.flair("Shutting down...")
        self.logger.error("Shut down successfully.")

    def run(self) -> None:
        self.logger.flair("Running...")
        uvicorn.run(
            "main:app",
            reload=True,
            reload_dirs=[str(PATHS.EXTENSIONS)],
            use_colors=True,
        )
