# compressor.py

class CompressorModel:
    """
    Class for modeling compressor behavior.
    """

    @staticmethod
    def calculate_total_enthalpy_out(ht_in, ht_out_ideal, eff):
        """
        Calculate the total enthalpy at the outlet of the compressor.

        Parameters:
        - ht_in (float): Total enthalpy at the inlet of the compressor.
        - ht_out_ideal (float): Ideal total enthalpy at the outlet of the compressor.
        - eff (float): Efficiency of the compressor.

        Returns:
        - float: Total enthalpy at the outlet of the compressor.
        """
        ht_out = ht_in + (ht_out_ideal - ht_in) / eff
        return ht_out
