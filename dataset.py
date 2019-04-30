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

def print_data(dataset):
  for data in dataset:
    print(data.x[0], data.x[1], data.y)

def middle_point(dataset):
  length = len(dataset[0].x)
  count = [0,0]

  r = [
    [0 for i in range(length)], # y = 0
    [0 for i in range(length)]  # y = 1
  ]
  
  for data in dataset:
    count[data.y] += 1
    for i in range(len(data.x)):
      r[data.y][i] += data.x[i]
  
  return [
    (
      [
        (r[k][i] / count[k]) for i in range(length)
      ] if count[k] > 0 else r[k]
    ) for k in range(len(r))
  ]

def get_middle(dataset):

  x = middle_point(dataset)

  return [
    data_point(x[0], 0),
    data_point(x[1], 1)
  ]