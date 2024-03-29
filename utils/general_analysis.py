# general_analysis.py

# The purpose of this file is to essentially draw out all the equations from Chapter 8 of the Mattingly textbook into one file.
# This is important because it does almost exactly what our project's goal was, to model engines based on certain inputs
# Seriously, read over Chapter 8 when you have the time, it explains what the inputs should be, what assumptions should be made,
# and how to combine them all together to gain graphs similar to 1-14a thru 1-14e in the Mattingly textbook
import numpy as np

class GeneralAnalysis:

    # Inputs: M_0, T_0, P_0, T_t4, P_9
    # Design Constants: pi_d_max, pi_b, pi_t, pi_n, tau_t, eta_c, eta_b, eta_m, gamma_c, gamma_t, c_pc, c_pt, h_br
    # Reference Values: M_0R, T_0R, P_0R, tau_rR, pi_rR, T_t4R, pi_dR, pi_cR, tau_cR
    # Outputs: F, m_dot, f, S, eta_p, eta_t, eta_o, pi_d, pi_c, tau_c, f, M_9, N/N_r

    # Note: For maps concerning reasonable values of pressure ratios and efficiencies for various types of aircraft, check page 363 of textbook

    # Start with outputs and work backwards
    def __init__(self, M_0=1.5, T_0=229.8, P_0=30.8, T_t4=1670, P9rat=0.955):
        # Initialize default values
        self.M_0 = M_0
        self.T_0 = T_0
        self.P_0 = P_0
        self.T_t4 = T_t4
        self.P9rat = P9rat
        self.P_9 = P_0/P9rat

        # Reference Values and Design Constants
        self.g_c = 1
        self.T_0R = 216.7
        self.gamma_cR = 1.4
        self.c_pc = 1.004
        self.c_ptR = 1.239
        self.gamma_tR = 1.3
        self.c_ptR = 1.239
        self.T_t4R = 1800
        self.M_0R = 2
        self.pi_cR = 10
        self.tau_cR = 2.0771
        self.eta_cR = .8641
        self.tau_tR = .8155
        self.pi_tR = .3746
        self.pi_d_maxR = .95
        self.pi_dR = .8788
        self.pi_bR = .94
        self.pi_nR = .96
        self.eta_bR = .98
        self.eta_mR = .99
        self.h_pR = 42800
        self.fR = .03567
        self.SR = 44.21
        self.P_0R = 19.40
        self.m_dot_R = 50
        self.FR = 40345
        self.P_9R = self.P_0R / .955
        self.P9ratR = .955

        self.gamma_c = self.gamma_cR
        self.gamma_t = self.gamma_tR
        self.c_pt = self.c_ptR
        self.c_p = self.c_pc

        self.tau_r = self.calc_tau_r(self.gamma_c, self.M_0)
        self.tau_rR = self.calc_tau_r(self.gamma_c, self.M_0R)
        self.T_t2 = self.calc_T_t2(self.T_0, self.tau_r)
        self.T_t2R = self.calc_T_t2(self.T_0R, self.tau_rR)
        self.tau_c = self.calc_tau_c(self.tau_cR, self.T_t4, self.T_t2, self.T_t4R, self.T_t2R)
        self.tau_t = self.tau_tR

        self.pi_rR = self.calc_pi_r(self.tau_rR, self.gamma_c)
        self.pi_cR = self.calc_pi_c(self.eta_cR, self.tau_cR, self.gamma_c)

        self.pi_b = self.pi_bR
        self.pi_t = self.pi_tR
        self.pi_n = self.pi_nR
        self.pi_d_max = self.pi_d_maxR

        self.eta_c = self.eta_cR
        self.eta_b = self.eta_bR
        self.T_9 = self.calc_T9T0Rat(self.T_t4, self.tau_t, self.P9rat, self.gamma_t, self.c_pc, self.c_pt) * self.T_0
        self.N_R = 18800 # double check this maximum rpm value


    def TSFC(self, a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, T_9, T_0, P_0, P_9, gamma_c):
        return (a_0/g_c)*(((1 + f)*(V9a0Rat)) - M_0 + ((1 + f)*(R_t/R_c)*((T_9/T_0)/(V9a0Rat))*((1 - (P_0/P_9))/gamma_c)))

    def calc_thrust(self, tsfc, m_dot):
        return tsfc*m_dot

    def S(self, tsfc, f):
        return (f/tsfc)

    def eta_T(self, a_0, f, V9a0Rat, M_0, g_c, h_pR):
        numerator = (a_0**2)*(((1 + f)*((V9a0Rat)**2)) - (M_0**2))
        denominator = 2*g_c*f*h_pR
        return numerator / denominator

    def eta_P(self, a_0, f, V_0, M_0, g_c, tsfc):
        numerator = 2*g_c*V_0*tsfc
        denominator = (a_0**2)*(((1 + f)*((self.V_9/a_0)**2)) - (M_0**2))
        return numerator / denominator

    def n_over_nr(self, T_0, tau_r, pi_c, gamma_t, T_0R, tau_rR, pi_cR):
        numerator = T_0*tau_r*(pi_c**((self.gamma_c - 1)/self.gamma_c)) - 1
        denominator = T_0R*tau_rR*(pi_cR**((self.gamma_c - 1)/self.gamma_c)) - 1
        return (numerator / denominator)**0.5

    # Find design constants
    def calc_R_c(self, gamma_c, c_pc):
        return ((gamma_c - 1)/gamma_c)*c_pc*1000

    def calc_R_t(self, gamma_t, c_pt):
        return ((gamma_t - 1)/gamma_t)*c_pt*1000

    def calc_a_0(self, gamma_c, R_c, g_c, T_0):
        return (gamma_c*R_c*g_c*T_0)**0.5

    def calc_V_0(self, a_0, M_0):
        return a_0*M_0

    def calc_tau_r(self, gamma_c, M_0):
        return 1 + (((gamma_c - 1)/2) * (M_0**2))

    def calc_pi_r(self, tau_r, gamma_c):
        return tau_r**(gamma_c/(gamma_c - 1))

    def calc_eta_r(self, M_0):
        if M_0 <= 1:
            return 1
        else:
            return 1 - (0.075*(M_0 - 1)**1.35)

    def calc_pi_d(self, pi_d_max, eta_r):
        return pi_d_max * eta_r

    def calc_T_t2(self, T_0, tau_r):
        return T_0*tau_r

    def calc_tau_c(self, tau_cR, T_t4, T_t2, T_t4R, T_t2R):
        return 1 + (tau_cR - 1)*((T_t4/T_t2)/(T_t4R/T_t2R))

    def calc_pi_c(self, eta_c, tau_c, gamma_c):
        return (1 + eta_c*(tau_c - 1))**(gamma_c/(gamma_c - 1))

    def calc_tau_lambda(self, c_pt, T_t4, c_pc, T_0):
        return (c_pt*T_t4)/(c_pc*T_0)

    def calc_f(self, tau_lambda, tau_r, tau_c, h_pR, eta_b, c_p, T_0):
        numerator = tau_lambda - (tau_r*tau_c)
        denominator = (h_pR*eta_b)/(c_p*T_0) - tau_lambda
        return numerator / denominator

    def calc_m_dot(self, m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, pi_dR, pi_cR, T_t4, T_t4R):
        numerator = P_0*pi_r*pi_d*pi_c
        denominator = P_0R*pi_rR*pi_dR*pi_cR
        return m_dot_R * (numerator / denominator) * ((T_t4R/T_t4)**0.5)

    def calc_P9Rat(self, P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n):
        return (P_0/P_9)*pi_r*pi_d*pi_c*pi_b*pi_t*pi_n

    def calc_M_9(self, gamma_t, P9rat):
        return np.sqrt((2/(gamma_t - 1))*((P9rat**((gamma_t - 1)/gamma_t)) - 1))

    def calc_T9T0Rat(self, T_t4, tau_t, P9rat, gamma_t,c_pc,c_pt):
        tau_lambda = self.calc_tau_lambda(c_pt,T_t4,c_pc,self.T_0)
        return (tau_lambda*tau_t)/(P9rat**((gamma_t - 1)/gamma_t))*c_pc/c_pt

    def calc_V0a0Rat(self, M_9, gamma_t, R_t, T_9, gamma_c, R_c, T_0):
        return M_9*(((gamma_t*R_t*T_9)/(gamma_c*R_c*T_0))**0.5)

    # Combine all of them to make complete equations from clear independent variables

    def calculateTSFC(self, M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = self.calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = self.calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, self.c_p, T_0)

        # Calculate m_dot
        m_dot = self.calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, self.pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = self.calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = self.calc_M_9(gamma_t, P9rat)

        # Calculate Temperature Ratio
        T9T0Rat = self.calc_T9T0Rat(T_t4,tau_t,P9rat,gamma_t,c_pc,c_pt)

        # Calculate V_0/a_0
        V9a0Rat = self.calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = self.TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, self.T_9, T_0, P_0, P_9, gamma_c)
        return tsfc


    def calculateThrust(self, M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = self.calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = self.calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, self.c_p, T_0)

        # Calculate m_dot
        m_dot = self.calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, self.pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = self.calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = self.calc_M_9(gamma_t, P9rat)

        # Calculate Temperature Ratio
        T9T0Rat = self.calc_T9T0Rat(T_t4,tau_t,P9rat,gamma_t,c_pc,c_pt)

        # Calculate V_0/a_0
        V9a0Rat = self.calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = self.TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, self.T_9, T_0, P_0, P_9, gamma_c)
        thrust = self.calc_thrust(tsfc, m_dot)
        return thrust

    def calculateUninstalledTSFC(self, M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = self.calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = self.calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, self.c_p, T_0)

        # Calculate m_dot
        m_dot = self.calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, self.pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = self.calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = self.calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = self.calc_T9T0Rat(T_t4,tau_t,P9rat,gamma_t,c_pc,c_pt)

        # Calculate V_0/a_0
        V9a0Rat = self.calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = self.TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, self.T_9, T_0, P_0, P_9, gamma_c)
        S = S(tsfc, f)
        return S

    def calculateTemperatureEfficiency(self, M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = self.calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = self.calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, self.c_p, T_0)

        # Calculate m_dot
        m_dot = self.calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, self.pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = self.calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = self.calc_M_9(gamma_t, P9rat)

        # Calculate Temperature Ratio
        T9T0Rat = self.calc_T9T0Rat(T_t4,tau_t,P9rat,gamma_t,c_pc,c_pt)
        # Calculate V_0/a_0
        V9a0Rat = self.calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        eta_T = eta_T(a_0, f, V9a0Rat, M_0, g_c, h_pR)
        return eta_T

    def calculatePressureEfficiency(self, M_0, T_0, P_0, T_t4, P_9, g_c, gamma_c, c_pc, gamma_t, c_pt, pi_d_max, tau_cR, T_t4R, tau_rR, eta_c, h_pR, eta_b, m_dot_R, P_0R, pi_rR, pi_cR, pi_b, pi_t, pi_n, tau_t):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)
        tau_lambda = self.calc_tau_lambda(c_pt, T_t4, c_pc, T_0)

        # Calculate f
        f = self.calc_f(tau_lambda, tau_r, tau_c, h_pR, eta_b, self.c_p, T_0)

        # Calculate m_dot
        m_dot = self.calc_m_dot(m_dot_R, P_0, pi_r, pi_d, pi_c, P_0R, pi_rR, self.pi_dR, pi_cR, T_t4, T_t4R)

        # Intermediary Step
        P9rat = self.calc_P9Rat(P_0, P_9, pi_r, pi_d, pi_c, pi_b, pi_t, pi_n)

        # Calculate M_9
        M_9 = self.calc_M_9(gamma_t, P9rat, tau_t)

        # Calculate Temperature Ratio
        T9T0Rat = self.calc_T9T0Rat(T_t4,tau_t,P9rat,gamma_t,c_pc,c_pt)

        # Calculate V_0/a_0
        V9a0Rat = self.calc_V0a0Rat(M_9, gamma_t, R_t, (T9T0Rat*T_0), gamma_c, R_c, T_0)

        # Finally, Calculate TSFC
        tsfc = self.TSFC(a_0, g_c, f, V9a0Rat, M_0, R_t, R_c, self.T_9, T_0, P_0, P_9, gamma_c)
        eta_P = eta_P(a_0, f, self.V_0, M_0, g_c, tsfc)
        return eta_P

    def calculateOverallEfficiency(eta_T, eta_P):
        return eta_T*eta_P

    def calculateRPM(self, N_R, T_0, T_0R, gamma_c, gamma_t, c_pc, c_pt, g_c, M_0, pi_d_max, tau_cR, T_t4, T_t4R, tau_rR, eta_c):
        # Calculate R_c ad R_t
        R_c = self.calc_R_c(gamma_c, c_pc)
        R_t = self.calc_R_t(gamma_t, c_pt)

        # Calculate a_0
        a_0 = self.calc_a_0(gamma_c, R_c, g_c, T_0)

        # Calculate various pressure ratios and efficiencies needed later
        tau_r = self.calc_tau_r(gamma_c, M_0)
        pi_r = self.calc_pi_r(tau_r, gamma_c)
        eta_r = self.calc_eta_r(M_0)
        pi_d = self.calc_pi_d(pi_d_max, eta_r)
        T_t2 = self.calc_T_t2(T_0, tau_r)
        tau_c = self.calc_tau_c(tau_cR, T_t4, T_t2, T_t4R, self.calc_T_t2(T_0, tau_rR))
        pi_c = self.calc_pi_c(eta_c, tau_c, gamma_c)

        n_div_nr = self.n_over_nr(T_0, tau_r, pi_c, gamma_t, T_0R, tau_rR, self.pi_cR)
        return n_div_nr * N_R
    
    def AtmosphereFunction(self, h_G_km):       #Atmosphere Function input hieght in Kilometers
        h_G = h_G_km*3280.84              #Kilometers to feet
        r_e=3959*5280                     #miles to feet
        R=1716.5                          #ft2/R-sec
        g0=32.174                         #ft/s^2
        T0=518.69                         #deg R
        g_hG=g0*(r_e/(r_e+h_G))**2        #gravity acceleration based on geopotential altitude
        h=(r_e/(r_e+h_G))*h_G             #altitude from geopotential altitude and earth radius
        if h<36000:                       # standard atmosphere maths up until tropopause
            h0=0                          # initial altitude of comparison is sea level
            T0=518.69                     #deg R
            P0=2116.22                    #psf
            rho0=2.3769e-3                #slugs/ft3
            a1=-3.57/1000                 #deg R/ft
            T= T0 + a1*(h-h0)             # calculate temperature from linear distribution
            P= P0*(T/T0)**(-g0/(R*a1))    #pressure from temperature
            rho = rho0*(T/T0)**(-((g0/(R*a1))+1))       #density from temperature
        else:
            h0=36000                      #tropopause altitude (ft)
            P0=4.760119191888137e+2       #from anderson
            rho0=7.103559955456123e-4     #from running code at 36000
            T=389.99                      # constant temperature
            P= P0*np.exp((-g0/(R*T)*(h-h0)))            #pressure from temperature
            rho = rho0*np.exp(-(g0/(R*T)*(h-h0)))       #density from temperature
        a=np.sqrt(1.4*P/rho)              # speed of sound
        h_G = h_G_km/3280.84              #Feet to Km
        h = h/3280.84                     #Geopotential altitude in km
        T = T*0.555556                    #Rankine to Kelvin
        P = P /0.020885 /1000             #Psf to KPa
        rho = rho/515.4                   #Density in kg/m^2
        a = a/3.281                       #Local  m/s
        return [h_G, h, T, P, rho,a]