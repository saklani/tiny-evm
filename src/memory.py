class Memory:

  def __init__(self):
    self.memory = []
  
  def load(self, offset: int):
    return self.memory[offset]
  
  def store(self, offset: int, value: int):
    if offset >= len(self.memory):
      size = (offset // 32 + 1) * 32 - len(self.memory)
      expand = [0] * size
      self.memory += expand
    self.memory[offset] = value