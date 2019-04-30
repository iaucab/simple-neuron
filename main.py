import sys

from neuron import Neuron
import dataset

neuron = Neuron()

if len(sys.argv) > 1 and sys.argv[1] == "middle":
  my_dataset = dataset.get_middle(dataset.test_data)
else:
  my_dataset = dataset.test_data

print("Please, wait a minute")

end = False
while not end:

  m_error = 0
  
  for data in my_dataset:
    neuron.set_x(data.x)
    neuron.set_y(data.y)

    y = neuron.calc_y()
    e = data.y - y
    m_error += e if e > 0 else -e

    neuron.update()
  
  #print("Medium error:", m_error / len(my_dataset))

  if m_error / len(my_dataset) < 0.01:
    end = True

neuron.print_me()
print("Test data:")
for data in my_dataset:
  neuron.set_x(data.x)
  y = neuron.calc_y()
  print("Expected:", data.y, "Received:", y)


while True:
  print()
  print("Insert your production data")
  x1 = float(input("x1="))
  x2 = float(input("x2="))
  neuron.set_x([x1, x2])
  print("Result:", neuron.calc_y())
  input("Press 'enter' to continue, or 'Ctrl + C' to exit")