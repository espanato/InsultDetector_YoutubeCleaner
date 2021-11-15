from carbonai import PowerMeter
from random import randrange

project_name = 'projet test'
program_name = 'increment'

power_meter = PowerMeter(project_name = "test")



l_test = [random.randrange(10) for _ in range(100)]

with power_meter(
  package="sklearn",
  algorithm="incrementation",
  data_type="tabular",
  data_shape=100,
  algorithm_params="l = l_test",
  comments=""
): 
def increment(l):
    return [x+1 for x in l]



power_meter = PowerMeter()