"""
baselinedrift.py
author: sean bergen
based on code from dr. firas khasawneh

python file that adjusts for baseline drift in datasets using stationary
wavelet decomposition as seen in the paper:
    "A Wavelet Based Baseline Drift Correction Method for Fetal
    Magnetocardiograms", 
    Arvinti-Costache, Beatrice; Costache, Marius; Nafornita, Corina;
    2011 IEEE 9th International New Circuits and Systems Conference, 2011
"""
# pywavelet is used for functions that do inverse discrete stationary wavelet
# transforms, which in our case we only need to do for 1 Dimension
import pywt


"""
drift_estimate_swt(x, wname, N)
     x     -> vector of the signal, could be a time series
     wname -> wavelet name
     N     -> level of decomposition used

returns baseline_estimate -> reconstruction of time series, which accounts
                             for baseline drift (changing population, etc)

"""
def drift_estimate_swt(x, wname="db8", N=9):
    # do pywt.swt to get stationary wavelet decomp
    wave_coeffs = pywt.swt(x, wname, level = N)
    
    # change the detail coefficients to 0 for the transform
    # because wave_coeffs is a list of tuples, we do this in a for loop
    for i in range(len(wave_coeffs)):
        j = list(wave_coeffs[i])
        j[1] = 0
        wave_coeffs[i] = tuple(j)

    # then use params for pywt.iswt
    baseline_estimate = pywt.iswt(wave_coeffs, 'db8')
    return baseline_estimate
