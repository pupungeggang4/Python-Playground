class Physics():
    @staticmethod
    def check_fall(base, fall):
        if fall.pos.y < base.pos.y and fall.pos.x > base.pos.x - base.size.x / 2 - fall.size.x / 2 and fall.pos.x < base.pos.x + base.size.x / 2 + fall.size.x / 2:
            return fall.size.y / 2 + base.size.y / 2 - (base.pos.y - fall.pos.y)
        return 0