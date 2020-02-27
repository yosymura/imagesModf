import os

for root, dirs, files in os.walk('c:\images'):
	for file in files:
		if file.endswith('.png'):
			print(os.path.join(root, file))