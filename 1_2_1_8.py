import random

class Apple:
    counter_apples = 0
    total_weight = 0
    def __init__(self,weight):
        if Apple.counter_apples <= 1000 and Apple.total_weight+weight <= 300:
            self.weight = weight
            Apple.counter_apples += 1
            Apple.total_weight += weight
        else:
            pass
            
            
            
def apples():
    while True:
        weight = random.uniform(0.2,0.5)
        if  Apple.counter_apples > 1000 or Apple.total_weight + weight > 300:
            break
        Apple(weight)
        
        
    print(f'The number of packaged apples is {Apple.counter_apples}')
    print(f'The weight of the packaged apples is {Apple.total_weight}')
        
