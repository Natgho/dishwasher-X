# Coded by Sezer Yavuzer Bozkır <admin@sezerbozkir.com>
# Date: 19.04.2017

"""
inputs:
Amount of dish
Degree of pollution
Dish Type

outputs:
wash time
amount of detergent
water temperature
Upper basket pump speed
Bottom basket pump speed
"""

from dishwasher import Machine

amount_of_dish = 50
degree_of_pollution = 80
dish_type = 20

sample_machine = Machine(amount_of_dish, degree_of_pollution, dish_type)
results = sample_machine.calculate_values()
for key, value in results.items():
    print(key, value)
