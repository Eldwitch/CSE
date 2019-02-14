class Battle(object):
    def __init__(self, enemy_name="jeff", run=True, enemy_health=10, enemy_damage=5):
        self.enemy_name = enemy_name
        self.run = run
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.drop_item = "A piece of lint."
        self.player_health = 15
        self.player_damage = 10
        self.battling = True

    def strangle(self):

