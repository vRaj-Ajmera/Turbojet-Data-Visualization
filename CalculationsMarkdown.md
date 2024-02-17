# VARIABLES:
# eta = efficiency
# eta_d = isentropic efficiency of diffusor
# eta_r = portion of pi_d due to ram recovery
# g = newton's constant
# gamma = ratio of specific heats
# h = enthalpy
# P = pressure
# pi = pressure ratio
# pi_d = pressure ratio across diffusor
# pi_dmax = portion of pi_d due to wall friction
# pi_r = total/static pressure ratio of free stream
# R = gas constant
# s = entropy
# T = temperature
# tau = temperature ratio
# tau_d = temperature ratio across diffusor
# tau_n = temperature ratio across nozzle
# tau_r = total/static temperature ratio of free stream
# V = Velocity

# A NOTE ON SUBSCRIPTING: Throughout the book, there are a series of subscripts which are used to denote location. These are not always intuitive,
# so the following denotes the general subscript meanings for certain numbers:
# 0 = Free Stream, Before Inlet
# 2 = At Inlet, Before Compressor
# 3 = After Compressor, Before Combustor
# 4 = After Combustor, Before Turbine
# 4.5 = After High-Pressure Turbines, Before Low-Pressure Turbines
# 5 = After Turbines, Before Nozzle
# 8 or 9 = After Nozzle
# 13 (only Turbofan) = After Fan, Before Bypass Nozzle
# 19 (only Turbofan) = After Bypass Nozzle

## Inlet/Exit Modelling - Matthew Weippert

  ### Mattingly 6-4: Isentropic Efficiency of Diffusor
    eta_d = (h_t2s - h_0)/(h_t0 - h_0)
    eta_d ≈ (T_t2s - T_0)/(T_t0 - T_0)
    eta_d = ((tau_r*pi_d)^((gamma - 1)/gamma) - 1)/(tau_r - 1)

  ### Mattingly 6-5: Pressure Ratio Causation Ratios
    pi_d = pi_dmax*eta_r   # For Mach numbers <= 1, eta_r = 1
    eta_r = 1 - (0.075*(M_0 - 1)^1.35)   # For Mach > 1, < 5
    eta_r = 800/(M_0^4 + 935)   # For Mach > 5

  ### Mattingly 6-9: Free Stream Properties
    tau_r = h_t0/h_0
    tau_r = (h_0 + V_0^2/(2*g_c))/h_0
    tau_d = 1   # Since the inlet is adiabatic
    pi_d = P_t2/P_t0
    pi_d = exp^(-(s_2 - s_0)/R)

  ### Mattingly 6-9: Nozzle Properties
    tau_n = 1   # Since the nozzle is adiabatic
    pi_n = P_t9/P_t8
    pi_n = exp^(-(s_9 - s_8)/R)
    V_9 = (2*g_c*(h_t9 - h_9))^0.5
    P_r9 = P_rt9/(P_t9/P_9)
