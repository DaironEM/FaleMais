# coding=utf-8

class TalkMore:
    relation_origin_destination = [('011', '016', 1.90),
                                   ('016', '011', 2.90),
                                   ('011', '017', 1.70),
                                   ('017', '011', 2.70),
                                   ('011', '018', 0.90),
                                   ('018', '011', 1.90)]

    tolerancia_planos = {'FaleMais 30': 30, 'FaleMais 60': 60, 'FaleMais 120': 120}

    def __init__(self, origin, destination, length, plan):
        self.__tariff = None
        self.__origin = origin
        self.__destination = destination
        self.__length = length
        self.__plan = plan
        self.cost_per_minute()

    @property
    def tariff(self):
        return self.__tariff

    def free_time_for_plan(self):
        return self.tolerancia_planos[self.__plan]

    def cost_per_minute(self):
        for relation in self.relation_origin_destination:
            if relation[0] == self.__origin and relation[1] == self.__destination:
                self.__tariff = relation[2]

    #If tariff is None then return False
    def is_valid_call(self):
        return not(self.__tariff == None)


    def cost_time_without_plan(self):
        return self.__tariff * self.__length

    def cost_time_with_plan(self, free_time):
        return (self.__tariff * 1.10) * (self.__length - free_time)

    def is_call_goin_cost(self, free_time):
        return free_time <= self.__length

    def cost_of_call_with_plan(self):
        if self.is_valid_call():
            final_cost =  self.cost_of_valid_call_with_plan()
        else:
            final_cost = '-'
        return final_cost

    def cost_of_valid_call_with_plan(self):
        free_time = self.free_time_for_plan()
        if self.is_call_goin_cost(free_time):
            final_cost_valid_call = self.format_final_cost(self.cost_time_with_plan(free_time))
        else:
            final_cost_valid_call = '$ 0.00'
        return final_cost_valid_call

    def cost_of_call_without_plan(self):
        if self.is_valid_call():
            final_cost = self.format_final_cost(self.cost_time_without_plan())
        else:
            final_cost = '-'
        return final_cost

    def format_final_cost(self, cost):
        return "$ {:.2f}".format(cost)
