import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def Test(self):
        name="Madhuban"
        upper=to_upper(name)
        self.assertEqual(upper,'MADHUBAN')

if __name__ == "__main__":
    unittest.main()