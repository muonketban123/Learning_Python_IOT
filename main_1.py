
#import mypackage.module1
#from mypackage.module1 import* // import tất cả hàm trong module1 rồi
from mypackage._init_ import *
from mypackage import module1, module2

print("tổng của a + b = ", end = "")
module1.cong_hai_so(a,b)

