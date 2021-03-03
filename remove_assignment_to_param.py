# By Kami Bigdely
# Remove assignment to method parameter.
class Final_Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
class Final_Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
def calculate_kinetic_energy(mass, distance, time):
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            in_km = distance.value * 9.461e12
            distance = Final_Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return
    speed = distance.value/time # [km per sec]
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            mass = Final_Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return    
        
    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass = Final_Mass(2, "solar-mass")
distance = Final_Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))