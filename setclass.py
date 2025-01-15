class cardSet:
    def __init__(self, number, color, shape, shade):
        self.number = number
        self.color = color
        self.shape = shape
        self.shade = shade
        self.selected = False 

    def __repr__(self):
        return f"cardSet(number={self.number}, color={self.color}, shape={self.shape}, shade={self.shade}, selected={self.selected})"
