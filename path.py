import os
import sys

test_path = os.path.dirname(__file__)
test_resource_path = test_path + "\\resources"
pom_path = test_path.removesuffix('test') + 'src\\pages'



print("1", test_path)
print("2", test_resource_path)
print("3", pom_path)