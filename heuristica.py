class Alfred:
  def __init__(self, name, motorcycle, schdule, shift):
    self.name = name
    self.motorcycle = motorcycle
    self.schedule = Schedule(shift)

  def __str__(self):
    return self.name + " " + str(self.motorcycle)

class Schedule:
  def __init__(self, shift):
    self.array = [True] * 24
    self.shift = shift
    if shift == "A":
      schedule_range = range(0,16)
    elif shift == "B":
      schedule_range = range(2,18)
    else
      schedule_range = range(4,20)
    for i in schedule_range:
      self.array[i] = False


alfreds = []

a1 = Alfred("John", False)
alfreds.append(a1)
a2 = Alfred("Sergio", False)
alfreds.append(a2)
a3 = Alfred("Isabel", True)
alfreds.append(a3)
a4 = Alfred("Santiago", True)
alfreds.append(a4)
a5 = Alfred("Miguel", False)



print(a1.name)
print(a1.motorcycle)
for alf in alfreds: 
    print(alf)