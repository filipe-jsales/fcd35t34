import matplotlib.pyplot as plt

def nrz_encoding(bits):
    signal = []
    for bit in bits:
        if bit == '1':
            signal.append(1)
        else:
            signal.append(0)
    return signal

def manchester_encoding(bits):
    signal = []
    for bit in bits:
        if bit == '1':
            signal.append(1)
            signal.append(0)
        else:
            signal.append(0)
            signal.append(1)
    return signal

def hdb3_encoding(bits):
    signal = []
    last_nonzero = 1  
    consecutive_zeros = 0
    violations = 0
    
    for bit in bits:
        if bit == '1':
            if last_nonzero == 1:
                signal.append(1)
                last_nonzero = -1
            else:
                signal.append(-1)
                last_nonzero = 1
            consecutive_zeros = 0
        else:
            consecutive_zeros += 1
            if consecutive_zeros == 4:
                if violations % 2 == 0:
                    signal[-3] = last_nonzero
                    signal.append(last_nonzero)
                else:
                    signal.append(0)
                    signal.append(0)
                    signal.append(0)
                    signal.append(-last_nonzero)
                violations += 1
                consecutive_zeros = 0
            else:
                signal.append(0)
    
    return signal

def plot_encoding(bits, nrz, manchester, hdb3, title):
    fig, axes = plt.subplots(4, 1, figsize=(15, 12), sharex=True)
    
    axes[0].step(range(len(bits)), [int(bit) for bit in bits], where='post')
    axes[0].set_ylim(-1.5, 1.5)
    axes[0].set_title(f'Original Bits - {title}')
    axes[0].grid(True)

    axes[1].step(range(len(nrz)), nrz, where='post')
    axes[1].set_ylim(-1.5, 1.5)
    axes[1].set_title('NRZ Encoding')
    axes[1].grid(True)

    axes[2].step(range(len(manchester)), manchester, where='post')
    axes[2].set_ylim(-1.5, 1.5)
    axes[2].set_title('Manchester Encoding')
    axes[2].grid(True)

    axes[3].step(range(len(hdb3)), hdb3, where='post')
    axes[3].set_ylim(-2, 2)
    axes[3].set_title('HDB3 Encoding')
    axes[3].grid(True)

    plt.tight_layout()
    plt.show()

sequence1 = '1000000001010011'
sequence2 = '1110100101000010'

nrz1 = nrz_encoding(sequence1)
manchester1 = manchester_encoding(sequence1)
hdb31 = hdb3_encoding(sequence1)

nrz2 = nrz_encoding(sequence2)
manchester2 = manchester_encoding(sequence2)
hdb32 = hdb3_encoding(sequence2)

plot_encoding(sequence1, nrz1, manchester1, hdb31, "Sequência 1")

plot_encoding(sequence2, nrz2, manchester2, hdb32, "Sequência 2")
