def identity(*args, **kwargs):
    """Identity function accounting for complicated possibilities"""
    if len(args) == 0 and len(kwargs) == 0:
        return None
    elif len(args) == 1 and len(kwargs) == 0:
        return args[0]
    elif len(args) > 1 and len(kwargs) == 0:
        return args
    elif len(args) == 0 and len(kwargs) != 0:
        return kwargs
    elif len(args) == 1 and len(kwargs) != 0:
        return (args[0], kwargs)
    elif len(args) > 1 and len(kwargs) != 0:
        return (args, kwargs)