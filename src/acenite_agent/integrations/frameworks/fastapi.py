from ..base import safe_import


def instrument(app):
    module = safe_import(
        "opentelemetry.instrumentation.fastapi",
        "pip install acenite-agent[fastapi]",
    )

    FastAPIInstrumentor = module.FastAPIInstrumentor
    FastAPIInstrumentor().instrument_app(app)
