FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY src ./src

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uv", "run", "python", "src/main.py"]