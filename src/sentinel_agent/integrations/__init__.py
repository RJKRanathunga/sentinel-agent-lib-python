FRAMEWORKS = {
    "flask": "sentinel_agent.integrations.frameworks.flask:instrument",
    "fastapi": "sentinel_agent.integrations.frameworks.fastapi:instrument",
    "django": "sentinel_agent.integrations.frameworks.django:instrument",
}

INSTRUMENTATIONS = {
    "requests": "sentinel_agent.integrations.instrumentations.requests:instrument",
    "httpx": "sentinel_agent.integrations.instrumentations.httpx:instrument",
    "psycopg2": "sentinel_agent.integrations.instrumentations.psycopg2:instrument",
    "sqlalchemy": "sentinel_agent.integrations.instrumentations.sqlalchemy:instrument",
}
