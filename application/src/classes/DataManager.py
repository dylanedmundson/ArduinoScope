import numpy as np

class DataManager:
    """ This class is responsible for managing data inputs to easily
        ouput the most recently entered data first (last in first out)
    """
    __BUFFER_DEFAULT_LENGTH = 1000
    __INIT_VALUE = -1
    
    def __init__(self):
        self.__time_buffer = np.full(self.__BUFFER_DEFAULT_LENGTH, self.__INIT_VALUE)
        self.__voltage_buffer = np.full(self.__BUFFER_DEFAULT_LENGTH, self.__INIT_VALUE)
        self.__voltage_buffer = self.__voltage_buffer.astype(np.float32)
        self.__pointer = -1 # initialize to buffer start
        self.__size = 0
    
    def add_data(self, time, voltage):
        """ adds oscilloscope time and voltage data to the manager
        
        Args:
            time_value (int): time data value in micro seconds
            voltage (float): voltage data value in volts
        """
        
        self.__pointer += 1
        if self.__pointer > self.__BUFFER_DEFAULT_LENGTH - 1:
            self.__pointer = 0
        
        self.__time_buffer[self.__pointer] = time
        self.__voltage_buffer[self.__pointer] = voltage
  
        
        self.__size += 1
        if self.__size > self.__BUFFER_DEFAULT_LENGTH:
            self.__size = self.__BUFFER_DEFAULT_LENGTH
    
    
    def clear_all(self):
        """ empties the entire array reinitializing to INIT_VALUE
        """
        for i in range(0, self.__BUFFER_DEFAULT_LENGTH -1):
            self.__voltage_buffer[i] = -1
        self.__size = 0
        self.__pointer = -1
    
    def pop(self):
        """ pops most recent value and removes from manager
        
            Returns:
                tuple: A tupple containing the time and voltage
                    - time (int): associated data time
                    - voltage (float): associated data voltage
                    
            Raises:
                ValueError in case of empty manager
        """
        if self.__size == 0:
            raise ValueError ("DataManager obj empty")
       
        voltage = self.__voltage_buffer[self.__pointer]
        time = self.__time_buffer[self.__pointer]
        
        self.__pointer -= 1
        self.__size -= 1
        
        if self.__size > 0 and self.__pointer < 0:
            self.__pointer = self.__BUFFER_DEFAULT_LENGTH - 1
        return time, voltage
    
    def data_waiting(self):
        """ returns the number of data points avaialable for popping

            Returns:
                size (int): number of data points available
        """
        return self.__size