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
        return "{0} {1}\n".format(self.first_name, self.last_name)