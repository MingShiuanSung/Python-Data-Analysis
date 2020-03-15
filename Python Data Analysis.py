# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = 'D:\Steven Sung\course\course\嵌入式\Homework\HW1\\107061139.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        if row.get('HUMD') == '-99.000' or row.get('HUMD') == '-999.000':
            row.pop('HUMD')
        data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
C0A880_list = list(filter(lambda item: item['station_id'] == 'C0A880', data))
C0F9A0_list = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
C0G640_list = list(filter(lambda item: item['station_id'] == 'C0G640', data))
C0R190_list = list(filter(lambda item: item['station_id'] == 'C0R190', data))
C0X260_list = list(filter(lambda item: item['station_id'] == 'C0X260', data))

List = [['C0A880',C0A880_list], ['C0F9A0', C0F9A0_list], ['C0G640', C0G640_list], ['C0R190', C0R190_list], ['C0X260', C0X260_list]]

output = []
for name, item_list in List:
    sumValue = 0
    for item in item_list:
        for key, value in item.items():
            if key == 'HUMD':
                sumValue += float(value)
    if sumValue == 0:
        sumValue = 'NONE'
    output.append([name,sumValue])


#=======================================

# Part. 4
#=======================================
# Print result
print(output)
#========================================