# general_analysis.py

# The purpose of this file is to essentially draw out all the equations from Chapter 8 of the Mattingly textbook into one file.
# This is important because it does almost exactly what our project's goal was, to model engines based on certain inputs
# Seriously, read over Chapter 8 when you have the time, it explains what the inputs should be, what assumptions should be made,
# and how to combine them all together to gain graphs similar to 1-14a thru 1-14e in the Mattingly textbook

class GeneralAnalysis:

    # Calculating referece pressure ratio at any given station delta_i
    def pressureRef(p_ref, p)
        return p/p_ref

    # Calculating reference temperature ratio at any given station theta_i
    def temperatureRef(T_ref, T)
        return T/Tref

    # Calculating corrected mass flow rate m_dot_c at any station 'i'
    def corrMassFlowRate(m_dot_i, delta_i, theta_i):
        numerator = m_dot_i * (theta_i**0.5)
        return numerator / delta_i

    # Calculating mass-flow parameter MFP
    def massFlowParameter_Simple(m_ci, A_i, p_ref, T_ref):
        numerator = m_ci * (T_ref**0.5)
        denominator = A_i * p_ref
        returm numerator/denominator

    def massFlowParameter_Mach(M, gamma, g_c, R):
        numerator = M*(((gamma*gc)/R)**0.5)
        denominator = (1 + (((gamma - 1)/2)*M)**2)**((gamma + 1)/(2*(gamma - 1)))
        return numerator/denominator

    # Corrected Engine Speed N_ci
    def corrEngineSpeed(N, theta_i):
        return N/(theta_i**0.5)

    # Corrected Thrust Fc
    def corrThrust(F, delta_0):
        return F/delta_0

    # Corrected Thrust specific fuel consumption S_c
    def corrTSFC(S, theta_0):
        return S/(theta_0**0.5)

    # Corrected fuel mass flow rate m_dot_fc
    def corrFMFR(m_dot_f, delta_2, theta_2)
        denominator = delta_2 * (theta_2**0.5)
        return m_dot_f / denominator

    # Specific m_dot_c2 calculation (gas generator)
    def calcMc2(T_4, T_2, pi_c, C_1):
        return C_1 * (pi_c / ((T_4/T_2)**0.5))
        
    # Turbine Characteristic: Capital Eta
    def capitalEta_i(gamma_i):
        return (gamma_i**0.5) * (2/(gamma_i + 1))**((gamma_i + 1)/(2*(gamma_i - 1)))

    # Corrected mass flow rate per unit area at station 4
    def calc_m4(p_4, A_4, gamma_i, T_4, R_4):
        numerator = p_4 * A_4 * capitalEta(gamma_i)
        denominator = (T_4**0.5) * (R_4**0.5)
        return numerator/denominator

    # Corrected mass flow rate per unit area station 8
    def calc_m8(p_8, A_8, T_8, M_8, gamma, g_c, R):
        return (p_8 * A_8 * massFlowParameter_Mach(M_8, gamma, g_c, R))/(T_8**0.5)

    # Pressure ratio between stage 4 and stage 8 where eta_t is turbine efficiency
    def pressureRatio4_8(T_4, T_8, eta_t, gamma_t):
        return (1 - ((1 - (T_8/T_4))/turb_eff))**(gamma_t/(gamma_t - 1))

    def temperatureRatio4_8(A_4, A_8, M_8, gamma, R, T_4, T_8, eta_t)
        numerator = A_8 * massFlowParameter_Mach(M_8, gamma, g_c, R) * pressureRatio4_8(T_4, T_8, eta_t, gamma)
        denominator = A_4 * (capitalEta(gamma)/(R**0.5))
        return (numerator/denominator)**2

    # Root of the temperature ratio as a function of Area, Mach number, and capital Eta
    def tempPressTurbineRel(A_4, A_8, M_8, gamma, R)
        numerator = A_8 * massFlowParameter_Mach(M_8, gamma, g_c, R)
        denominator = A_4 * (capitalEta(gamma)/(R**0.5))
        return numerator/denominator

    # Calculate compressor pressure ratio
    def compressorPressureRatio(T_4, theta_0, K, gamma_c):
        return (1 + (T_4/theta_0)*K)**(gamma_c/(gamma_c - 1))

    # Corrected mass flow rate through compressor
    def corrMassFlowCompr(theta_0, T_4, K_1, K_2)
        return ((theta_0/T_4)**0.5) * ((1 + (T_4/theta_0)*K_1)**(gamma_c/(gamma_c - 1))) * K_2


        

