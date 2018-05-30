#Q.4- Extract day from the time.
import time
from time import localtime,strftime
print("Day is: ",time.strftime("%d",localtime()))
