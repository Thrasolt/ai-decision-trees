import unittest
from data_mod.Datapoint import Datapoint


class DatapointTest(unittest.TestCase):

    def testCall(self):
        bla = Datapoint(0.5,0.5,1,1,0,0.5,0.5)
        self.assertEqual(bla(), "0.5,0.5,1,1,0,0.5,0.5,"+str(bla.success))


if __name__ == '__main__':
    unittest.main()
