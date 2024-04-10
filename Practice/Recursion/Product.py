def product(array, result, builder, index):
	"""Return all possibilities"""
  if len(builder) >= len(array):
      result.append(builder)
      return
  if index >= len(array):
    return
  _permute(array, result, builder.copy(), index+1)
  builder.append(array[index])
  _permute(array, result, builder.copy(), index)
  return result