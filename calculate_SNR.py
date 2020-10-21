## Function outputs two arrays; the new signal with added noise, as well as the noise generated signal
def SNR(signal, SNR, seed):
    from math import sqrt, log10
    # Signal must be a sequence for numbers with a fixed length
    # SNR is the desired ratio between the signal and noise expressed in dB
    # Seed is for reproduction of the random number generator from numpy
    np.random.seed(seed)
    if signal.ndim == 2:
        signal = signal[:,0]
    # Create random gaussian noise
    noise = np.random.randn(len(signal))

    # Calculate signal power and noise power
    signal_power = sum(abs(signal)*abs(signal))/len(signal)
    print(signal_power)
    noise_power = sum(abs(noise)*abs(noise))/len(signal)
    print(noise_power)
    # Calculate initial SNR
    initial_snr = 10*(log10(signal_power/noise_power))
    print(initial_snr)
    
    # k as converter to desired SNR value
    k = (signal_power/noise_power)*10**(-SNR/10)
    
    # Create new noise based on SNR value
    new_noise = sqrt(k)*noise
    
    # Calculate new noise power and SNR [new SNR should be more or less the same as desired SNR]
    new_noise_power = sum(abs(new_noise)*abs(new_noise))/len(signal)
    print(new_noise_power)
    new_snr = 10*(log10(signal_power/new_noise_power))
    print(new_snr)
    
    # Add new noise to original signal
    signal = signal + new_noise
    return(signal, new_noise)



def signal_plots(signal,noise,noisy_signal):
    if signal.ndim == 2:
        signal = signal[:,0]
    import matplotlib.pyplot as plt
    import numpy as np
    fig, axs = plt.subplots(3)
    
    fig.set_size_inches(9.5, 5.5)
    #axs.plot(data)
    #axs.plot(data2)
    
    axs[0].plot(signal, color = "deepskyblue")
    axs[1].plot(noise , color = "deepskyblue")
    axs[2].plot(noisy_signal , color = "deepskyblue")
    
    # Defining custom 'xlim' and 'ylim' values.
    custom_ylim = (-2, 2)
    
    # Setting the values for all axes.
    plt.setp(axs, ylim=custom_ylim)
    
    # Adjust the Y-axis values
    axs[0].locator_params(axis='y', nbins=2)
    axs[1].locator_params(axis='y', nbins=2)
    axs[2].locator_params(axis='y', nbins=2)
    fig.tight_layout()




