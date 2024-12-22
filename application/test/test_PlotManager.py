import unittest
import sys

sys.path.append('C:/Users/dylan/VsCodeRepos/ArduinoScope/application')

from src.classes.DataManager import test1

class TestPlotManager(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
        
        
if __name__ == '__main__':
    unittest.main()