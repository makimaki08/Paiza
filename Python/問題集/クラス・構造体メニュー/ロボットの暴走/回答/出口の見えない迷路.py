class Point:
    def __init__(self, keyword, path_a, path_b):
        self.keyword = keyword
        self.path_a = path_a
        self.path_b = path_b

    def get_keyword(self):
        return self.keyword

    def get_path(self, direction):
        if direction == 1:
            return self.path_a
        else:
            return self.path_b


n, k, s = [int(x) for x in input().split()]

maze = [None] * n
for i in range(n):
    values = input().split()

    keyword = values[0]
    path_a = int(values[1]) - 1
    path_b = int(values[2]) - 1

    maze[i] = Point(keyword, path_a, path_b)

now_point = maze[s-1]
ans = now_point.get_keyword()
for _ in range(k):
    direction = int(input())

    to = now_point.get_path(direction)
    now_point = maze[to]
    ans += now_point.get_keyword()

print(ans)