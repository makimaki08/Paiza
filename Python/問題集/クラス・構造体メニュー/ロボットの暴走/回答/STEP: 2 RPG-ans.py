class Hero:
    def __init__(self, lv, hp, at, df, sp, cl, ft):
        self.lv = lv
        self.hp = hp
        self.at = at
        self.df = df
        self.sp = sp
        self.cl = cl
        self.ft = ft

    def levelup(self, hp, at, df, sp, cl, ft):
        self.lv += 1
        self.hp += hp
        self.at += at
        self.df += df
        self.sp += sp
        self.cl += cl
        self.ft += ft

    def muscle_training(self, hp, at):
        self.hp += hp
        self.at += at

    def running(self, df, sp):
        self.df += df
        self.sp += sp

    def study(self, cl):
        self.cl += cl

    def pray(self, ft):
        self.ft += ft

    def print(self):
        print(self.lv, self.hp, self.at, self.df, self.sp, self.cl, self.ft)


n, k = [int(x) for x in input().split()]

heroes = [None] * n
for i in range(n):
    lv, hp, at, df, sp, cl, ft = [int(x) for x in input().split()]
    heroes[i] = Hero(lv, hp, at, df, sp, cl, ft)

for _ in range(k):
    values = input().split()

    index = int(values.pop(0)) - 1
    event = values.pop(0)

    if event == "levelup":
        hp, at, df, sp, cl, ft = [int(x) for x in values]
        heroes[index].levelup(hp, at, df, sp, cl, ft)
    elif event == "muscle_training":
        hp, at = [int(x) for x in values]
        heroes[index].muscle_training(hp, at)
    elif event == "running":
        df, sp = [int(x) for x in values]
        heroes[index].running(df, sp)
    elif event == "study":
        cl = int(values[0])
        heroes[index].study(cl)
    else:
        ft = int(values[0])
        heroes[index].pray(ft)

for hero in heroes:
    hero.print()