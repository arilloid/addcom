import subprocess

def run_linter():
    # Run Ruff with autofix enabled
    try:
        subprocess.run(["ruff", "check", "--fix"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Ruff. Make sure you have it installed: {e}")

if __name__ == "__main__":
    run_linter()
