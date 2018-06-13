
class Request:

    def __init__(self,name,destiny):
        self.name = name
        self.destiny=destiny

    def getName(self):
        return self.name

    def getDestiny(self):
        return self.destiny

class BridgeRequest:

    def __init__(self,name, destiny, maxValue, currentValue):
        self.name = name
        self.destiny = destiny
        self.maxValue = maxValue
        self.currentValue = currentValue

    def getName(self):
        return self.name

    def getDestiny(self):
        return self.destiny

    def getMaxValue(self):
        return self.maxValue

    def getCurrentValue(self):
        return self.currentValue

    def getFilter(self):
        if self.currentValue < self.maxValue:
            return 0
        else:
            return 1

class RoundaboutRequest:
    def __init__(self, name, destiny, origin, currentValue):
        self.name = name
        self.destiny = destiny
        self.origin = origin
        self.currentValue = currentValue

    def getName(self):
        return self.name

    def getDestiny(self):
        return self.destiny

    def getOrigin(self):
        return self.origin

    def getCurrentValue(self):
        return self.currentValue

    def getFilter(self):
        if self.currentValue < self.maxValue:
            return 0
        else:
            return 1

