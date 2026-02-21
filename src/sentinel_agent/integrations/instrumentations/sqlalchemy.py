from ..base import safe_import


def instrument(engine=None):
    module = safe_import(
        "opentelemetry.instrumentation.sqlalchemy",
        "pip install sentinel-agent-lib[sqlalchemy]",
    )

    SQLAlchemyInstrumentor = module.SQLAlchemyInstrumentor

    if engine is not None:
        SQLAlchemyInstrumentor().instrument(engine=engine)
    else:
        SQLAlchemyInstrumentor().instrument()
