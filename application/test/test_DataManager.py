import unittest
import sys

sys.path.append('C:/Users/dylan/VsCodeRepos/ArduinoScope/application')

import src.classes.DataManager as data_mngr

MAX_BUFFER = data_mngr.DataManager._DataManager__BUFFER_DEFAULT_LENGTH

class TestDataManager(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    
    def assert_add_pop_match(self, t_input, v_input, mngr):
        """ assertion to confirm most resent data add/pop
            function work properly
            Args: 
                t (int): time value
                v (float): voltage value
                mngr (data_mngr.DataManager): data manager
        """
        if (isinstance(mngr, data_mngr.DataManager)):
            mngr.add_data(t_input, v_input)
            t, v = mngr.pop()
            self.assertEqual(t, t_input)
            self.assertEqual(v, v_input)
        else:
            print("Test code error - assert_add_pop_match")
    
    def test_add_data_and_pop(self):
        
        mnger = data_mngr.DataManager()
        
        # test negative time when empty
        try:
            mnger.pop()
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        
        self.assert_add_pop_match(100, 5.0, mnger)
        
        # test filling buffer to maximum
        fail_flag = False
        for i in range(0, MAX_BUFFER):
            mnger.add_data(i, 5.0)
        
        # test proper pointer adjustment and pop/add 
        # functionality-full buffer
        mnger.add_data(10285, 2.5)
        self.assertEqual(mnger.__pointer, 0)
        t, v = mnger.pop()
        self.assertEqual(t, 10285)
        self.assertEqual(v, 2.5)
        
        # test poping buffer empty
        for i in range(MAX_BUFFER, 0):
            t, v = mnger.pop()
            if not t == i:
                fail_flag = True
        self.assertFalse(fail_flag)

    
    def clear_all_assisstant(self, mngr):
        """ assists test_clear_all function to make sure
            proper functionallity after clearing
        """
        if (isinstance(mngr, data_mngr.DataManager)):
            mngr.clear_all()
            self.assertEqual(mngr.data_waiting(), 0)
            try:
                t,v = mngr.pop()
                self.assertFalse(True)
            except ValueError:
                self.assertTrue(True)
        else:
            print("Test code error - test_clear_all_assisstant")
        
    def test_clear_all(self):
        mnger = data_mngr.DataManager()

        # clear all on empty
        self.clear_all_assisstant(mngr=mnger)
        
        #fill completely
        for i in range(0, MAX_BUFFER):
            mnger.add_data(i, 5.0)
        self.clear_all_assisstant(mngr=mnger)
        
        # fill one over max length
        for i in range(0, MAX_BUFFER + 1):
            mnger.add_data(i, 5.0)
        self.clear_all_assisstant(mngr=mnger)
    
    def test_data_waiting(self):
        mnger = data_mngr.DataManager()
        mnger.__init__()
        
        # test zero at init
        self.assertEqual(mnger.data_waiting(), 0)
        
        # test increments with filling
        for i in range(0, MAX_BUFFER):
            mnger.add_data(1, 1)
            self.assertEqual(mnger.data_waiting(), i + 1)
        
        # test does not increase past buffer max
        mnger.add_data(1, 1)
        self.assertEqual(mnger.data_waiting(), MAX_BUFFER)
        
        # test returns to zero when cleared
        mnger.clear_all()
        self.assertEqual(mnger.data_waiting(), 0)
            
        
if __name__ == '__main__':
    unittest.main()