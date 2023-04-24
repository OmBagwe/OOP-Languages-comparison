import subprocess
import json
import os

languages = {
    "java": {
        "extension": ".java",
        "compile_command": "javac",
        "run_command": "java"
    },
    "python": {
        "extension": ".py",
        "compile_command": "",
        "run_command": "python"
    },
    "ruby": {
        "extension": ".rb",
        "compile_command": "",
        "run_command": "ruby"
    }
}

benchmarks = {
    "BenchmarkMemory": "BenchmarkMemory",
    "BenchmarkProcessingSpeed": "BenchmarkProcessingSpeed",
    "BenchmarkEfficiency": "BenchmarkEfficiency"
}


def run_benchmark(benchmark, language):
    file_name = f"{benchmark}{languages[language]['extension']}"
    if language == "java":
        compile_command = f"{languages[language]['compile_command']} -cp .;\"C:\\Users\\Om Bagwe\\Downloads\\gson-2.8.9.jar\" {file_name}"
        print(f"Running compile command: {compile_command}")  # Add this line to print the compile command
        subprocess.run(compile_command, shell=True, check=True)
        file_name = file_name.replace(".java", "")

    if language == "java":
        command = f"{languages[language]['run_command']} -cp .;\"C:\\Users\\Om Bagwe\\Downloads\\gson-2.8.9.jar\" {file_name}"
    else:
        command = f"{languages[language]['run_command']} {file_name}"

    # Execute the benchmark for the specific language
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return json.loads(result.stdout.decode("utf-8").strip())



def main():
    results = {}

    for language in languages:
        results[language] = {}
        for benchmark in benchmarks:
            benchmark_result = run_benchmark(benchmark, language)
            results[language][benchmark] = benchmark_result

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
