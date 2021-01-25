import json
import sys
import os

base_path = sys.argv[1] #data
train_data_path = base_path + "/train_dials.json"
dev_data_path = base_path + "/dev_dials.json"
test_data_path = base_path + "/test_dials.json"
data_paths = {"train": train_data_path, "dev": dev_data_path, "test": test_data_path}
data_path = data_paths[sys.argv[2]]
output_path = "data/single/" + sys.argv[2]+".json"

with open(data_path) as json_file:
    data = json.load(json_file)
json_file.close()

result = []
for item in data:
    if len(result) < 100:
    #if item["dialogue_idx"] == filename:
        result.append(item)
output_json = json.dumps(result)
print(item)
try:
    with open(output_path, 'w') as output_file:
        output_file.write(output_json)
except:
    path = "data/single/" 
    os.mkdir(path)
    with open(output_path, 'w') as output_file:
        output_file.write(output_json)
output_file.close()
'''
test_path = sys.argv[1]
prediction_path = sys.argv[2]
with open(test_path) as json_file:
    data = json.load(json_file)
json_file.close()
with open(prediction_path, 'w') as file_handle:
    for t in data:
        file_handle.write( str(t).replace("'","\"")  + '\n')
file_handle.close()
'''

