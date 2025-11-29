# Tracking 
import traceback

arr = [1,2,3,4,5]

try:
    value = arr[6]

except:
    traceback.print_exc()

print("end")