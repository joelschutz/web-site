

class AppError(Exception):
    pass


class ServiceNotFound(AppError):
    pass


class ReachingAPILimit(AppError):
    pass
