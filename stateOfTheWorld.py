import random


class World(object):
    naturalResources = 0
    naturalResourcesExtractionRate = 0
    population = 0
    income = 0
    outgoings = 0
    foreignAid = 0
    publicGoods = 0
    publicOpinion = 0
    taxes = 0
    averageSalary = 0
    influentialSize = 0
    treasury = 0
    embezzlement = 0

    def __init__(
            self,
            natural_resources,
            natural_resources_extraction_rate,
            population,
            foreign_aid,
            public_goods,
            public_opinion_noise,
            taxes,
            average_salary,
            coalition_size,
            treasury,
            embezzlement
    ):
        self.naturalResources = natural_resources
        self.naturalResourcesExtractionRate = natural_resources_extraction_rate
        self.population = population
        self.income = population * taxes * average_salary
        self.outgoings = public_goods * population * average_salary + embezzlement
        self.foreignAid = foreign_aid
        self.publicGoods = public_goods
        temp_public_opinion = public_goods - taxes + public_opinion_noise
        if temp_public_opinion < -1:
            self.publicOpinion = -1
        elif temp_public_opinion > 1:
            self.publicOpinion = 1
        else:
            self.publicOpinion = temp_public_opinion
        self.taxes = taxes
        self.averageSalary = average_salary
        self.influentialSize = coalition_size
        self.treasury = treasury
        self.embezzlement = embezzlement

    def print_world_state(self):
        print("Natural Resources: {0}\n"
              "Natural Resources Extraction Rate: {1}\n"
              "Population: {2}\n"
              "Income: {3}\n"
              "Outgoings: {4}\n"
              "Foreign Aid: {5}\n"
              "Public Goods: {6}\n"
              "Public Opinion: {7}\n"
              "Taxes: {8}\n"
              "Average Salary: {9}\n"
              "Coalition Size: {10}\n"
              "Treasury: {11}\n"
              "Embezzlement: {12}"
              .format(self.naturalResources,
                      self.naturalResourcesExtractionRate,
                      self.population,
                      self.income,
                      self.outgoings,
                      self.foreignAid,
                      self.publicGoods,
                      self.publicOpinion,
                      self.taxes,
                      self.averageSalary,
                      self.influentialSize,
                      self.treasury,
                      self.embezzlement,
                      ))


def make_world():
    natural_resources = random.gauss(100000000, 50000000)
    if natural_resources < 0:
        natural_resources = 0
    natural_resources_extraction_rate = random.random()
    population = random.randint(200000, 500000000)
    foreign_aid = random.randint(0, 1000000000)
    public_goods = random.random()
    public_opinion_noise = random.gauss(0, 0.05)
    taxes = random.random()
    average_salary = random.randint(1, 40000)
    coalition_size = random.randint(3, 100)
    treasury = random.gauss(0, 1000000000)
    embezzlement = random.gauss(20000, 10000)
    world = World(
        natural_resources,
        natural_resources_extraction_rate,
        population,
        foreign_aid,
        public_goods,
        public_opinion_noise,
        taxes,
        average_salary,
        coalition_size,
        treasury,
        embezzlement
    )
    return world
