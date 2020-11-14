import json

# dict = {1: {"cod1": '011', "cod2": '016', "tariff": 1.90},
#         2: {"cod1": '016', "cod2": '011', "tariff": 2.90},
#         3: {"cod1": '011', "cod2": '017', "tariff": 1.70},
#         4: {"cod1": '017', "cod2": '011', "tariff": 2.70},
#         5: {"cod1": '011', "cod2": '018', "tariff": 0.90},
#         6: {"cod1": '018', "cod2": '011', "tariff": 1.90}
#         }

class RelationOriginDestination():

        def __init__(self):
                self.relation_origin_destination = self.file_to_jason()

        def file_to_jason(self):
                file = open("Files/relation.txt", "r+")
                new_jason = None
                for line in file:
                        new_jason = line
                return json.loads(new_jason)



print(RelationOriginDestination().relation_origin_destination)



