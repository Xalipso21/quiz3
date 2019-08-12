from .orm import ORM

class TSLA(ORM):
    dbpath = ""
    tablename = "tesla"
    fields = ['title', 'description', 'complete']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.open = kwargs.get("open")
        self.close = kwargs.get("close")
        self.high = kwargs.get("high")
        self.low = kwargs.get("low")
        self.adjusted_close = kwargs.get("adjusted_close")
        self.volume=kwargs.get("volume")
