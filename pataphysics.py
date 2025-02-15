def compute_energy(m, phi, c=299792458):
    """
    Compute the energy based on the formula:
        E = m * c^2 * (1 + φ)
    
    Parameters:
        m (float): Mass in kilograms.
        phi (float): Pataphysical factor.
        c (int or float, optional): Speed of light in m/s (default is 299,792,458 m/s).
    
    Returns:
        float: Computed energy in Joules.
    """
    return m * (c ** 2) * (1 + phi)

if __name__ == "__main__":
    try:
        # User inputs for mass and the pataphysical factor.
        mass = float(input("Enter the mass (in kg): "))
        phi = float(input("Enter the pataphysical factor φ: "))
        
        energy = compute_energy(mass, phi)
        print(f"\nFor a mass of {mass} kg and φ = {phi}, the computed energy is:\n{energy} Joules")
    except ValueError:
        print("Please enter valid numeric values for mass and φ.")
