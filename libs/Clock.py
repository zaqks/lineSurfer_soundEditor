class Clock:
    def __init__(self, parentClk,  childClk):
        self.clk =  childClk/parentClk
        self.counter = self.clk

    def tick(self):
        if self.counter >= self.clk:
            self.counter = 1
            return True

        self.counter += 1 
        return False