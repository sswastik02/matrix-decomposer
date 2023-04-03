class DotDict(dict):
    """
    a dictionary that supports dot notation 
    as well as dictionary access notation 
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
