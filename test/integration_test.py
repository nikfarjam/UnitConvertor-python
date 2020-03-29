import sys
sys.path.append(sys.path[0] + '/..')
import doctest
doctest.testfile("integration_test.txt")

print("Finished integration tests")