# This file should contain the main process, data --> outputs

# Libraries and environment variables
from src.utilities import load
from src.utilities import helpers
from src.utilities import parameters

# Processing class
class ProcessingClass():
    """
    Data processing class.
    The aim of this class.
    """
    def __init__(self, **kwargs):
        self.args = kwargs

        self.data = load.DataClass()

        self.processed_data = self.processing_function()

    def __repr__(self) -> str:
        return f"ProcessingClass(arguments = {self.args})"
    
    # Processing functions
    def processing_function(self, **kwargs):
        """
        Function to load all data

        Attributes
        ----------
        - 

        Data attributes
        ----------
        - 

        Parameters
        ----------
        - 

        Process
        ----------
        - 

        Outputs
        ----------
        - 
        """
        pass