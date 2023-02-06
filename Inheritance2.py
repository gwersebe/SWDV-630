# Gabriel Wersebe

#  Consider the following code:

 

class Spell:
  def __init__(self, incantation, name):
    self.name = name
    self.incantation = incantation

  def __str__(self):
    return self.name + ’ ’ + self.incantation + ’\n’ + self.get_description()

  def get_description(self):
    return ’No description’

  def execute(self):
    print self.incantation

class Accio(Spell):
  def __init__(self):
    Spell.__init__(self, ’Accio’, ’Summoning Charm’)

class Confundo(Spell):
  def __init__(self):
    Spell.__init__(self, ’Confundo’, ’Confundus Charm’)

  def get_description(self):
    return ’Causes the victim to become confused and befuddled.’

def study_spell(spell):
  print spell

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

 

# Answer the following questions:

# 1. What are the parent and child classes here?

# 2. What are the base and sub-classes?

# 3. What is the output from this code?   Try without running if you can

# 4. When study_spell(Confundo()) executes...what get_description method gets called and why?

# 5. The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? Write down the code that we need to add and/or change.


# 1. The parent class is "Spell" and the child classes are "Accio" and "Confundo".

# 2. The base class is "Spell" and the sub-classes are "Accio" and "Confundo".

# 3. The output is:
# Accio
# Summoning Charm Accio
# No description
# Confundus Charm Confundo
# Causes the victim to become confused and befuddled.

# 4. The get_description method gets called from the Confudo class it calls the get_description method from the Confudo class because it has its own get_description method.

# 5. If we wanted to add a similar method to Accio we would need to write a get_description method in their as well.

def get_description(self):
    return "This charm summons an object to the caster, potentially over a significant distance"

