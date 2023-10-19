import subprocess
import os
os.environ["PYTHONIOENCODING"] = "utf-8"

def run_command(command):
    """Function to execute a command and print its output"""
    result = subprocess.run(command, capture_output=True, text=True,encoding='utf-8', shell=True)
    if result.stderr:
        print(result.stderr)
    else:
        print(result.stdout)

# Set the initial seed
seed = 1225

# Run the process 10 times
for i in range(10):
    # Create a unique name for each iteration
    name = f"jesus_{i}"

    print("starting 1!")
    # Construct and run the first command
    cmd1 = f'python text2img.py "Jesus Christ, realistic, game asset, 4k, hyperealistic, majestic" {name} --seed {seed}'
    run_command(cmd1)

    print("starting 2!")
    # Construct and run the second command
    cmd2 = f'python main.py --config configs/image.yaml input=data/{name}_rgba.png save_path={name}'
    run_command(cmd2)

    # Construct and run the third command
    print("starting 3!")
    cmd3 = f'python main2.py --config configs/image.yaml input=data/{name}_rgba.png save_path={name}'
    run_command(cmd3)
    print("done!")
    # Increment the seed for the next iteration
    seed += 1
