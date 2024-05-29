# A script to classify and count 'active' and 'inactive'
# gridblocks in a discretized reservoir

#################### Task 1 ############################
# Request for reservoir dimensions and discretization parameters

# Lx
Lx = float(input("Enter the length of the reservoir in the x-direction (Lx): "))
# Ly
Ly = float(input("Enter the length of the reservoir in the y-direction (Ly): "))
# Lz
Lz = float(input("Enter the length of the reservoir in the z-direction (Lz): "))
# nx
nx = int(input("Enter the number of gridblocks in the x-direction (nx): "))
# ny
ny = int(input("Enter the number of gridblocks in the y-direction (ny): "))
# nz
nz = int(input("Enter the number of gridblocks in the z-direction (nz): "))

#################### Task 2 ############################
# Request for the cut-off value
# cut_off
cut_off = float(input("Enter the cut-off value for classifying gridblocks (cut_off): "))

#################### Task 3 ############################
# Initialize counters

# n_active
n_active = 0
# n_inactive
n_inactive = 0

#################### Task 4 ############################
# Loop through all blocks (nested loop)
for k in range(1, nz+1):
    # Initialize layer counter
    layer_count = 0
    # two nested loops go here
    for j in range(1, ny+1):
        for i in range(1, nx+1):
            # Request the permeability value from the user (not implemented)
            permeability = float(input(f"Enter the permeability value of gridblock ({i}, {j}, {k}): "))
            # Classify the gridblock as 'active' or 'inactive' based on the cut-off value
            if permeability < cut_off:
                n_inactive += 1
            else:
                n_active += 1
            # Increment the layer counter
            layer_count += 1
    # Print layer count
    print(f"Number of 'active' gridblocks in layer {k}: {layer_count}")

#################### Task 5 ############################
# Print overall counts

# Print 'active'
print(f"Number of 'active' gridblocks: {n_active}")

# Print 'inactive'
print(f"Number of 'inactive' gridblocks: {n_inactive}")
