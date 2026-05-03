from ..base import safe_import


def instrument():
    module = safe_import(
        "opentelemetry.instrumentation.psycopg2",
        "pip install acenite-agent[psycopg2]",
    )

    Psycopg2Instrumentor = module.Psycopg2Instrumentor
    Psycopg2Instrumentor().instrument()
