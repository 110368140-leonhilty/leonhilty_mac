class Scoop:
    def __init__(self,flavor):
        self.flavor = flavor

class Scoop_Maker:
    def create(self,flavors):
        return [Scoop(flavor) for flavor in flavors]

class Bowl():
    def __init__(self):
        self.scoops =[]
    def add_scoop(self,*new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)
    def flavors(self):
        return '/'.join(scoop.flavor for scoop in self.scoops)
    def __str__(self) -> str:
        flavors = '/'.join(scoop.flavor for scoop in self.scoops)
        return f'冰淇淋碗口味：{flavors}'


scoop_maker = Scoop_Maker()
scoops = scoop_maker.create(['巧克力','香草','薄荷'])

bowl = Bowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))
print(bowl)
# for scoop in scoops:
#     print(scoop,scoop.flavor)

