import os
import importlib.util
import inspect
import traceback
import datetime


def discover_tests(start_dir):
    """
    Discovers all test functions (named test_*) in files (named test_*.py)
    within a specified directory.
    """
    discovered_tests = []
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                module_name = file[:-3]
                file_path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for name, func in inspect.getmembers(module, inspect.isfunction):
                    if name.startswith("test_"):
                        discovered_tests.append(func)
    return discovered_tests


def run_tests(tests):
    """
    Runs a list of discovered test functions and reports the results.
    """
    results = {"passed": 0, "failed": 0, "failures": [], "test_details": []}
    total_tests = len(tests)

    for i, test_func in enumerate(tests):
        status = "PASS"
        error = ""
        try:
            test_func()
            results["passed"] += 1
        except AssertionError as e:
            status = "FAIL"
            error = str(e)
            results["failed"] += 1
            results["failures"].append({"name": test_func.__name__, "error": error})

        results["test_details"].append({"name": test_func.__name__, "status": status, "error": error})
    return results


def generate_html_report(results):
    """
    Generates a simple HTML report from the test results.
    """
    passed_count = results['passed']
    failed_count = results['failed']
    total_count = passed_count + failed_count
    pass_percentage = (passed_count / total_count * 100) if total_count > 0 else 0

    failure_details_html = ""
    for failure in results["failures"]:
        failure_details_html += f"<h4>{failure['name']}</h4><pre>{failure['error']}</pre>"

    test_details_rows_html = ""
    for detail in results["test_details"]:
        status_class = "pass" if detail["status"] == "PASS" else "fail"
        test_details_rows_html += f"<tr><td>{detail['name']}</td><td class='{status_class}'>{detail['status']}</td></tr>"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Test Report</title>
        <style>
            body {{ font-family: sans-serif; }}
            h1, h2, h3, h4 {{ color: #333; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ padding: 8px; border: 1px solid #ddd; text-align: left; }}
            thead {{ background-color: #f2f2f2; }}
            .summary {{ margin-bottom: 2em; }}
            .pass {{ color: green; font-weight: bold; }}
            .fail {{ color: red; font-weight: bold; }}
            pre {{ background-color: #eee; padding: 1em; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Test Execution Report</h1>
        <div class="summary">
            <h2>Summary</h2>
            <p><strong>Run Date:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Total Tests:</strong> {total_count}</p>
            <p class="pass"><strong>Passed:</strong> {passed_count}</p>
            <p class="fail"><strong>Failed:</strong> {failed_count}</p>
            <p><strong>Pass Percentage:</strong> {pass_percentage:.2f}%</p>
        </div>

        <h2>Test Details</h2>
        <table>
            <thead><tr><th>Test Name</th><th>Status</th></tr></thead>
            <tbody>{test_details_rows_html}</tbody>
        </table>

        <h2>Failures</h2>
        {failure_details_html if failed_count > 0 else "<p>No failures.</p>"}
    </body>
    </html>
    """

    # Ensuring the reports directory exists
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/report.html", "w") as f:
        f.write(html_content)
    print("\nHTML report generated at reports/report.html")


if __name__ == "__main__":
    all_tests = discover_tests("tests")
    print(f"Found {len(all_tests)} tests.")

    run_results = run_tests(all_tests)

    generate_html_report(run_results)