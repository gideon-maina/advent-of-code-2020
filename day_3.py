# coding: utf-8
def toboggan_trajectory(geology: list, down_steps: int, right_steps: int):
    width = len(geology[0])
    trees = 0
    row = down_steps
    column = right_steps

    while row < len(geology):
        if geology[row][column] == "#":
            trees += 1
        row += down_steps
        column = (column + right_steps) % width
    return trees


input_date = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]
