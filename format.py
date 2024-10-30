import subprocess


def run_black():
    # Check if Black is installed
    try:
        subprocess.run(["black", "."], check=True)
        print("Formatting complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Black. Make sure you have it installed: {e}")


if __name__ == "__main__":
    run_black()
