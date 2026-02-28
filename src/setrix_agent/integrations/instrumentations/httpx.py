from ..base import safe_import


def instrument():
    module = safe_import(
        "opentelemetry.instrumentation.httpx",
        "pip install sentinel-agent-lib[httpx]",
    )

    HTTPXClientInstrumentor = module.HTTPXClientInstrumentor
    HTTPXClientInstrumentor().instrument()
