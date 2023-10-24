from pathlib import Path
import json

numbers = [1,2,3,4,5,6]

path = Path('numbers.json')          # creating the json file
contents = json.dumps(numbers)       # convert
contents1 = json.dump(numbers)
path.write_text(contents)
path.write_text(contents1)