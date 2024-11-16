#year


with open('year_data.txt', 'r') as file:
    year = [line.strip().strip("'") for line in file.readlines()]

#make
with open('make_data.txt', 'r') as file:
    make = [line.strip().strip("'") for line in file.readlines()]

#model
with open('model_data.txt', 'r') as file:
    model = [line.strip().strip("'") for line in file.readlines()]

#trim
with open('trim_data.txt', 'r') as file:
    trim = [line.strip().strip("'") for line in file.readlines()]

#body
with open('body_data.txt', 'r') as file:
    body= [line.strip().strip("'") for line in file.readlines()]

#transmission
with open('transmission_data.txt', 'r') as file:
    transmission= [line.strip().strip("'") for line in file.readlines()]

#state
with open('state_data.txt', 'r') as file:
    state = [line.strip().strip("'") for line in file.readlines()]

#color
with open('color_data.txt', 'r') as file:
    color = [line.strip().strip("'") for line in file.readlines()]

#interior
with open('interior_data.txt', 'r') as file:
    interior = [line.strip().strip("'") for line in file.readlines()]

#print(interior)