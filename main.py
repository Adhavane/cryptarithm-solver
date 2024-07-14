from cripthmik.solve import GenerateAndTest
from cripthmik.utils import Cryptarithm

cryptarithm = Cryptarithm("SEND + MORE = MONEY")
cryptarithm = Cryptarithm("ODD + ODD = EVEN")


solver = GenerateAndTest()
# print(solver._all_digits(cryptarithm))
# print(solver._all_diff(cryptarithm))
# print(solver._all_diff(cryptarithm))
# print(solver._generate(cryptarithm, allow_zero=False, allow_leading_zero=True))
# print(solver._test(cryptarithm))
# print(solver._query(cryptarithm))
print(next(solver.solve(cryptarithm)))
