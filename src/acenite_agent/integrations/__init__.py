FRAMEWORKS = {
    "flask": "acenite_agent.integrations.frameworks.flask:instrument",
    "fastapi": "acenite_agent.integrations.frameworks.fastapi:instrument",
    "django": "acenite_agent.integrations.frameworks.django:instrument",
}

INSTRUMENTATIONS = {
    "requests": "acenite_agent.integrations.instrumentations.requests:instrument",
    "httpx": "acenite_agent.integrations.instrumentations.httpx:instrument",
    "psycopg2": "acenite_agent.integrations.instrumentations.psycopg2:instrument",
    "sqlalchemy": "acenite_agent.integrations.instrumentations.sqlalchemy:instrument",
}
