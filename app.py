from flask import Flask, jsonify, render_template, request
from algorithms.base import SortAlgorithm
from algorithms.bubble_sort import BubbleSort
from algorithms.quick_sort import QuickSort
from algorithms.merge_sort import MergeSort
from benchmark import benchmark
import random
import importlib

app = Flask(__name__)

# Default available algorithms
DEFAULT_ALGOS = {
    "BubbleSort": BubbleSort,
    "QuickSort": QuickSort,
    "MergeSort": MergeSort
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_benchmark", methods=["POST"])
def run_benchmark():
    data = request.json
    algo_names = data.get("algorithms", [])
    array_size = int(data.get("array_size", 1000))
    num_runs = int(data.get("num_runs", 5))
    max_value = int(data.get("max_value", 1000))

    results = {}

    for name in algo_names:
        # Dynamically import algorithm if not default
        if name in DEFAULT_ALGOS:
            alg_class = DEFAULT_ALGOS[name]
        else:
            try:
                mod = importlib.import_module(f"algorithms.{name.lower()}")
                alg_class = getattr(mod, name)
            except Exception as e:
                results[name] = {"error": str(e)}
                continue

        alg = alg_class()
        times = []
        correct_all = True

        for _ in range(num_runs):
            arr = [random.randint(0, max_value) for _ in range(array_size)]
            test_arr = arr.copy()
            sorted_arr, elapsed = benchmark(alg, test_arr)
            times.append(elapsed)
            if sorted_arr != sorted(arr):
                correct_all = False

        avg_time = sum(times) / num_runs
        results[name] = {
            "average_time_ms": avg_time,
            "runs": times,
            "correct": correct_all
        }

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
