class Wizard:
    def __init__(self, name):
        self.name = name
        # Spells are stored as: {'spell_name': power_level}
        self.spellbook = {}

    def learn_spell(self, spell_name, power):
        if spell_name not in self.spellbook:
            self.spellbook[spell_name] = power
            print(f"{self.name} has learned {spell_name}!")
        else:
            print(f"{self.name} already knows {spell_name}.")

    def cast_spells(self, spell_targets):
        total_power = 0
        print(f"\n--- {self.name} begins casting! ---")
        for spell in spell_targets:
            if spell in self.spellbook:
                power = self.spellbook[spell]
                print(f"Casting {spell} with power {power}!")
                total_power += power
            else:
                print(f"Cannot cast {spell}. Spell is unknown.")
        return total_power

# --- A new wizard begins their training! ---

gandalf = Wizard("Gandalf")
saruman = Wizard("Saruman")

# Learning phase

gandalf.learn_spell("Fireball", 50)
gandalf.learn_spell("Frostbolt", 40)
saruman.learn_spell("Fireball", 60)

# Battle phase
spells_to_cast = ["Fireball", "Lightning Bolt", "Frostbolt"]
damage_dealt_gandalf = gandalf.cast_spells(spells_to_cast[1:])
damage_dealt_saruman = saruman.cast_spells(spells_to_cast[0:1])

# Final status
print(f"\nTotal damage dealt by gandalf: {damage_dealt_gandalf}")
print(f"Total damage dealt by saruman: {damage_dealt_saruman}")
print(f"\nFinal spellbooks: {gandalf.spellbook} and {saruman.spellbook}")
