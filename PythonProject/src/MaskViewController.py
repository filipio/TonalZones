class MaskViewController:
    """class that sets the data associated with masks."""
    def __init__(self,gui):
        self.gui=gui
    def set_range_mask_params(self, m_min, m_max, m_tol):
        if m_min == None:
            m_min = 0
        if m_max == None:
            m_max = 0
        self.gui.mask_min_slider.setValue(m_min)
        self.gui.mask_max_slider.setValue(m_max)
        self.gui.mask_tolerance_slider.setValue(m_tol)
        self.gui.mask_min_label.setText(str(m_min))
        self.gui.mask_max_label.setText(str(m_max))
        self.gui.mask_tolerance_label.setText(str(m_tol))

    def set_pixel_mask_params(self, m_tol):
        self.gui.pixel_tolerance_slider.setValue(m_tol)
        self.gui.pixel_tolerance_label.setText(str(m_tol))

    def set_data_from_mask(self, mask):
        self.set_range_mask_params(mask.slider_min, mask.slider_max, mask.slider_tol)
        self.set_pixel_mask_params(mask.pixels_tol)