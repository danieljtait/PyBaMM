import electrolyte_conductivity_Landesfeind2019_base as base
import numpy as np


def electrolyte_conductivity_Landesfeind2019_EC_DMC_1_1(c_e, T, T_inf, E_k_e, R_g):
    """
    Conductivity of LiPF6 in EC:DMC (1:1) as a function of ion concentration and
    Temperature. The data comes from [1].
    References
    ----------
    .. [1] Landesfeind, J. and Gasteiger, H.A., 2019. Temperature and Concentration
    Dependence of the Ionic Transport Properties of Lithium-Ion Battery Electrolytes.
    Journal of The Electrochemical Society, 166(14), pp.A3079-A3097.
    ----------
    c_e: :class: `numpy.Array`
        Dimensional electrolyte concentration
    T: :class: `numpy.Array`
        Dimensional temperature
    Returns
    -------
    :`numpy.Array`
        Electrolyte diffusivity
    """
    coeffs = np.array([7.98e-1, 2.28e2, -1.22, 5.09e-1, -4e-3, 3.79e-3])

    return base.electrolyte_conductivity_Landesfeind2019_base(c_e, T, coeffs)
