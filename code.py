import random
from gurobipy import *


def get_item_vars(model, item, num_items):
  return [model.getVarByName(str(item) + "_" + str(i)) for i in range(num_items)]

def get_bin_vars(model, binn, num_items):
  return [model.getVarByName(str(i) + "_" + str(binn)) for i in range(num_items)]

def get_bin_vars_multiplied_by_item_weights(model, binn, items, num_items):
  return [model.getVarByName(str(i) + "_" + str(binn)) * items[i] for i in range(num_items)]


def optimum(items, capacity):
  env = Env(empty=True)
  env.setParam("OutputFlag",0)
  env.start()

  int_prog_model = Model(env=env)

  obj =  0

  # initiating variables
  for item in range(len(items)):
    for binn in range(len(items)):
      int_prog_model.addVar(vtype=GRB.BINARY, name = str(item)+"_"+str(binn))
  
  int_prog_model.update()
  
  for item in range(len(items)):
    int_prog_model.addConstr(sum(get_item_vars(int_prog_model, item, len(items))) == 1)
  
  bin_vars = []
  for binn in range(len(items)):
    bin_is_used_var = int_prog_model.addVar(vtype=GRB.BINARY, name = str(binn)+"_is_used")
    bin_vars.append(bin_is_used_var)
    obj += bin_is_used_var
    int_prog_model.addConstr(sum(get_bin_vars_multiplied_by_item_weights(\
      int_prog_model, binn, items, len(items))) <= capacity * bin_is_used_var)
    

  num_bins_used = sum(bin_vars)
  int_prog_model.setObjectiveN(num_bins_used, GRB.MINIMIZE)
  int_prog_model.optimize()

  return int(sum([x.X for x in bin_vars]))


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
    else:
      bins.append(item)
    
  return len(bins)

def return_random_dataset(num_items):
  items = [random.randint(1,20) for i in range(num_items)]
  capacity = 30
  return items, capacity

##################### testing #####################
def run_tests(num_tests):
  
  for i in range(num_tests):
    num_items = i * 300 + 20
    items, capacity =  return_random_dataset(num_items)
    print("number of items:", num_items)
    print("random test %d: optimum %d, first fit %d, first fit descending %d, best fit %d, best fit descending %d" % \
      (i, optimum(items,capacity), first_fit(items, capacity), first_fit_desc(items, capacity), best_fit(items, capacity), best_fit_desc(items, capacity)))

run_tests(10)




items_ex1 = [5,3,7,9,12,2,4,4]
capacity_ex1 = 15

items_ex2 = [5,3,7,9,12,2,4,4,13]
capacity_ex2 = 15

# 
# print("1st example")
# print(first_fit(items_ex1, capacity_ex1))
# print(first_fit_desc(items_ex1, capacity_ex1))
# print(best_fit(items_ex1, capacity_ex1))
# print(best_fit_desc(items_ex1, capacity_ex1))
# print("2nd example")
# print(first_fit(items_ex2, capacity_ex2))
# print(first_fit_desc(items_ex2, capacity_ex2))
# print(best_fit(items_ex2, capacity_ex2))
# print(best_fit_desc(items_ex2, capacity_ex2))
