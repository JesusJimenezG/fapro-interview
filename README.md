# Fapro interview project

Desafío: Creación de API para consultar la Unidad de Fomento en Python <https://gist.github.com/lhidalgo42/47c2c1ea4ddbfd50e4b0acd82c24bc23>

## Requerimientos

- Python 3.10
- Poetry

## Instalación

```bash
poetry install
```

## Ejecución

```bash
poetry run uvicorn app.main:app --reload
```

## Tests

```bash
poetry run pytest tests/tests.py
```
