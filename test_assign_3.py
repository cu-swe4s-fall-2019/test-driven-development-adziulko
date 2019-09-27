import unittest
import random
import statistics
import math
import math_lib



class TestMathLib(unittest.TestCase):

    def test_list_mean_empty_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_empty_list_2(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)

    def test_list_mean_constants(self):
        r = math_lib.list_mean([1, 1, 1, 1, 1])
        self.assertEqual(r, 1)

    def test_list_mean_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertAlmostEqual(r, e)

    def test_list_mean_rand_floats_model(self):
        L = []
        u = (0 + 100)/ 2.0
        for i in range(100):
            for j in range(10):
                L.append(random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, u, rel_tol = 10.0, abs_tol = 0.0))

    def test_list_stdev_empty_list(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)

    def test_list_stdev_empty_list_2(self):
        r = math_lib.list_stdev([])
        self.assertEqual(r, None)

    def test_list_stdev_rand_floats_model(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.uniform(0, 100))
            r = math_lib.list_stdev(L)
            e = statistics.stdev(L)
            self.assertTrue(math.isclose(r, e))





if __name__ == '__main__':
    unittest.main()
