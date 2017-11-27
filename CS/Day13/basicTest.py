import unittest
class TestWhatever(unittest.TestCase):
  def setUp(self):
    self.thing = 1
  def test_first_thing(self):
    self.assertEqual(self.thing,1)
  def tearDown(self):
    self.thing = None

if __name__ == '__main__':
    unittest.main()