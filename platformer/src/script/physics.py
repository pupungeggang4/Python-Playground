class Physics():
    @staticmethod
    def collide_check_up(base, entity):
        if abs(base.pos.x - entity.pos.x) < base.size.x / 2 + entity.size.x / 2:
            if entity.pos.y < base.pos.y:
                return base.size.y / 2 + entity.size.y / 2 - (base.pos.y - entity.pos.y)
        return 0

    @staticmethod
    def collide_check_down(base, entity):
        if abs(base.pos.x - entity.pos.x) < base.size.x / 2 + entity.size.x / 2:
            if entity.pos.y > base.pos.y:
                return base.size.y / 2 + entity.size.y / 2 + (base.pos.y - entity.pos.y)
        return 0

    @staticmethod
    def collide_check_left(base, entity):
        if abs(base.pos.y - entity.pos.y) < base.size.y / 2 + entity.size.y / 2:
            if entity.pos.x < base.pos.x:
                return base.size.x / 2 + entity.size.x / 2 - (base.pos.x - entity.pos.x)
        return 0

    @staticmethod
    def collide_check_right(base, entity):
        if abs(base.pos.y - entity.pos.y) < base.size.y / 2 + entity.size.y / 2:
            if entity.pos.x < base.pos.x:
                return base.size.x / 2 + entity.size.x / 2 + (base.pos.x - entity.pos.x)
        return 0
