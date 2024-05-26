import subprocess

def run_script(script_path):
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script_path}: {result.stderr}")
        exit(result.returncode)

def main():
    scripts = [
        'src/data/make_dataset.py',
        'src/features/build_features.py',
        'src/split/split_data.py',
        'src/models/train_model.py',
        'src/models/evaluate_model.py',
        'src/data/generate_new_data.py',  
        'src/models/predict_model.py',
        'src/visualization/visualize.py'
    ]
    
    for script in scripts:
        print(f"Running {script}...")
        run_script(script)
        print(f"Finished {script}\n")

if __name__ == '__main__':
    main()
