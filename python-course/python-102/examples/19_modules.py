# Module for the Operating System
import collections
import time
import re
import sys
print(sys.path)

# Module for the Regular Expressions
text = "Mi numero de telefono es 22402231, y el códifo de pais es 506, mi numero de suerte es 3"
result = re.findall("[0-9]+", text)
print(result)

# Module for time and dates
timestamp = time.time()
localtime = time.localtime()
humanlocaltime = time.asctime(localtime)
print(timestamp)
print(localtime)
print(humanlocaltime)

# Module for list
numbers = [1, 1, 2, 1, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)
