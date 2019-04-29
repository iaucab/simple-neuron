class data_point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

test_data = [
  data_point([8.3,7.9], 1),
  data_point([7.6,8.6], 1),
  data_point([6.8,9.8], 1),
  data_point([9.8,5.1], 1),
  data_point([8.8,9.1], 1),
  data_point([8.3,7.8], 1),
  data_point([4.5,3.2], 0),
  data_point([6.8,6.2], 0),
  data_point([7.8,2.3], 0),
  data_point([1.6,8.4], 0),
  data_point([4.3,7.4], 0),
  data_point([6.9,6.2], 0),
  data_point([5.5,5.1], 0),
  data_point([3.6,6.3], 0),
  data_point([0.5,1.2], 0),
  data_point([2.8,8.4], 0),
  data_point([6.7,6.6], 0)
]

AND = [
  data_point([0,0], 0),
  data_point([1,0], 0),
  data_point([0,1], 0),
  data_point([0,0], 1)
]

OR = [
  data_point([0,0], 0),
  data_point([1,0], 1),
  data_point([0,1], 1),
  data_point([0,0], 1)
]

bin2dec = [
  data_point([0,0,0], 0),
  data_point([0,0,1], 1),
  data_point([0,1,0], 2),
  data_point([0,1,1], 3),
  data_point([1,0,0], 4),
  data_point([1,0,1], 5),
  data_point([1,1,0], 6),
  data_point([1,1,1], 7)
]

def print_data(dataset):
  for data in dataset:
    print(data.x[0], data.x[1], data.y)