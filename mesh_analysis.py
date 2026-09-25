# Python Program to Calculate Mesh Currents
# Electrical Engineering - Mesh Analysis

import numpy as np

print("========================================")
print("          MESH ANALYSIS")
print("========================================")

# Enter circuit parameters
R1 = float(input("Enter R1 (ohm): "))
R2 = float(input("Enter common resistance R2 (ohm): "))
R3 = float(input("Enter R3 (ohm): "))

V1 = float(input("Enter voltage source V1 (V): "))
V2 = float(input("Enter voltage source V2 (V): "))

# Mesh equations:
# (R1 + R2)I1 - R2 I2 = V1
# -R2 I1 + (R2 + R3)I2 = V2

Z = np.array([
    [R1 + R2, -R2],
    [-R2, R2 + R3]
])

V = np.array([V1, V2])

# Solve for mesh currents
I = np.linalg.solve(Z, V)

I1 = I[0]
I2 = I[1]

print("\n------------- RESULTS ----------------")
print(f"Mesh Current I1 = {I1:.3f} A")
print(f"Mesh Current I2 = {I2:.3f} A")

# Current through common resistor
I_common = I1 - I2

print(f"Common Branch Current = {I_common:.3f} A")
print("--------------------------------------")
