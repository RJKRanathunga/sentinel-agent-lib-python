from flask import Flask

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

from src.sentinel_agent.constants import SENTINEL_URL


def setup_otel(*,app: Flask,api_key: str, service_name: str) -> None:
    provider = TracerProvider(
        resource=Resource.create({"service.name": service_name})
    )
    trace.set_tracer_provider(provider)

    exporter = OTLPSpanExporter(
                endpoint=f"{SENTINEL_URL}/monitor/",
                headers={"Authorization": f"Bearer {api_key}"}
                )

    provider.add_span_processor(BatchSpanProcessor(exporter))

    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()
