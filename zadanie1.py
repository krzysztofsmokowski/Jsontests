import argparse
import pprint
import json


class Printer(object):
    def __init__(self):
        self.json_data = self.get_json_data()

    def get_json_data(self):
        with open('dane1.json') as data_file:
            return json.load(data_file)
#print(data)

    def region_printer(self):
        for dat in self.json_data["results"]:
            print(dat["address_components"][3]["long_name"])
    
    def street_name(self):
        for dat in self.json_data["results"]:
            print(dat["address_components"][1]["long_name"]+" "+dat["address_components"][0]["long_name"])

    def data_types(self):
        for dat in self.json_data["results"][0]["address_components"]:
            print(dat["types"])

    def typ(self, word):
        arr = []
        for dat in self.json_data["results"][0]["address_components"]:
            if word in dat["types"]:
                arr.append(dat["long_name"])
        print(arr)

    def to_json(self, typ):
        #Po podaniu przez uzytkownika np: --type='route' --get_json program wyprintuje jsona zawierajacego short_name i typy dla tego typu w formie, przykladowo:
        #[{"typy":["route"],"krotka_nazwa":"Strzegomska"}]
        types_and_names =[]
        for dat in self.json_data["results"][0]["address_components"]:
            if typ in dat["types"]:
                types_and_names.append(({"typy: ": dat["types"], "krotka nazwa: ": dat["short_name"]}))
        print(types_and_names)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", action ="store_true", help="printing region of city")
    parser.add_argument("--street_name", action="store_true", help="printing street name")
    parser.add_argument("--types",action="store_true",help="printing types")
    parser.add_argument("--typ", help = "returning type")
    parser.add_argument("--get_json", action="store_true", help="making json out of typ data")
    args = parser.parse_args()
    printer = Printer()
    if args.region:
        what_to_print = printer.region_printer()
    if args.street_name:
        what_to_print = printer.street_name()
    if args.types:
        what_to_print = printer.data_types()
    if args.get_json and args.typ:
        what_to_print = printer.to_json(args.typ)
    elif args.typ:
        what_to_print = printer.typ(args.typ)
if __name__ == '__main__':
    main()
