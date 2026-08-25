class ORDER_SOURCE(object):
    KEY = "order_source"
    VERSION_KEY = "order_source_version"
    VALUE = "python-sdk"

    @staticmethod
    def version():
        # __version__ is set at the top of nimbbl/__init__.py before submodules load, so it is
        # always available by the time create() runs. Narrow catch: fall back only if it is
        # genuinely absent (removed/renamed) rather than masking unrelated errors.
        try:
            from nimbbl import __version__
            return __version__
        except (ImportError, AttributeError):
            return "0.0.0"
