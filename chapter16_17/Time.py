import copy

class Time(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.min = minute
        self.sec = second
    def print_time(self):
        """ Exerciese 1"""
        print "%.2d:%.2d:%.2d" %(self.hour,self.min,self.sec)
        
    def increment(self,seconds):
        """ Exercise 2"""
        self.sec += seconds
    
        actSec = self.sec%60
        addMin = self.sec/60
        
        self.sec = actSec
        self.min += addMin
        
        actMin = self.min%60
        addHr = self.min/60
        
        self.min = actMin
        self.hour +=addHr
        
        self.hour = self.hour%24
    def time_to_int(self):
        """Exercise 17_1 """
        minutes = self.hour * 60 + self.min
        seconds = minutes * 60 + self.sec
        return seconds 
    
    
  
def time_to_int_Pure(time):
    minutes = time.hour * 60 + time.min
    seconds = minutes * 60 + time.sec
    return seconds        
        
def int_to_time(seconds):
    time = Time()
    minutes, time.sec = divmod(seconds, 60)
    time.hour, time.min = divmod(minutes, 60)
    time.hour = time.hour%24
    return time        

def is_after(t1,t2):
    """Exercise 3"""
    return ((t1.hour*60*60)+(t1.min*60)+t1.sec) > ((t2.hour*60*60)+(t2.min*60)+t2.sec)

def increment_pure(t1,seconds):
    """Exercise 4"""
    newTime = copy.copy(t1)
    
    newTime.sec += seconds
    
    actSec = newTime.sec%60
    addMin = newTime.sec/60
        
    newTime.sec = actSec
    newTime.min += addMin
        
    actMin = newTime.min%60
    addHr = newTime.min/60
        
    newTime.min = actMin
    newTime.hour +=addHr
        
    newTime.hour = newTime.hour%24
    
    return newTime

def increment_short(t,seconds):
    """ Exercise 5"""
    t_inSec = time_to_int_Pure(t)
    t_inSec +=seconds
    return int_to_time(t_inSec)
def mul_time(t,num):
    """Exercise 6_1"""
    t_inSec = time_to_int_Pure(t)
    prod = t_inSec*num
    return int_to_time(prod)

def avgSpeed(t,d):
    t_sec = time_to_int_Pure(t)
    speed_inSec = t_sec/d
    return int_to_time(speed_inSec)
    
if __name__ == "__main__":
    t1 = Time()
    t1.print_time()
    t2 = Time(15,30,54)
    t2.print_time()
    
    print is_after(t2, t1)
    
    t1.increment(108000)
    t1.print_time()
    
    t3 = Time()
    t4 = increment_pure(t3,108000)
    t3.print_time()
    t4.print_time()
    t5 = increment_short(t3, 108197)
    t3.print_time()
    t5.print_time()
    
    StartTime = Time(1,0,0)
    print "Start Time = ",
    StartTime.print_time()
    MulTime = mul_time(StartTime, 8)
    print "Mul Time = ",
    MulTime.print_time()
    EndTime = Time(0,45,32)
    AvgTime = avgSpeed(EndTime, 8)
    
    print "End Time = ",
    EndTime.print_time()
    
    print "Avarage speed for 8 miles in miles per hour = ",
    AvgTime.print_time()
    
    print "Cross Check avg time with mul_time = ",
    mul_time(AvgTime, 8).print_time()
    