# unit_conversions.py

class UnitConversions:
    @staticmethod
    def C_to_K(C):
        """
        Convert Celsius (°C) to Kelvin (K).
        """
        return C + 273.15

    @staticmethod
    def F_to_K(F):
        """
        Convert Fahrenheit (°F) to Kelvin (K).
        """
        return (F - 32) * 5 / 9 + 273.15

    @staticmethod
    def Pa_to_kPa(Pa):
        """
        Convert Pascals (Pa) to kilopascals (kPa).
        """
        return Pa / 1000

    @staticmethod
    def atm_to_kPa(atm):
        """
        Convert atmospheres (atm) to kilopascals (kPa).
        """
        return atm * 101.325
    
    @staticmethod
    def psia_to_Pa(psia):
        """
        Convert pounds per square inch absolute (psia) to Pascals (Pa).
        """
        return psia * 6894.76

    @staticmethod
    def Pa_to_psia(Pa):
        """
        Convert Pascals (Pa) to pounds per square inch absolute (psia).
        """
        return Pa / 6894.76

    @staticmethod
    def N_to_lbf(N):
        """
        Convert Newtons (N) to pounds-force (lbf).
        """
        return N * 0.224809

    @staticmethod
    def lbf_to_N(lbf):
        """
        Convert pounds-force (lbf) to Newtons (N).
        """
        return lbf / 0.224809

    @staticmethod
    def BTU_to_J(BTU):
        """
        Convert British Thermal Units (BTU) to Joules (J).
        """
        return BTU * 1055.06

    @staticmethod
    def J_to_BTU(J):
        """
        Convert Joules (J) to British Thermal Units (BTU).
        """
        return J * 0.000947817

    @staticmethod
    def lbhr_to_kgs(lbhr):
        """
        Convert pounds per hour (lb/hr) to kilograms per second (kg/s).
        """
        return lbhr * 4.53592e-4

    @staticmethod
    def kgs_to_lbhr(kgs):
        """
        Convert kilograms per second (kg/s) to pounds per hour (lb/hr).
        """
        return kgs * 2204.62

    @staticmethod
    def K_to_C(K):
        """
        Convert Kelvin (K) to Celsius (°C).
        """
        return K - 273.15

    @staticmethod
    def R_to_K(R):
        """
        Convert degrees Rankine (°R) to Kelvin (K).
        """
        return R * 5 / 9
    
    @staticmethod
    def meters_to_km(m):
        """
        Convert meters (m) to kilometers (km).
        """
        return m / 1000.0
    
    @staticmethod
    def meters_to_feet(m):
        """
        Convert meters (m) to feet (ft).
        """
        return m * 3.2808399
    
    @staticmethod
    def feet_to_meters(f):
        """
        Convert feet (ft) to meters (m).
        """
        return f / 3.2808399
    
    @staticmethod
    def feet_to_km(f):
        """
        Convert feet (ft) to kilometers (km).
        """
        return UnitConversions.feet_to_meters(f) / 1000.0
