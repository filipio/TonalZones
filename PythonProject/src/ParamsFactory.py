from FiltersEnum import Filter
class ParamsFactory:
    """class that returns data from gui"""
    def __init__(self,gui):
        self.gui=gui
    def get_fparams(self,filter_name):
        """return params to given filter"""
        if filter_name==Filter.AVARAGING:
            return {'ksize':(self.gui.avaraging_kernel_size.value(),1)}


    def set_mask_params(self, m_min, m_max):
        self.gui.min_slider.setValue(m_min)
        self.gui.max_slider.setValue(m_max)
        self.gui.min_label.setText(str(m_min))
        self.gui.max_label.setText(str(m_max))