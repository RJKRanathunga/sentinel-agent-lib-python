from .otel import setup_otel
from .heartbeat import send_heartbeat
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from opentelemetry import trace


class SentinelAgent:
    _started = False

    @classmethod
    def start(
        cls,
        *,
        app: Flask,
        api_key: str,
        service_name: str = "unknown-service",
        enable_logging: bool = True,
        enable_heartbeat: bool = True,
        heartbeat_interval: float = 60.0,
    ) -> None:

        if cls._started:
            return

        if enable_logging:
            setup_otel(
                app=app,
                api_key=api_key,
                service_name=service_name
            )

        if enable_heartbeat:
            scheduler = BackgroundScheduler(daemon=True)
            scheduler.add_job(send_heartbeat, "interval", seconds=heartbeat_interval, max_instances=1, coalesce=True,
                kwargs={
                    "api_key": api_key,
                    "interval": heartbeat_interval,
                },
            )
            scheduler.start()

        cls._started = True

    @classmethod
    def get_tracer(cls):
        tracer = trace.get_tracer(__name__)
        return tracer
