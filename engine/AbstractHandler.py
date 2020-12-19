from engine.Handler import Handler


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, total, request=None):
        if self._next_handler:
            return self._next_handler.handle(total, request)
        return None