def first_fit(items, capacity):
  bins = [] # current capacities
  for item in items:
    added = False
    for bin_index in range(len(bins)):
      if bins[bin_index] + item <= capacity:
        bins[bin_index] += item
        added = True
        break
    if (not added):
      if item < capacity:
        bins.append(item)
    
  return len(bins)


def first_fit_desc(items, capacity):
  items_copy = items.copy()
  items_copy.sort(reverse = True)
  bins = [] # current capacities
  for item in items_copy:
    added = False
    for bin_index in range(len(bins)):
      if bins[bin_index] + item <= capacity:
        bins[bin_index] += item
        added = True
        break
    if (not added):
      if item < capacity:
        bins.append(item)
    
  return len(bins)



def best_fit(items, capacity):
  bins = [] # current capacities
  for item in items:
    fits = False
    bestBin = len(items)
    for bin_index in range(len(bins)):
      if bins[bin_index] + item <= capacity:
        if not fits:
          bestBin = bin_index
        fits = True
        if bins[bin_index] >= bins[bestBin]:
          bestBin = bin_index
    if bestBin != len(items):
      bins[bestBin] += item
    else:
      bins.append(item)
    
  return len(bins)


def best_fit_desc(items, capacity):
  bins = [] # current capacities
  items_copy = items.copy()
  items_copy.sort(reverse=True)
  for item in items_copy:
    fits = False
    bestBin = len(items)
    for bin_index in range(len(bins)):
      if bins[bin_index] + item <= capacity:
        if not fits:
          bestBin = bin_index
        fits = True
        if bins[bin_index] >= bins[bestBin]:
          bestBin = bin_index
    if bestBin != len(items):
      bins[bestBin] += item
      print(bins)
    else:
      bins.append(item)
      print(bins)
    
  return len(bins)




items_ex1 = [5,3,7,9,12,2,4,4]
capacity_ex1 = 15

items_ex2 = [5,3,7,9,12,2,4,4,13]
capacity_ex2 = 15


print("1st example")
print(first_fit(items_ex1, capacity_ex1))
print(first_fit_desc(items_ex1, capacity_ex1))
print(best_fit(items_ex1, capacity_ex1))
print(best_fit_desc(items_ex1, capacity_ex1))
print("2nd example")
print(first_fit(items_ex2, capacity_ex2))
print(first_fit_desc(items_ex2, capacity_ex2))
print(best_fit(items_ex2, capacity_ex2))
print(best_fit_desc(items_ex2, capacity_ex2))
