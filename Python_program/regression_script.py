import os
import subprocess
import csv
import datetime

# Configuration parameters
SIMULATOR = "vcs"  # Change based on simulator (e.g., vcs, questa, xcelium)
TOP_MODULE = "tb_top"
COMPILE_CMD = f"{SIMULATOR} -full64 -sverilog -debug_all +define+UVM_NO_DPI -top {TOP_MODULE} -o simv"
RUN_CMD = "./simv +UVM_TESTNAME={testname} +ntb_random_seed={seed} -l {logfile}"

# Test list
TEST_LIST = [
    {"name": "basic_test", "seed": 12345},
    {"name": "edge_case_test", "seed": 67890},
    {"name": "error_injection_test", "seed": 11111},
]

# Directories
RESULTS_DIR = "results"
LOG_DIR = os.path.join(RESULTS_DIR, "logs")
REPORT_FILE = os.path.join(RESULTS_DIR, "regression_report.csv")

def setup_directories():
    """Create required directories for results and logs."""
    os.makedirs(LOG_DIR, exist_ok=True)

def compile_design():
    """Compile the design and testbench."""
    print("Compiling the design...")
    result = subprocess.run(COMPILE_CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Compilation failed. Check the logs.")
        print(result.stderr.decode())
        exit(1)
    print("Compilation successful.")

def run_test(testname, seed):
    """Run a single test case."""
    logfile = os.path.join(LOG_DIR, f"{testname}_seed{seed}.log")
    cmd = RUN_CMD.format(testname=testname, seed=seed, logfile=logfile)
    print(f"Running test: {testname} with seed {seed}...")
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Test {testname} failed to execute. Check the log: {logfile}")
        return "FAIL"
    
    # Parse logfile for pass/fail status
    with open(logfile, 'r') as log:
        for line in log:
            if "UVM_INFO" in line and "TEST PASSED" in line:
                return "PASS"
            if "UVM_ERROR" in line:
                return "FAIL"
    return "UNKNOWN"

def generate_report(results):
    """Generate a CSV report of the regression run."""
    print("Generating regression report...")
    with open(REPORT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Test Name", "Seed", "Result"])
        for result in results:
            writer.writerow([result["name"], result["seed"], result["status"]])
    print(f"Report generated: {REPORT_FILE}")

def main():
    """Main function for running the regression."""
    setup_directories()
    compile_design()

    results = []
    for test in TEST_LIST:
        status = run_test(test["name"], test["seed"])
        results.append({"name": test["name"], "seed": test["seed"], "status": status})

    generate_report(results)
    print("Regression completed.")

if __name__ == "__main__":
    main()

