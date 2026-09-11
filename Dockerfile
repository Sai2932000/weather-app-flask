# Build stage
FROM python:3.13-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

RUN uv venv .venv && \
    uv pip install --python .venv/bin/python .

COPY app.py .
COPY templates ./templates
COPY static ./static


# Runtime stage
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/app.py .
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/static ./static

RUN groupadd thumma && \
    useradd -m -G thumma appuser

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]