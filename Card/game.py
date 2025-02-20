import data
import prototype
import var

def game_init():
    var.player = prototype.Player()
    var.player.hand = [prototype.Card(data.card[1]), prototype.Card(data.card[1]), prototype.Card(data.card[2]), prototype.Card(data.card[2])]
    var.player.deck = [prototype.Card(data.card[1]), prototype.Card(data.card[1]), prototype.Card(data.card[2]), prototype.Card(data.card[2])]

    var.field = prototype.Field()
    var.field.unit = [
        prototype.Leader(),
        prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(),
        prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(),
        prototype.Leader()
    ]
