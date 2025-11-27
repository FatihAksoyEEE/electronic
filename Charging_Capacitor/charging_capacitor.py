# source : The ARRL Handbook for Radio Communications
# https://en.wikipedia.org/wiki/RC_time_constant

""" 
Description:
-------------
When a capacitor is connected with a potential source (AC or DC). It starts to charge
at a general speed but when a resistor is connected in the  circuit with in series to
a capacitor then the capacitor charges slowly means it will take more time than usual.
while the capacitor is being charged, the voltage is in exponential function with time.

'resistance(ohms) * capacitance(farads)' is called RC-timeconstant which may also b e
represented as τ (tau).  By using this RC-timeconstant we can find the voltage at any
time 't' from the initiation of charging a capacitor with the help of the exponential
function containing RC.  Both at charging and discharging of a capacitor.
"""

from math import exp # value of exp = 2.718281828459045

def charging_capacitor ( 
    voltage_source: float,
    resistance: float,
    capacitance: float,
    time: float
) -> float:
    
    
    """ 
    Calculate the voltage across a charging capacitor in an RC circuit.

    Parameters:
    -------------
    voltage_source : float
        The voltage of the source in volts (V).
    resistance : float
        The resistance in ohms (Ω).
    capacitance : float
        The capacitance in farads (F).
    time : float
        The time in seconds (s) since the capacitor started charging.

    Returns:
    -------------
    float
        The voltage across the capacitor at time 't' in volts (V).
    """
    if voltage_source <= 0:
        raise ValueError("Source Voltage must be positive.")
    if resistance <= 0: 
        raise ValueError("Resistance must be positive.")
    if capacitance <= 0: 
        raise ValueError("Capacitance must be positive.")
    return voltage_source * (1 - exp(-time / (resistance * capacitance)))

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        # Kullanıcıdan gerekli verileri al
        user_voltage = float(input("Kaynak voltajını girin (Volt): "))
        user_resistance = float(input("Direnci girin (Ohm): "))
        user_capacitance = float(input("Kapasitansı girin (Farad): "))
        user_time = float(input("Zamanı girin (saniye): "))

        # Fonksiyonu çağır ve sonucu hesapla
        capacitor_voltage = charging_capacitor(
            user_voltage, user_resistance, user_capacitance, user_time
        )

        # Sonucu ekrana yazdır
        print(f"\n{user_time} saniye sonra kapasitör üzerindeki voltaj: {capacitor_voltage:.4f} V")

    except ValueError as e:
        print(f"\nHata: Geçersiz giriş. Lütfen sayısal bir değer girin. ({e})")