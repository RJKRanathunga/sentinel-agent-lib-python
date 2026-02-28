from ..base import safe_import


def instrument():
    module = safe_import(
        "opentelemetry.instrumentation.django",
        "pip install sentinel-agent-lib[django]",
    )

    DjangoInstrumentor = module.DjangoInstrumentor
    DjangoInstrumentor().instrument()
