from sortedcontainers import SortedSet
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_food = defaultdict(SortedSet)  # ->(rating , food)
        self.cuisines = {}  # ->(food -> cuisines)
        self.ratings = {}  # ->(food -> rating)
        for i in range(len(foods)):
            self.cuisine_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisines[food]
        r = self.ratings[food]
        self.cuisine_food[c].remove((-r, food))
        self.cuisine_food[c].add((-newRating, food))

        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food[cuisine][0][1]


x = FoodRatings(
    [
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    ]
)

print(x.highestRated("korean"))

x.changeRating("sushi", 16)
