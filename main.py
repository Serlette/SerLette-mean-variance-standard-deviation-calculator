import numpy as np

input_str = input('Enter nine numbers separated by spaces: ')
input_list = [int(x) for x in input_str.split()]

def calculate(numbers):
  if len(numbers) != 9:
    raise ValueError("List must contain nine numbers.")
  print(numbers)
  a = np.array(numbers).reshape(3, 3)
  #print(a)

  cal = {}
  cal = ({'mean': [a.mean(0).tolist(), a.mean(1).tolist(), a.mean()],
          'variance': [a.var(0).tolist(), a.var(1).tolist(), a.var()],
          'standard deviation': [a.std(0).tolist(), a.std(1).tolist(), a.std()],
          'max': [a.max(0).tolist(), a.max(1).tolist(), a.max()],
          'min': [a.min(0).tolist(), a.min(1).tolist(), a.min()],
          'sum': [a.sum(0).tolist(), a.sum(1).tolist(), a.sum()]
          })



  return cal
print(calculate(input_list))
