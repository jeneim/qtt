import numpy as np

from qtt.instrument_drivers.virtual_awg.setting import Setting
from qtt.instrument_drivers.virtual_awg.awgs.common import AwgCommon, AwgCommonError


class KeysightM3202A_AWG(AwgCommon):

    def __init__(self, awg):
        super('M3202A', channels=[1, 2, 3, 4], markers=[1])
        if type(awg).__name__ is not self._awg_name:
            raise AwgCommonError('The AWG does not correspond with {}'.format(self._awg_name))
        self.__settings = {'sampling_rate': Setting('GS/s', 1.0e9, 1.0e7, 1.2e9),
                           'marker_delay': Setting('ns', 0.0, 0.0, 1.0),
                           'marker_low': Setting('V', 0.0, -1.0, 2.6),
                           'marker_high': Setting('V', 1.0, -0.9, 2.7),
                           'amplitudes': Setting('V', 1.0, 0.02, 4.5),
                           'offset': Setting('V', 0, -2.25, 2.25)}
        self.__awg = awg
        self.update_settings()

    @property
    def get(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def enable_outputs(self, channels=None):
        raise NotImplementedError

    def disable_outputs(self, channels=None):
        raise NotImplementedError

    def change_setting(self, setting, value):
        raise NotImplementedError

    def update_settings(self):
        raise NotImplementedError

    def set_mode(self, mode):
        raise NotImplementedError

    def get_mode(self):
        raise NotImplementedError

    def set_sampling_rate(self, sampling_rate):
        raise NotImplementedError

    def get_sampling_rate(self, sampling_rate):
        raise NotImplementedError

    def set_gain(self, gain):
        raise NotImplementedError

    def get_gain(self):
        raise NotImplementedError

    def set_sequence(self, channel, sequence):
        raise NotImplementedError

    def get_sequence(self, channel):
        raise NotImplementedError

    def upload_waveforms(self, names, waveforms):
        raise NotImplementedError

    def delete_waveforms(self):
        raise NotImplementedError