import pytest
import time
from base.DriverClass import Driver
@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope='class')
def oneTimeSetUp(request):
 print('Before Class')
 driver1 = Driver()
 driver = driver1.getDriverMethod()
 if request.cls is not None:
   request.cls.driver = driver
 yield driver
 time.sleep(5)
 driver.quit()
 print('After Class')



