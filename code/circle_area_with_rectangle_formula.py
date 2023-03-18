import math

def circle_area(circle_radius, dr_length):
	"""
	Parameters:
	- circle_radius (int/ float): the radius of main circle that we want to calculate the area
	- dr_length(int/float): dr length is the height of each rectangle, while the circumference (2*pi*r) of each circle is the wide of each rectangle
	"""
	
	# Calculate the number of circle/ rectangle produced
	number_of_circle = circle_radius / dr_length # how much we divide the main circle is depend on the dr_length, smaller dr_length is better because the number of circle would be much more

	# Calculate the area
	area = 0
	for i in range(int(number_of_circle)):
		rectangle_area = 2 * math.pi * (dr_length * (i + 1)) * dr_length # formula = circumference of each circle (2*pi*r) * dr_length
		area += rectangle_area

	# Calculate the original area (using standard formula)
	area_original = math.pi * circle_radius * circle_radius

	# Return the value
	return area, area_original


area, original_area = circle_area(4, 0.01)
print(f"Calculated area: {area}\nOriginal area: {original_area}\n")

area, original_area = circle_area(4, 0.001)
print(f"Calculated area: {area}\nOriginal area: {original_area}\n")

area, original_area = circle_area(4, 0.0001)
print(f"Calculated area: {area}\nOriginal area: {original_area}\n")