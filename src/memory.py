class Memory:

  def __init__(self):
    self.memory = []
  
  def load(self, offset: int):
    return self.memory[offset]
  
  def store(self, offset: int, value: int):
    self.memory[offset] = value