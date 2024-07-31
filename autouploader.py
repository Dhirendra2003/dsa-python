import subprocess
import os

# Define the path to your Git repository
repo_path = 'C:/Users/shind/PycharmProjects/python DSA'

# Change to the repository directory
os.chdir(repo_path)

# Function to run a command and print its output
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    print("Command:", ' '.join(command))
    print("Return code:", result.returncode)
    if result.stdout:
        print("Output:", result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())
    return result

# Run `git add .`
result_add = run_command(['git', 'add', '.'])

# Check if `git add .` was successful
if result_add.returncode != 0:
    print("Failed to add changes. Exiting.")
    exit(1)

# Run `git commit -m "new code"`
commit_message = "new code"
result_commit = run_command(['git', 'commit', '-m', commit_message])

# Check if `git commit` was successful
if result_commit.returncode != 0:
    print("Failed to commit changes. Exiting.")
    exit(1)

# Run `git push origin master`
result_push = run_command(['git', 'push', 'origin', 'main'])

# Check if `git push` was successful
if result_push.returncode != 0:
    print("Failed to push changes. Exiting.")
    exit(1)

print("Git repository updated successfully.")
