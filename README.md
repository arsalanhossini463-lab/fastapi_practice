# FastAPI List API

A small REST API built with [FastAPI](https://fastapi.tiangolo.com/) that manages a list of numbers, plus a Python client that calls it with `requests`. It is a simple example of the four main HTTP methods: `GET`, `POST`, `PUT` and `DELETE`.

The list lives in memory and starts as `[10, 20, 30, 40, 50, 60]`. It resets every time the server restarts.

## Files

| File | Description |
|------|-------------|
| `app.py` | The API server. Uses `FastAPIOffline`, so the interactive docs work without internet access. |
| `call_api.py` | Functions that call the API with `requests`, with a small demo at the bottom. |

## Endpoints

| Method | Path | Parameters | Description |
|--------|------|------------|-------------|
| GET | `/` | | Hello message |
| GET | `/home/` | | Welcome message |
| GET | `/getitem/` | | Return the whole list |
| POST | `/add/{new_item}` | `new_item` (in the path) | Add a number to the end of the list |
| POST | `/addindex/` | `index`, `newitem` | Insert a number at a given index |
| DELETE | `/deleteitem/` | `item` | Remove a number by value |
| DELETE | `/deleteindex/` | `index` (default `-1`) | Remove the number at a given index (the last one by default) |
| PUT | `/update/` | `old_item`, `new_item` | Replace a number by value |
| PUT | `/updateindex/` | `index`, `new_item` | Replace the number at a given index |

Example:

```bash
curl -X POST "http://127.0.0.1:8000/add/70"
curl "http://127.0.0.1:8000/getitem/"
```

## Requirements

- Python 3
- The packages in `requirements.txt`: `fastapi-offline`, `uvicorn` and `requests`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Start the server:

```bash
uvicorn app:app --reload
```

The API runs at `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` to try every endpoint in the browser.

In a second terminal, run the client demo:

```bash
python call_api.py
```

It prints the list, removes the last item, and prints the list again. You can import the functions from `call_api.py` (`get_all_item`, `add_item`, `delete_item`, `delete_item_by_index`, `update_item`, `update_item_by_index`) in your own code.

## Notes

- The server must be running before you run `call_api.py`.
- `call_api.py` has no function for `/addindex/`. Call it from `/docs` or with `curl`.
- The client functions return `"EROR"` if the server answers with a status other than 200.
