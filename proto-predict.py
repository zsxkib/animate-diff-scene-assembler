import subprocess
import json
import time  # Import the time module

print("Starting the script to execute 'cog predict' command...")

# Attempting to read the JSON content from 'workflow_api.json'
try:
    with open("workflow_api.json", "r") as file:
        workflow_json = json.load(file)
        # Convert the JSON object to a string, for demonstration we'll truncate the content for readability
        workflow_json_content = json.dumps(workflow_json)
        print("Successfully read 'workflow_api.json'.")
        print(f"JSON content (truncated for display): {workflow_json_content[:100]}...")
except Exception as e:
    print(f"Failed to read 'workflow_api.json': {e}")
    exit(1)

# Constructing the command with the read JSON content
print("Constructing the 'cog predict' command...")
command = [
    "sudo",
    "cog",
    "predict",
    "-i",
    f"workflow_json={workflow_json_content}",
    "-i",
    "input_file=@files.zip",
    "-i",
    "return_temp_files=True",
    "-i",
    "randomise_seeds=True",
]
print("Command constructed successfully.")


# Displaying the command to be executed (truncating for readability)
command_str = "\n".join(command)
print("Executing command:\n\n{}\n".format(command_str))

# Execute the command and log the output
try:
    start_time = time.time()  # Capture the start time
    print("Starting the execution of the command...")
    with open(
        "command_output.log", "w"
    ) as log_file:  # Open a log file to write the output, clearing it for subsequent runs
        subprocess.run(
            command, check=True, stdout=log_file, stderr=subprocess.STDOUT
        )  # Redirect both stdout and stderr to the log file, effectively clearing the log before writing new output
    end_time = time.time()  # Capture the end time
    duration = end_time - start_time  # Calculate the duration
    print("Command executed successfully. Output logged to 'command_output.log'.")
    print(f"Execution time: {duration:.2f} seconds.")  # Print the execution time
except subprocess.CalledProcessError as e:
    print(f"Command execution failed: {e}")
