class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.changes = []
        self.undoChanges = []

    def add(self, num: int):
        self.value += num
        self.changes.append(num)

    def subtract(self, num: int):
        self.add(-num)

    def undo(self):
        self.bulk_undo(1)

    def redo(self):
        self.bulk_redo(1)

    def bulk_undo(self, steps: int):
        # take the top steps of the redo stack and move them to the undo stack
        undoVals = self.changes[-steps:]
        undoVals.reverse()
        self.value -= sum(undoVals)
        self.changes = self.changes[:-steps]
        self.undoChanges.extend(undoVals)
        
    def bulk_redo(self, steps: int):
        # take the top steps of the undo stack and move them to the redo stack
        redoVals = self.undoChanges[-steps:]
        redoVals.reverse()
        self.value += sum(redoVals)
        self.undoChanges = self.undoChanges[:-steps]
        self.changes.extend(redoVals)
