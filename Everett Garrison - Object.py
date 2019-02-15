class Battle(object):
    def __init__(self, enemy_name="jeff", run=True, enemy_health=15, enemy_damage=5, enemy_defense=5):
        self.enemy_name = enemy_name
        self.run = run
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_defense = enemy_defense
        self.drop_item = "A piece of lint."
        self.player_health = 25
        self.player_damage = 10
        self.player_defense = 10
        self.battling = True

    def p_strangle(self):
        if self.battling:
            if self.player_health and self.enemy_health > 0:
                print("Player health: %d" % self.player_health)
                print("Enemy health: %d" % self.enemy_health)
                self.enemy_health -= (self.player_damage - (self.enemy_defense * 0.5))
                print("-" * 20)
                print("You grab the rat by the throat and strangle it for a couple seconds before it wriggles out of "
                      "your grasp.")
                print("-" * 20)
                print("Player health: %d" % self.player_health)
                print("Enemy health: %d" % self.enemy_health)
            else:
                self.battling = False
        else:
            print("-" * 20)
            print("The battle is over, cease.")
            print("-" * 20)

    def e_attack(self):
        if self.battling:
            if self.player_health and self.enemy_health > 0:
                self.player_health -= (self.enemy_damage - (self.player_defense * 0.5))
                print("-" * 20)
                print("The rat runs up and bites your ankle viciously with bloodlust before scurrying back away from "
                      "you.")
                print("-" * 20)
                print("Player health: %d" % self.player_health)
                print("Enemy health: %d" % self.enemy_health)
                print("-" * 20)
            else:
                self.battling = False
        else:
            print("-" * 20)
            print("The battle is over, cease.")
            print("-" * 20)


mrat = Battle("Mutated rat", True)

mrat.p_strangle()
mrat.e_attack()
mrat.p_strangle()
mrat.e_attack()
mrat.p_strangle()
