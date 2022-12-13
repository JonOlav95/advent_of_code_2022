import pandas as pd
import numpy as np


arr = pd.read_csv("day_12.txt", header=None).values.squeeze()
arr = np.array(list((map(list, arr))))

start = np.where(arr == "S")
end = np.where(arr == "E")

start_y = start[0][0]
start_x = start[1][0]

end_y = end[0][0]
end_x = end[1][0]

arr[start_y, start_x] = "a"
arr[end_y, end_x] = "z"

max_y = len(arr)
max_x = len(arr[0])