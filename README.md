# Polylith Demo

```shell
fraser.langton@KWT1321 polylith-demo % uv run poly check
🤔 Cannot locate httpx, requests in lambda
```

## Repository Structure

```
polylith-demo/
├── bases/
│   └── demo/
│       └── rest_api/
│           ├── __init__.py
│           ├── core.py  <-- has fastapi
│           └── tests/
│               └── test_api.py  <-- has httpx
├── components/
│   └── demo/
│       └── c1/
│           ├── __init__.py
│           └── core.py  <-- has pydantic
│           └── tests/
│               └── test_core.py  <-- has requests
├── development/
├── projects/
│   └── lambda/
│       └── pyproject.toml  <-- has fastapi, pydantic in deps
```
