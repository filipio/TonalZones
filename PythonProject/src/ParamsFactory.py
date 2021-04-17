from FiltersEnum import Filter
class ParamsFactory:
    """class that returns data from gui"""
    def __init__(self,gui):
        self.gui=gui
    def get_fparams(self,filter_name):
        """return params to given filter"""
        if filter_name==Filter.AVARAGING:
            return {'ksize':(self.gui.avaraging_kernel_size.value(),1)}
