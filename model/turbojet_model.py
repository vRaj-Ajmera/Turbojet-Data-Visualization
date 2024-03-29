from utils.general_analysis import GeneralAnalysis
import numpy as np
class TurbojetModel:
    def __init__(self, **input_parameters):
        # Initialization code for the TurbojetModel
        # Example input parameters
        self.M_0 = input_parameters.get('M_0')  # Mach number low end
        self.M_1 = input_parameters.get('M_1')  # Mach number high end
        self.T_0 = input_parameters.get('T_0')  # Total temperature (degrees K)
        self.P_0 = input_parameters.get('P_0')  # Total pressure (kPa)
        self.T_t4 = input_parameters.get('T_t4')  # Turbine Inlet Temperature (degrees K)
        self.P9rat = input_parameters.get('P9rat')  # Exit Pressure ratio

    def calculate(self):
        """
        Example method to perform overall calculations using the model.

        Parameters:
        - input_parameters (dict): Input parameters for the calculation.

        Returns:
        - dict: Results of calculations.
        """
        # Extract input parameters, with default values in case the field is empty
        #throttle = input_parameters.get('throttle', 0.8)
        #efficiency = input_parameters.get('efficiency', 0.9)
        #power = input_parameters.get('power', 50000)

        # Using GeneralAnalysis functions for thrust calculation
        # Initialize results
        mach_vals = np.linspace(self.M_0, self.M_1, 1000)
        thrust_vals = []
        tsfc_vals = []
        #rpm_vals = []

        # Initialize Analysis object
        analysis = GeneralAnalysis(M_0=self.M_1, T_0=self.T_0, P_0=self.P_0, T_t4=self.T_t4, P9rat=self.P9rat)

        # Calculate thrust over the range of Mach numbers
        for M in mach_vals:
            thrust_result = analysis.calculateThrust(M, self.T_0, self.P_0, self.T_t4, analysis.P_9, analysis.g_c, analysis.gamma_c, analysis.c_pc, analysis.gamma_t, analysis.c_pt, analysis.pi_d_max, analysis.tau_cR, analysis.T_t4R, analysis.tau_rR, analysis.eta_c, analysis.h_pR, analysis.eta_b, analysis.m_dot_R, analysis.P_0R, analysis.pi_rR, analysis.pi_cR, analysis.pi_b, analysis.pi_t, analysis.pi_n, analysis.tau_t)
            thrust_vals.append(thrust_result)
            tsfc_result = analysis.calculateTSFC(M, self.T_0, self.P_0, self.T_t4, analysis.P_9, analysis.g_c, analysis.gamma_c, analysis.c_pc, analysis.gamma_t, analysis.c_pt, analysis.pi_d_max, analysis.tau_cR, analysis.T_t4R, analysis.tau_rR, analysis.eta_c, analysis.h_pR, analysis.eta_b, analysis.m_dot_R, analysis.P_0R, analysis.pi_rR, analysis.pi_cR, analysis.pi_b, analysis.pi_t, analysis.pi_n, analysis.tau_t)
            tsfc_vals.append(tsfc_result)
            #rpm_result = analysis.calculateRPM(analysis.N_R, self.T_0, analysis.T_0R, analysis.gamma_c, analysis.gamma_t, analysis.c_pc, analysis.c_pt, analysis.g_c, analysis.M_0, analysis.pi_d_max, analysis.tau_cR, analysis.T_t4, analysis.T_t4R, analysis.tau_rR, analysis.eta_c)
            #rpm_vals.append(rpm_result)
        return mach_vals, thrust_vals, tsfc_vals
