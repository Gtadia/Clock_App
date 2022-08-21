import math
class Round:
    def round(self, num):
        if num < 0:
            return 0
            
        if (num - int(num)) >= 0.5:
            return math.ceil(num)
        else: 
            return math.floor(num)