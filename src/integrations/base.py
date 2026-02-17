from importlib import import_module


class IntegrationError(RuntimeError):
    pass


def safe_import(module_path: str, install_hint: str):
    try:
        return import_module(module_path)
    except Exception as e:
        raise IntegrationError(
            f"Required dependency not installed.\n"
            f"Install with: {install_hint}"
        ) from e
