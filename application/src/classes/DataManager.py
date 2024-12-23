import numpy as np

class DataManager:
    """ This class is responsible for managing data inputs to easily
        ouput the most recently entered data first (last in first out)
    """
    __BUFFER_DEFAULT_LENGTH = 1000
    __INIT_VALUE = -1
    
    def __init__(self):
        self._time_buffer = np.full(self.__BUFFER_DEFAULT_LENGTH, self.__INIT_VALUE)
        self.__voltage_buffer = np.full(self.__BUFFER_DEFAULT_LENGTH, self.__INIT_VALUE)
        self.__pointer = 0 # initialize to buffer start
        self.__size = 0
    
    def add_data(self, time, voltage):
        """ adds oscilloscope time and voltage data to the manager
        
        Args:
            time_value (int): time data value in micro seconds
            voltage (float): voltage data value in volts
        """
        return
    
    
    def clear_all(self):
        """ empties the entire array reinitializing to INIT_VALUE
        """
        return
    
    def pop(self):
        """ pops most recent value and removes from manager
        
            Returns:
                tuple: A tupple containing the time and voltage
                    - time (int): associated data time
                    - voltage (float): associated data voltage
                    
            Raises:
                ValueError in case of empty manager
        """
        return -1, -1
    
    def data_waiting(self):
        """ returns the number of data points avaialable for popping

            Returns:
                size (int): number of data points available
        """
        return -1