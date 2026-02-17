from ..base import safe_import


def instrument(app):
    module = safe_import(
        "opentelemetry.instrumentation.flask",
        "pip install sentinel-agent-lib[flask]",
    )

    FlaskInstrumentor = module.FlaskInstrumentor
    FlaskInstrumentor().instrument_app(app)
