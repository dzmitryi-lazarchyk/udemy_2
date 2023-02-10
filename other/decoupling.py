from other.converter import convert
from other.parser import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']} feet and {parsed['inches']} inches"
      f"  is equal {result} meters." )
