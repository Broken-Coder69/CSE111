# class Vector3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')
# # Write your driver code here



# # Create the first vector
# v1 = Vector3D(2, -3, 1)

# # Create the second vector
# v2 = Vector3D(-1, 4, 0)

# # Calculate and print the magnitude of the first vector
# magnitude1 = (v1.x**2 + v1.y**2 + v1.z**2)**0.5
# print(f"Magnitude of the first vector = {magnitude1}")

# # Calculate and print the magnitude of the second vector
# magnitude2 = (v2.x**2 + v2.y**2 + v2.z**2)**0.5
# print(f"Magnitude of the second vector = {magnitude2}")

# # Calculate and print the dot product of the two vectors
# dot_product = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
# print(f"Dot product of the two vectors = {dot_product}")

# # Create the third vector
# v3 = Vector3D(-4, -1, 5)

# # Calculate and print the cross product of the two vectors
# cross_product = Vector3D((v1.y*v2.z - v1.z*v2.y), (v1.z*v2.x - v1.x*v2.z), (v1.x*v2.y - v1.y*v2.x))
# print(f"Cross product of the two vectors = <{cross_product.x}, {cross_product.y}, {cross_product.z}>")




class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')


# Create the first vector
v1 = Vector3D(2, -3, 1)

# Create the second vector
v2 = Vector3D(-1, 4, 0)

# Calculate and print the magnitude of the first vector
magnitude1 = (v1.x**2 + v1.y**2 + v1.z**2)**0.5
print(f"Magnitude of the first vector = {magnitude1}")

# Calculate and print the magnitude of the second vector
magnitude2 = (v2.x**2 + v2.y**2 + v2.z**2)**0.5
print(f"Magnitude of the second vector = {magnitude2}")

# Calculate and print the dot product of the two vectorsclea
dot_product = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
print(f"Dot product of the two vectors = {dot_product}")

# Create the third vector
# v3 = Vector3D(-4, -1, 5)

# Calculate and print the cross product of the two vectors
cross_product = Vector3D((v1.y*v2.z - v1.z*v2.y), (v1.z*v2.x - v1.x*v2.z), (v1.x*v2.y - v1.y*v2.x))
print(f"Cross product of the two vectors = <{cross_product.x}, {cross_product.y}, {cross_product.z}>")




