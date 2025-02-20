from Helmet_Detection_PyTorch.logger import logging
from Helmet_Detection_PyTorch.exception import HelmetException
import sys


logging.info("First Log!")

try :
    a= 2+ "3"
    print(a)
except Exception as e:
    raise HelmetException(e,sys) from e