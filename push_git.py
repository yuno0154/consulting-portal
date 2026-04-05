import subprocess
import os

try:
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write("Running git init...\n")
        res1 = subprocess.run(['git', 'init'], capture_output=True, text=True, check=False)
        f.write(f"STDOUT: {res1.stdout}\nSTDERR: {res1.stderr}\n")

        f.write("\nAdding remote origin...\n")
        res2 = subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/yuno0154/consulting-portal.git'], capture_output=True, text=True, check=False)
        f.write(f"STDOUT: {res2.stdout}\nSTDERR: {res2.stderr}\n")

        f.write("\nAdding files...\n")
        res3 = subprocess.run(['git', 'add', '.'], capture_output=True, text=True, check=False)
        f.write(f"STDOUT: {res3.stdout}\nSTDERR: {res3.stderr}\n")

        f.write("\nCommitting...\n")
        res4 = subprocess.run(['git', 'commit', '-m', 'Initial commit'], capture_output=True, text=True, check=False)
        f.write(f"STDOUT: {res4.stdout}\nSTDERR: {res4.stderr}\n")

        f.write("\nPushing to GitHub...\n")
        res5 = subprocess.run(['git', 'push', '-u', 'origin', 'master'], capture_output=True, text=True, check=False)
        f.write(f"STDOUT: {res5.stdout}\nSTDERR: {res5.stderr}\n")
        
        # Try both main and master push
        res6 = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True, check=False)
        f.write(f"\nPush to main STDOUT: {res6.stdout}\nSTDERR: {res6.stderr}\n")
except Exception as e:
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write(f"\nAn error occurred: {str(e)}\n")
