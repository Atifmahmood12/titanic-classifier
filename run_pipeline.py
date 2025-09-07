
import subprocess
import os

# List of output files to clean before running pipeline
output_files = [
    'data/train.csv',
    'data/features.csv',
    'data/labels.csv',
    'data/model.joblib',
    'data/predictions.csv',
]

for file in output_files:
    if os.path.exists(file):
        print(f"Removing {file}...")
        os.remove(file)

# List of scripts to run in order
scripts = [
    'data/prep_data.py',
    'src/data_prep.py',
    'src/train.py',
    'src/infer.py',
    'src/evaluate.py',
    'src/visualize.py',
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run(['python', script])
    if result.returncode != 0:
        print(f"Error running {script}. Stopping pipeline.")
        break
    else:
        print(f"Finished {script}.")
