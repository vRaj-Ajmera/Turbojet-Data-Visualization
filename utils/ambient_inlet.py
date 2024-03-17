# ambient_inlet.py

class AmbientInletModel:

    # isentropic efficiency of the diffuser eta_d
    def findIsEff_RatioMethod(tau_r, pi_d, gamma):
        numerator = ((tau_r * pi_d) ** ((gamma - 1)/gamma)) - 1
        denominator = tau_r - 1
        return numerator/denominator

    def findIsEff_EnthMethod(h_t2s, h_t0, h_0):
        numerator = h_t2s - h_0
        denominator = h_t0 - h_0
        return numerator/denomincator

    def findIsEff_TempMethod(T_t2s, T_t0, T_0):
        numerator = T_t2s - T_0
        denominator = T_t0 - T_0
        return numerator/denomincator

    # Finding the total pressure ratio pi_d
    def findPRessureRatio(M_0, pi_dmax):
        if M_0 <= 1:
            return 1 * pi_dmax
        elif M_0 > 1 and M_0 < 5:
            eta_r = 1 - (0.075*(M_0 - 1)**1.35)
            return eta_r * pi_dmax
        else:
            eta_r = 800 / (M_0**4 + 935)
            return eta_r * pi_dmax

    
