class ORDER_SOURCE(object):
    KEY = "order_source"
    VERSION_KEY = "order_source_version"
    VALUE = "python-sdk"

    @staticmethod
    def version():
        # Resolved lazily to avoid an import cycle with the package __init__.
        try:
            from nimbbl import __version__
            return __version__
        except Exception:
            return "0.0.0"
