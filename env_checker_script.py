import subprocess
import re

expect_yml = open("environment.yml")

# Consume all the lines before dependencies.
while True:
    line = expect_yml.readline()
    if re.match(rf'dependencies:\s*\n', line):
        line = expect_yml.readline()
        break

# Construct the dependency&version list
dep_list = []
while line:
    result = re.search(rf'- (\w+)=?(.*)\n?', line).groups()
    dep_list.append(result)
    line = expect_yml.readline()

# Get the current environment info
subprocess = subprocess.Popen("conda list ", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
curr_env = subprocess_return.decode()

# Check if each of the dependency is in the curr_env
invalid = []
for i in dep_list:
    #     re.search(rf'{(i[0]})\s+{i[1]}')
    if not re.search(rf'({i[0]})\s+{i[1]}', curr_env):
        invalid.append(i)

# Print the result
if not invalid:
    print("Your environment is all set!")
else:
    print("---***---\nMissing the following dependencies:")
    print(invalid)
    print("---***---")
    print("(Note that if you already have the dependency in your environment, \nit might have different versions than expected in the yml file)")