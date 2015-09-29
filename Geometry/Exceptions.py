

class ZeroSlope(Exception):
    pass

class InfiniteSlope(Exception):
    pass

class CollinearPoints(Exception):
    pass

class InfiniteLength(Exception):
    pass

class Parallel(Exception):
    pass

class NoIntersection(Exception):
    pass

class UngrokkableObject(Exception):
    def __init__(self,obj):
        self.obj = obj

    def __str__(self):
        fmt = "object '%s' is ungrokkable: %s"
        return fmt % (self.obj.__class__.__name__,repr(self.obj))