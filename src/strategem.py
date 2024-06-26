class Strategem:
  def __init__(self, name, category, command, icon_name):
    self.name = name
    self.category = category
    self.command = command
    self.icon_name = icon_name
  
  def prepare_strategem(self, model, executer):
    self.commandArray=[]
    for input in self.command:
      key = model.settings.strategemKeys[input]
      self.commandArray.append(executer.parse_macro_key(key))