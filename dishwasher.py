# Coded by Sezer Yavuzer Bozkır <admin@sezerbozkir.com>
# Date: 19.04.2017
"""
dish levels = low - medium - high
pollution levels = low - medium - high
dish type = delicate - mixed - strong
"""


class Machine:
    def __init__(self, dish_level, pollution, dish_type):
        self._dish_level = dish_level
        self._pollution = pollution
        self._dish_type = dish_type

        # main outputs
        self._wash_time = 95.0
        self._amount_of_detergent = 50.0
        self._temperature = 50.0
        self._upper_pump = 1400.0
        self._bottom_pump = 2800.0

        # fuzzy pieces
        self._coefficient_wash_time = 0.0
        self._coefficient_amount_of_detergent = 0.0
        self._coefficient_temperature = 0.0
        self._coefficient_upper_pump = 0.0
        self._coefficient_bottom_pump = 0.0

    def calculate_values(self):
        # dish level fuzzy rules
        if self._dish_level <= 35:
            self._coefficient_wash_time += self._dish_level * 0.0031
            self._coefficient_amount_of_detergent += self._dish_level * 0.0031
            self._coefficient_temperature += self._dish_level * 0.0031
            self._coefficient_upper_pump += self._dish_level * 0.0031
            self._coefficient_bottom_pump += self._dish_level * 0.0031

        if 85 >= self._dish_level > 15:
            if self._dish_level <= 35:
                self._coefficient_wash_time -= 0.007
                self._coefficient_amount_of_detergent -= self._dish_level * 0.014
                self._coefficient_temperature -= self._dish_level * 0.014
                self._coefficient_upper_pump -= self._dish_level * 0.014
                self._coefficient_bottom_pump = self._dish_level * 0.014
            self._coefficient_wash_time += self._dish_level * 0.014
            self._coefficient_amount_of_detergent += self._dish_level * 0.014
            self._coefficient_temperature += self._dish_level * 0.014
            self._coefficient_upper_pump += self._dish_level * 0.014
            self._coefficient_bottom_pump += self._dish_level * 0.014

        if 100 >= self._dish_level > 65:
            if self._dish_level <= 85:
                self._coefficient_wash_time -= self._dish_level * 0.014
                self._coefficient_amount_of_detergent -= self._dish_level * 0.014
                self._coefficient_temperature -= self._dish_level * 0.014
                self._coefficient_upper_pump -= self._dish_level * 0.014
                self._coefficient_bottom_pump -= self._dish_level * 0.014
            self._coefficient_wash_time += self._dish_level * 0.014
            self._coefficient_amount_of_detergent += self._dish_level * 0.014
            self._coefficient_temperature += self._dish_level * 0.014
            self._coefficient_upper_pump += self._dish_level * 0.014
            self._coefficient_bottom_pump += self._dish_level * 0.014

        # pollution fuzzy rules
        if self._pollution <= 35:
            self._coefficient_wash_time += self._pollution * 0.0031
            self._coefficient_amount_of_detergent += self._pollution * 0.0031
            self._coefficient_temperature += self._pollution * 0.0031
            self._coefficient_upper_pump += self._pollution * 0.0031
            self._coefficient_bottom_pump += self._pollution * 0.0031

        if 85 >= self._pollution > 15:
            if self._pollution <= 35:
                self._coefficient_wash_time -= 0.007
                self._coefficient_amount_of_detergent -= self._pollution * 0.014
                self._coefficient_temperature -= self._pollution * 0.014
                self._coefficient_upper_pump -= self._pollution * 0.014
                self._coefficient_bottom_pump = self._pollution * 0.014
            self._coefficient_wash_time += self._pollution * 0.014
            self._coefficient_amount_of_detergent += self._pollution * 0.014
            self._coefficient_temperature += self._pollution * 0.014
            self._coefficient_upper_pump += self._pollution * 0.014
            self._coefficient_bottom_pump += self._pollution * 0.014

        if 100 >= self._pollution > 65:
            if self._pollution <= 85:
                self._coefficient_wash_time -= self._pollution * 0.014
                self._coefficient_amount_of_detergent -= self._pollution * 0.014
                self._coefficient_temperature -= self._pollution * 0.014
                self._coefficient_upper_pump -= self._pollution * 0.014
                self._coefficient_bottom_pump -= self._pollution * 0.014
            self._coefficient_wash_time += self._pollution * 0.014
            self._coefficient_amount_of_detergent += self._pollution * 0.014
            self._coefficient_temperature += self._pollution * 0.014
            self._coefficient_upper_pump += self._pollution * 0.014
            self._coefficient_bottom_pump += self._pollution * 0.014

        # dish types fuzzy rules
        if self._dish_type <= 35:
            self._coefficient_wash_time += self._dish_type * 0.0031
            self._coefficient_amount_of_detergent += self._dish_type * 0.0031
            self._coefficient_temperature += self._dish_type * 0.0031
            self._coefficient_upper_pump += self._dish_type * 0.0031
            self._coefficient_bottom_pump += self._dish_type * 0.0031

        if 85 >= self._dish_type > 15:
            if self._dish_type <= 35:
                self._coefficient_wash_time -= 0.007
                self._coefficient_amount_of_detergent -= self._dish_type * 0.014
                self._coefficient_temperature -= self._dish_type * 0.014
                self._coefficient_upper_pump -= self._dish_type * 0.014
                self._coefficient_bottom_pump = self._dish_type * 0.014
            self._coefficient_wash_time += self._dish_type * 0.014
            self._coefficient_amount_of_detergent += self._dish_type * 0.014
            self._coefficient_temperature += self._dish_type * 0.014
            self._coefficient_upper_pump += self._dish_type * 0.014
            self._coefficient_bottom_pump += self._dish_type * 0.014

        if 100 >= self._dish_type > 65:
            if self._dish_type <= 85:
                self._coefficient_wash_time -= self._dish_type * 0.014
                self._coefficient_amount_of_detergent -= self._dish_type * 0.014
                self._coefficient_temperature -= self._dish_type * 0.014
                self._coefficient_upper_pump -= self._dish_type * 0.014
                self._coefficient_bottom_pump -= self._dish_type * 0.014
            self._coefficient_wash_time += self._dish_type * 0.014
            self._coefficient_amount_of_detergent += self._dish_type * 0.014
            self._coefficient_temperature += self._dish_type * 0.014
            self._coefficient_upper_pump += self._dish_type * 0.014
            self._coefficient_bottom_pump += self._dish_type * 0.014

        self._wash_time *= self._coefficient_wash_time
        self._amount_of_detergent *= self._coefficient_amount_of_detergent
        self._temperature *= self._coefficient_temperature
        self._upper_pump *= self._coefficient_upper_pump
        self._bottom_pump *= self._coefficient_bottom_pump

        return {"Wash time": self._wash_time,
                "Amount of detergent": self._amount_of_detergent,
                "Temperature": self._temperature,
                "Upper pump speed": self._upper_pump,
                "Bottom pump speed": self._bottom_pump}
