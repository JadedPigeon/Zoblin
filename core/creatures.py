class CreatureBaseline():
    def __init__(self, name, health, mana, strength, defence, creature_type):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.creature_type = creature_type
        self.weakness = {
            "slash": 0,
            "crush": 0,
            "stab": 0,
            "magic": 0
        }

    def creature_damage(self, damage):
        self.health -= damage

    def creature_health(self, heal):
        self.health += heal

class PlayerCharacter(CreatureBaseline):
    def __init__(self, name, health, mana, strength, defence, creature_type):
        super().__init__(name, health, mana, strength, defence, creature_type)