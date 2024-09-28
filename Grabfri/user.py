class User:
    def __init__(self, us_info):
        self.id = us_info["id"]
        self.first_name = us_info["first_name"]
        self.last_name = us_info["last_name"]

        if "is_closed" in us_info:
            self.is_closed = us_info["is_closed"]
        else:
            self.is_closed = True

        if "is_deactivated" in us_info:
            self.is_closed = True

        self.domain = us_info["domain"]

    def __str__(self):
        return "{0} {1} {2}\n".format(self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name

    def __hash__(self):
        return hash((self.id, self.first_name, self.last_name))