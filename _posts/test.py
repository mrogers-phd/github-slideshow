def test_function(some_value):
	"""This is just a test function to show the issues
	with PyCharm text."""
	if some_value <= 10:
		print('{} is below 10'.format(some_value))
	else:
		print('{} at least 10'.format(some_value))


test_function(4)
test_function(12)