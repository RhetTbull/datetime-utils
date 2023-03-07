# Developer Notes

These are notes for developers of the project.

## Development Environment

While the package has no dependencies, the development environment does. To set up the development environment, run:

```bash
pip install -r requirements_dev.txt
```

## Testing

- `python -m pytest --cov=datetime_tzutils --cov-report=term-missing`

## Publishing

Uses [flit](https://flit.readthedocs.io/en/latest/) to publish to PyPI.

- `flit publish`
