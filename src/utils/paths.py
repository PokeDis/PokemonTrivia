from __future__ import annotations

import enum
import pathlib

# pyright: reportGeneralTypeIssues=false
__all__: tuple[str, ...] = (
    "PATHS",
    "ROUTES",
)


class ROUTES(str, enum.Enum):
    IMAGES: str = "images"
    BONUS: str = "bonus"
    GEN1: str = "gen1"
    GEN2: str = "gen2"
    GEN3: str = "gen3"
    GEN4: str = "gen4"
    GEN5: str = "gen5"
    GEN6: str = "gen6"
    GEN7: str = "gen7"


class PATHS:
    ASSETS: pathlib.Path = pathlib.Path("src/assets")
    BIN: pathlib.Path = pathlib.Path("src/bin")
    EXTENSIONS: pathlib.Path = pathlib.Path("src/extensions")
