import subprocess
import re
import os

expect_yml = open("environment.yml")
expect_yml = expect_yml.read().split('\n')
expect_yml = expect_yml[expect_yml.index('dependencies:')+1:]
expect_yml = [item[4:].split('=') for item in expect_yml]
# print(expect_yml)

if not os.path.exists("env_list.txt"):
    os.system("conda list >> env_list.txt")
else:
    os.system("rm env_list.txt")
    os.system("conda list >> env_list.txt")

curr_env = open("env_list.txt")
curr_env = curr_env.read().split('\n')
curr_env = [item.split() for item in curr_env]
curr_env_dict = {item[0]:item[1] for item in curr_env if len(item)>1}
print("Checking packages...")

invalid = []
for item in expect_yml:
    if len(item) == 2:
        if item[0] not in curr_env_dict or curr_env_dict[item[0]] != item[1]:
            invalid.append(item[0])
    else:
        if item[0] not in curr_env_dict:
            invalid.append(item[0])

# Print the result
if not invalid:
    print("Your environment is all set!")
else:
    print("---***---\nMissing the following dependencies:")
    print(invalid)
    print("---***---")
    print("(Note that if you already have the dependency in your environment, \nit might have different versions than expected in the yml file)")