import data
import prototype
import var

def game_init():
    var.Player.hand = [prototype.Card(data.card[1]), prototype.Card(data.card[1]), prototype.Card(data.card[2]), prototype.Card(data.card[2])]
    var.Player.deck = []
    var.Field.unit = [
        prototype.Leader(),
        prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(),
        prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(), prototype.Empty(),
        prototype.Leader()
    ]
