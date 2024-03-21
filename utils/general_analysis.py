# general_analysis.py

# The purpose of this file is to essentially draw out all the equations from Chapter 8 of the Mattingly textbook into one file.
# This is important because it does almost exactly what our project's goal was, to model engines based on certain inputs
# Seriously, read over Chapter 8 when you have the time, it explains what the inputs should be, what assumptions should be made,
# and how to combine them all together to gain graphs similar to 1-14a thru 1-14e in the Mattingly textbook

class GeneralAnalysis:

    # Inputs: M_0, T_0, P_0, T_t4, P_9
    # Design Constants: pi_d_max, pi_b, pi_t, pi_n, tau_t, eta_c, eta_b, eta_m, gamma_c, gamma_t, c_pc, c_pt, h_br
    # Reference Values: M_0R, T_0R, P_0R, tau_rR, pi_rR, T_t4R, pi_dR, pi_cR, tau_cR
    # Outputs: F, m_dot, f, S, eta_p, eta_t, eta_o, pi_d, pi_c, tau_c, f, M_9, N/N_r

    # Note: For maps concerning reasonable values of pressure ratios and efficiencies for various types of aircraft, check page 363 of textbook

    # Start with outputs and work backwards

    def TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c):
        return (a_0/g_c)*(((1 + f)*(V9a0Rat)) - M_0 + ((1 + f)*(R_t/R_c)*((T_9/T_0)/(V9a0Rat))*((1 - (P_0/P_9))/gamma_c)))

    def thrust(tsfc, m_dot):
        return tsfc*m_dot

    def S(tsfc, f):
        return (f/tsfc)

    def eta_T(a_0, f, V9a0Rat, M_0, g_c, h_pR):
        numerator = (a_0**2)*(((1 + f)*((V9a0Rat)**2)) - (M_0**2))
        denominator = 2*g_c*f*h_pR
        return numerator / denominator

    def eta_P(a_0, f, V_0, M_0, g_c, tsfc):
        numerator = 2*g_c*V_0*tsfc
        denominator = (a_0**2)*(((1 + f)*((V_0/a_0)**2)) - (M_0**2))
        return numerator / denominator

    def n_over_nr(T_0, tau_r, pi_c, gamma_t, T_0R, tau_rR, pi_cR):
        numerator = T_0*tau_r*(pi_c**((gamma_c - 1)/gamma_c)) - 1
        denominator = T_0R*tau_rR*(pi_cR**((gamma_c - 1)/gamma_c)) - 1
        return (numerator / denominator)**0.5

    # Find design constants

    def calc_R_c(gamma_c, c_pc):
        return ((gamma_c - 1)/gamma_c)*c_pc

    def calc_R_t(gamma_t, c_pt):
        return ((gamma_t - 1)/gamma_t)*c_pt

    def calc_a_0(gamma_c, R_c, g_c, T_0):
        return (gamma_c*R_c*g_c*T_0)**0.5

    def calc_V_0(a_0, M_0):
        return a_0*M_0

    def calc_tau_r(gamma_c, M_0):
        return 1 + (((gamma_c - 1)/2) * (M_0**2))

    def calc_pi_r(tau_r, gamma_c):
        return tau_r**(gamma_c/(gamma_c - 1))

    def calc_eta_r(M_0):
        if M_0 <= 1:
            return 1
        else:
            return 1 - (0.075*(M_0 - 1)**1.35)

    def calc_pi_d(pi_d_max, eta_r):
        return pi_d_max * eta_r

    def calc_T_t2(T_0, tau_r):
        return T_0*tau_r

    def calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, T_t2R):
        return 1 + (tau_cR - 1)*((T_t4/T_t2)/(T_t4R/T_t2R))

    def calc_pi_c(eta_c, tau_c, gamma_c):
        return (1 + eta_c*(tau_c - 1))**(gamma_c/(gamma_c - 1))

    def calc_tau_lambda(c_pt, T_t4, c_pc, T_0):
        return (c_pt*T_t4)/(c_pc*T_0)

    def calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0):
        numerator = tau_lambda - (tau_r*tau_c)
        denominator = (h_pR*eta_b)/(c_p*T_0 - tau_lambda)
        return numerator / denominator

    def calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R):
        numerator = P_0*pi_r*pi_d*pi_c
        denominator = P_0R*pi_rR*pi_dR*pi_cR
        return m_dot_R * (numerator / denominator) * ((T_t4R/T_t4)**0.5)

    def calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n):
        return (P_0/P_9)*pi_r*pi_d*pi_c*pi_b*pi_t*pi_n

    def calc_M_9(gamma_t, P9rat, tau_t):
        return ((2/(gamma_t - 1))*((P9rat**((gamma_t - 1)/tau_t)) - 1))**0.5

    def calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t):
        return (T_t4*tau_t)/(P9rat**((gamma_t - 1)/gamma_t))

    def calc_V0a0Rat(M_9, gamma_t, R_t, T_9, gamma_c, R_c, T_0):
        return M_9*(((gamma_t*R_t*T_9)/(gamma_c*R_c*T_0))**0.5)

    # Combine all of them to make complete equations from clear independent variables

    def calculateTSFC(M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0)

        # Calculate m_dot
        m_dot = calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t)

        # Calculate V_0/a_0
        V9a0Rat = calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c)
        return tsfc


    def calculateThrust(M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0)

        # Calculate m_dot
        m_dot = calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t)

        # Calculate V_0/a_0
        V9a0Rat = calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c)
        thrust = thrust(tsfc, m_dot)
        return thrust

    def calculateUninstalledTSFC(M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0)

        # Calculate m_dot
        m_dot = calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t)

        # Calculate V_0/a_0
        V9a0Rat = calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c)
        S = S(tsfc, f)
        return S
    
    def calculateTemperatureEfficiency(M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0)

        # Calculate m_dot
        m_dot = calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t)

        # Calculate V_0/a_0
        V9a0Rat = calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        eta_T = eta_T(a_0, f, V9a0Rat, M_0, g_c, h_pR)
        return eta_T

    def calculatePressureEfficiency(M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0)

        # Calculate m_dot
        m_dot = calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = calc_T9T0Rat(T_t4, tau_t, P9rat, gamma_t)

        # Calculate V_0/a_0
        V9a0Rat = calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c)
        eta_P = eta_P(a_0, f, V_0, M_0, g_c, tsfc)
        return eta_P

    def calculateOverallEfficiency(eta_T, eta_P):
        return eta_T*eta_P

    def calculateRPM(N_R, T_0, T_0R, gamma_c, gamma_t, c_pc, c_pt, g_c, M_0, pi_d_max, tau_cR, T_t4, T_t4R, tau_rR, eta_c):
        # Calculate R_c ad R_t
        R_c = calc_R_c(gamma_c, c_pc)
        R_t = calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = calc_tau_r(gamma_c, M_0)
        pi_r = calc_pi_r(tau_r, gamma_c)
        eta_r = calc_eta_r(M_0)
        pi_d = calc_pi_d(pi_d_max, eta_r)
        T_t2 = calc_T_t2(T_0, tau_r)
        tau_c = calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, calc_T_t2(T_0, tau_rR))
        pi_c = calc_pi_c(eta_c, tau_c, gamma_c)
        
        n_div_nr = n_over_nr(T_0, tau_r, pi_c, gamma_t, T_0R, tau_rR, pi_cR)
        return n_div_nr * N_R
