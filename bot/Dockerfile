FROM python:3.12.7-slim-bookworm AS base

WORKDIR /app

RUN python3 -m pip install --upgrade pip virtualenv && \
    python3 -m virtualenv .venv

COPY requirements.txt /tmp/requirements.txt

RUN . .venv/bin/activate && \
    pip --no-cache-dir install --prefer-binary -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt


FROM python:3.12.7-slim-bookworm AS executable

RUN addgroup --gid 1000 notroot  \
    && useradd -u 1000 -g notroot notroot -m

ENV HOME=/app
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH=bot

WORKDIR /app

COPY --from=base                /app/.venv      /app/.venv

COPY --chown=notroot:notroot    entrypoint.sh   /app
COPY --chown=notroot:notroot    .               /app


USER notroot
RUN chmod +x $HOME/entrypoint.sh
CMD ["./entrypoint.sh"]