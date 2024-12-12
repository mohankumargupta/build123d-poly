def mark(func):
    if not hasattr(func, '__drawing1d__'):
        func.__drawing1d__ = set()
    func.__drawing1d__.add(mark)
    return func


class FreeFunctionMetaclass(type):
    """Metaclass to dynamically define free functions for marked methods."""
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)

        for method_name, method in namespace.items():
            if callable(method) and getattr(method, "_is_marked", True):
                # Define the free function
                def free_function(*args, method=method, **kwargs):
                    if cls._context_manager is None:
                        raise RuntimeError(f"No active context manager for {cls.__name__}")
                    return getattr(cls._context_manager, method.__name__)(*args, **kwargs)

                free_function.__name__ = method_name
                globals()[method_name] = free_function

        return cls
