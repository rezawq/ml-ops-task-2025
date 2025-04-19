"""
Test script to demonstrate printing Python version, path,
environment information, and system-wide Python details
when running within a virtual environment.
It also includes a basic PySpark initialization and usage example.
"""

import os
import subprocess
import sys

# Import SparkSession from PySpark library
from pyspark.sql import SparkSession

def get_system_python_info():
    """
    Attempts to find the system-wide Python interpreter and returns its
    version and executable path. This is useful when the script is run
    within a virtual environment and you need information about the base
    system Python.
    """
    # Common locations for system Python on Linux and macOS.
    # You might need to adjust this list based on your specific OS
    # or custom Python installations.
    possible_system_paths = ["/usr/bin/python3", "/usr/bin/python", "/usr/local/bin/python3", "/usr/local/bin/python"]

    system_python_executable = None
    for path in possible_system_paths:
        # Check if the path exists and is an executable file
        if os.path.exists(path) and os.access(path, os.X_OK):
            system_python_executable = path
            break

    if system_python_executable:
        try:
            # Execute the system Python interpreter to get its version
            version_output = subprocess.run(
                [system_python_executable, "--version"],
                capture_output=True,
                text=True,
                check=True,  # Raise an exception for non-zero exit codes
            )
            # The version string is typically on the first line of stdout
            system_python_version = version_output.stdout.strip()

            # Execute the system Python interpreter to get its executable path
            executable_output = subprocess.run(
                [system_python_executable, "-c", "import sys; print(sys.executable)"],
                capture_output=True,
                text=True,
                check=True,  # Raise an exception for non-zero exit codes
            )
            system_python_path = executable_output.stdout.strip()

            return system_python_version, system_python_path
        except subprocess.CalledProcessError as e:
            print(f"Error getting system Python info: {e}")
            print(f"Stderr: {e.stderr}")
            return None, None
        except FileNotFoundError:
            print(f"System Python executable not found at: {system_python_executable}")
            return None, None
    else:
        print("Could not find a common system-wide Python executable.")
        return None, None

if __name__ == "__main__":
    # Initialize Spark Session
    # This creates a Spark application and gets or creates a SparkSession
    spark = SparkSession.builder \
        .appName("TestSparkJob") \
        .getOrCreate()

    # Basic output to indicate the script is running
    print("Hello, World!")

    # Print the current working directory where the script is being executed
    print(f"Current Working Directory: {os.getcwd()}")

    # Print the environment variables of the current process
    print("\nEnvironment Variables:")
    for key, value in os.environ.items():
        print(f"{key}={value}")
    print("-" * 20)

    # Print the Python version that is currently running the script
    # When inside a venv, this will be the venv's Python
    print(f"\nCurrent Python Version (within venv if active): {sys.version}")

    # Print the full path to the Python executable that is currently running the script
    # When inside a venv, this will be the venv's Python executable
    print(f"Full Path to Python Executable (within venv if active): {sys.executable}")
    print("-" * 20)

    # Attempt to get and print information about the system-wide Python
    system_version, system_path = get_system_python_info()

    if system_version and system_path:
        print("System-wide Python Information:")
        print(f"  System Python Version: {system_version}")
        print(f"  System Python Executable Path: {system_path}")
        print("-" * 20)
    else:
        print("Could not retrieve system-wide Python information.")
        print("-" * 20)

    # Create a simple Spark DataFrame to demonstrate Spark functionality
    data = [(1, "test"), (2, "example")]
    columns = ["id", "value"]
    df = spark.createDataFrame(data, columns)

    print("\nSample Spark DataFrame:")
    df.show()

    # Important: Always stop the SparkSession to release resources
    spark.stop()
    print("\nSparkSession stopped.")