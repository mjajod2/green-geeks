from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ExtendedTyping.Typing import SupportsStr
from ProgressManager.Output.OutputProcedure import OutputProcedure as output

from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath
import pandas as pd
import random

import subprocess


class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = "new_runner_experiment"

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path            = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 1000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""

        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN       , self.before_run       ),
            (RunnerEvents.START_RUN        , self.start_run        ),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT         , self.interact         ),
            (RunnerEvents.STOP_MEASUREMENT , self.stop_measurement ),
            (RunnerEvents.STOP_RUN         , self.stop_run         ),
            # (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT , self.after_experiment )
        ])
        self.run_table_model = None  # Initialized later

        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""
        factor1 = FactorModel("example_factor1", ["example_treatment1"]) # just one factor with one level
        
        self.run_table_model = RunTableModel(
            factors=[factor1], data_columns=["timestamp", "tag", "duration", "package_0", "core_0", "input_file"] # Adjust columns
        )

        return self.run_table_model


    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.before_experiment() called!")

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""

        output.console_log("Config.before_run() called!")

    def start_run(self, context: RunnerContext) -> None:
        """Apply both techniques to each input file, generate output files, and then run the output files to measure energy."""
        output.console_log("Config.start_run() called!")


        # Output directory (you can modify this as needed)
        output_dir = Path("/home/mihir/Desktop/newProject/green-geeks/experiment-runner/examples/optimized_loops/")

        # List of techniques with corresponding command options
        techniques = [
            ['-u', 'unrolling'],  # Loop unrolling
            ['-i', 'inline']      # Inlining
        ]
        
        # for i in range(1,101):
        #     output_file = output_dir / f"optimized_loop{i}_unroll.py"
        #     if not output_file.exists():
        #         continue
        #     print('righr')
        #     run_command = ['sudo', 'python3', str(output_file)]
        #     result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     if result.returncode != 0:
        #         print(f"Error in optimization command: {result.stderr.decode('utf-8')}")
        #     energy_output = result.stdout.decode('utf-8')
        #     print("Energy Measurement STDOUT:", energy_output)

        #     self.populate_run_data(context, energy_output, "unrolled", f"optimized_loop{i}_unroll.py")

        # for i in range(1,101):
        #     output_file = output_dir / f"optimized_loop{i}_unswitch.py"
        #     if not output_file.exists():
        #         continue
        #     print('righr')
        #     run_command = ['sudo', 'python3', str(output_file)]
        #     result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     if result.returncode != 0:
        #         print(f"Error in optimization command: {result.stderr.decode('utf-8')}")
        #     energy_output = result.stdout.decode('utf-8')
        #     print("Energy Measurement STDOUT:", energy_output)

        #     self.populate_run_data(context, energy_output, "unswitched", f"optimized_loop{i}_unswitch.py")

        # for i in range (1,101):
        #     output_file = output_dir / f"optimized_loop{i}_earlyT.py"
        #     print('righr')
        #     if not output_file.exists():
        #         continue
        #     run_command = ['sudo', 'python3', str(output_file)]
        #     result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     if result.returncode != 0:
        #         print(f"Error in optimization command: {result.stderr.decode('utf-8')}")
        #     energy_output = result.stdout.decode('utf-8')
        #     print("Energy Measurement STDOUT:", energy_output)

        #     self.populate_run_data(context, energy_output, "earlyT", f"optimized_loop{i}_earlyT.py")
            
        # for i in range (1,101):
        #     output_file = output_dir / f"optimized_loop{i}_var.py"
        #     print('righr')
        #     if not output_file.exists():
        #         continue
        #     run_command = ['sudo', 'python3', str(output_file)]
        #     result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     if result.returncode != 0:
        #         print(f"Error in optimization command: {result.stderr.decode('utf-8')}")
        #     energy_output = result.stdout.decode('utf-8')
        #     print("Energy Measurement STDOUT:", energy_output)

        #     self.populate_run_data(context, energy_output, "var", f"optimized_loop{i}_var.py")

        techniques = [
            ('_unroll', 'unrolled'),
            ('_unswitch', 'unswitched'),
            ('_earlyT', 'earlyT'),
            ('_var', 'var')
        ]

        for i in range(1, 101):
            for suffix, technique_name in techniques:
                output_file = output_dir / f"optimized_loop{i}{suffix}.py"
                if output_file.exists():
                    run_command = ['sudo', 'python3', str(output_file)]
                    result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if result.returncode == 0:
                        energy_output = result.stdout.decode('utf-8')
                        print("Energy Measurement STDOUT:", energy_output)
                        self.populate_run_data(context, energy_output, technique_name, output_file)


        # Iterate over input files and apply both techniques
        # for idx, input_file in enumerate(input_files):
        #     for technique_params in techniques:
        #         technique_option, technique_name = technique_params

        #         # Define the output file name
        #         output_file = output_dir / f"{Path(input_file).stem}_{technique_name}.py"

        #         # Construct the subprocess command to optimize the input file
        #         # optimize_command = ['python3', '/home/mihir/Desktop/green-geeks/experiment-runner/examples/PythonLoopOptimizer/src/main.py', 
        #         #                     '-f', input_file, '-o', str(output_file)] + [technique_option]

        #         # # Log the command for debugging
        #         # print(f"Running optimization command: {' '.join(optimize_command)}")

        #         # # Run the optimization command using subprocess
        #         # subprocess.run(optimize_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        #         # After generating the output file, run the output file to measure energy consumption
        #         run_command = ['sudo', 'python3', str(output_file)]

        #         # Log the command for debugging
        #         print(f"Running output file command: {' '.join(run_command)}")

        #         # Run the output file and capture the energy measurement output
        #         result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #         if result.returncode != 0:
        #             print(f"Error in optimization command: {result.stderr.decode('utf-8')}")
        #         # Capture the energy measurement STDOUT and pass it to populate_run_data
        #         energy_output = result.stdout.decode('utf-8')
        #         print("Energy Measurement STDOUT:", energy_output)

        #         # Pass the energy output and the technique name to populate_run_data
        #         self.populate_run_data(context, energy_output, technique_name, output_file)





    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        output.console_log("Config.start_measurement() called!")

    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""

        output.console_log("Config.interact() called!")

    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""

        output.console_log("Config.stop_measurement called!")

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""

        output.console_log("Config.stop_run() called!")
    

        # self.profiler.wait()

    #     stdout, stderr = self.profiler.communicate()

    # # Optionally print or log the stdout and stderr
    #     print("STDOUT:", stdout.decode('utf-8'))
    #     print("STDERR:", stderr.decode('utf-8'))

    def populate_run_data(self, context: RunnerContext, energy_output: str, technique_name: str, input_file: str) -> None:
        """Parse and process energy measurement data from measure_energy decorator, then store it in run_table.csv."""
        output.console_log("Config.populate_run_data() called!")

        # Split the energy_output by lines
        output_lines = energy_output.strip().splitlines()
        print(output_lines)
        # Check if there are any lines to process
        if not output_lines:
            print(f"No valid data output from energy measurement for {input_file} using {technique_name}.")
            return

        # Initialize an empty list to collect the parsed rows
        rows = []

        # Loop through the output lines and parse energy measurement data
        for line in output_lines:
            print('UEYE',line)
            try:
                # Parse each key-value pair from the line (assuming they are separated by ';')
                data = line.strip().split(';')

                # Create a dictionary to store the parsed data
                parsed_data = {}
                for item in data:
                    key, value = item.split(':')
                    parsed_data[key.strip()] = value.strip()

                # Append the parsed data to the list of rows
                rows.append({
                    'timestamp': parsed_data.get('begin timestamp', ''),
                    'tag': parsed_data.get('tag', ''),
                    'duration': parsed_data.get('duration', ''),
                    'package_0': parsed_data.get('package_0', ''),
                    'core_0': parsed_data.get('core_0', ''),
                    'input_file': input_file
                })

            except ValueError as e:
                print(f"Error parsing line: {e}")
                continue

        # Convert the list of rows to a DataFrame
        df = pd.DataFrame(rows)

        # Ensure there are valid rows to write to the CSV
        if not df.empty:
            # Add __run_id and technique name to columns manually
            df['__run_id'] = 'run_0_repetition_0'
            df['__done'] = 'DONE'
            df['example_factor1'] = technique_name  # Insert the applied technique here
            df['input_file'] = input_file

            # Reorder columns to match the CSV format
            df = df[['__run_id', '__done', 'example_factor1', 'timestamp', 'tag', 'duration', 'package_0', 'core_0', 'input_file']]

            # Save the DataFrame to a CSV file, appending each row
            run_table_path = context.run_dir / 'run_table.csv'
            df.to_csv(run_table_path, mode='a', header=not run_table_path.exists(), index=False)

            print(f"Data successfully written to {run_table_path}.")
        else:
            print(f"No valid energy measurement data to write for {input_file} using {technique_name}.")






    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.after_experiment() called!")

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None