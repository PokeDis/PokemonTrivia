# Pokemon Trivia API

## Description

Simple json API for Pokemon Trivia and quiz questions.

## Usage

- Endpoint: https://pokemontrivia-1-c0774976.deta.app/
    - `/trivia` - returns a random trivia question

### Trivia Endpoint

```http
  GET /trivia
```

| Parameter  | Type     | Description                                                                                                                                   |
|:-----------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| `endpoint` | `string` | **Required**. Type of trivia question. Can be one of the following: `images`, `bonus`, `gen1`, `gen2`, `gen3`, `gen4`, `gen5`, `gen6`, `gen7` |

```python
import requests

url = "https://pokemontrivia-1-c0774976.deta.app/trivia"
response = requests.get(url, params={"endpoint": "images"})
print(response.url)
print(response.json())
```

```python
"https://pokemontrivia-1-c0774976.deta.app/trivia?endpoint=images"
{
    "id": 163,
    "label": "163",
    "specific": {
        "hints": [
            "Held item that makes Pokemon evolve upon level up",
            "The kings most prized possession"
        ],
        "image": "http://pokemontrivia-1-c0774976.deta.app/assets/images/kings_rock.png",
        "imageText": "Name this item",
        "word": "kings rock"
    }
}
```

## Setup

- Clone the repo
- Install dependencies with `pip install -r requirements.txt`
- Run `python main.py` to start the server
