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


# # Consume all the lines before dependencies.
# while True:
#     line = expect_yml.readline()
#     if re.match(rf'dependencies:\s*\n', line):
#         line = expect_yml.readline()
#         break

# # Construct the dependency&version list
# dep_list = []
# while line:
#     result = re.search(rf'- (\w+)=?(.*)\n?', line).groups()
#     dep_list.append(result)
#     line = expect_yml.readline()

# # Get the current environment info
# subprocess = subprocess.Popen("conda list ", shell=True, stdout=subprocess.PIPE)
# subprocess_return = subprocess.stdout.read()
# curr_env = subprocess_return.decode()

# # Check if each of the dependency is in the curr_env
# invalid = []
# for i in dep_list:
#     #     re.search(rf'{(i[0]})\s+{i[1]}')
#     if not re.search(rf'({i[0]})\s+{i[1]}', curr_env):
#         invalid.append(i);

# Print the result
if not invalid:
    print("Your environment is all set!")
else:
    print("---***---\nMissing the following dependencies:")
    print(invalid)
    print("---***---")
    print("(Note that if you already have the dependency in your environment, \nit might have different versions than expected in the yml file)")