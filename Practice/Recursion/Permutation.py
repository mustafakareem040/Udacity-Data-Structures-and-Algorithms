def _permute(array, result, builder, index):
  if not array:
    result.append(builder)
  if index == len(array):
    return array
  _permute(array.copy(), result, builder.copy(), index+1)
  builder.append(array[index])
  array.pop(index)
  _permute(array, result, builder.copy(), 0)
  return result

def permute(array):

  """
  Return a list of permutations

  Examples:
  permute([0, 1]) returns [ [0, 1], [1, 0] ]

  Args:
  l(list): list of items to be permuted

  Returns:
  list of permutation with each permuted item being represented by a list

  Time Complexity:
  O(n!)

  Space Complexity:
  O(n!)
  """
  return _permute(array, [], [], 0)

if __name__ == "__main__":
  print(permute([1, 2, 3, 4])) # List of length 24
  print(permute([0, 1, 2])) # List of length 6
  print(permute([])) # []
  print(permute([1, 2])) # [[2, 1], [1, 2]]