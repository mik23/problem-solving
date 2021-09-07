from unittest import TestCase
import math
from geometry.Pi import pi_approx

class Test(TestCase):
    def test_approx_pi(self):
        pi = pi_approx(10000000)
        print(pi)

        self.assertTrue(abs(pi - math.pi) < 0.01)
