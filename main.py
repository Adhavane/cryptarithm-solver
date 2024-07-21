from cripthmik.solve import GenerateAndTest, Enumerate
from cripthmik.utils import Cryptarithm

cryptarithm = Cryptarithm("SEND + MORE = MONEY")
cryptarithm = Cryptarithm("ODD + ODD = EVEN")

if __name__ == "__main__":
    # solver = GenerateAndTest()
    # print(solver._all_digits(cryptarithm))
    # print(solver._all_diff(cryptarithm))
    # print(solver._all_diff(cryptarithm))
    # print(solver._generate(cryptarithm, allow_zero=False, allow_leading_zero=True))
    # print(solver._test(cryptarithm))
    # print(solver._query(cryptarithm))
    # gen = solver.solve(cryptarithm)
    # print(next(solver.solve(cryptarithm)))
    # print(next(gen))
    # print(next(gen))
    # print(next(solver.solve(cryptarithm)))
    # print(next(solver.solve(cryptarithm)))
    # print(next(solver.solve(cryptarithm)))

    solver2 = Enumerate()
    gen = solver2.solve(cryptarithm)
    print(next(gen))
    print(next(gen))
    print(next(gen))
