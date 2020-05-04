from pathlib import Path
from time import perf_counter_ns
from statistics import mean
from typing import List, Tuple
import csv

# import team class 1
# from KerasExample.KerasLoader import KerasLoader as Loader

# ...
# import team class 2
from PyTorchExample.PyTorchLoader import PyTorchLoader as Loader

def evaluate():
    # import team class 1
    # base_path = Path("./KerasExample").resolve()

    # import team class 1
    base_path = Path("./PyTorchExample").resolve()
    timings = []
    results = {}

    for i in range(1, 7):
        loader = Loader(i, str(base_path))
        filenames = load_filenames(i)=
        partition_results = []
        # measure execution time
        time_start = perf_counter_ns()

        for cl, filename in filenames:
            result = loader.predict(filename)
            partition_results.append((result, cl))
        # measure execution times    
        time_end = perf_counter_ns()
        total_time = time_end - time_start
        timings.append(total_time)
        result[i] = partition_results
        
    print(f"Average time evaluating a partition: {mean(timings)}")

    #final_res = mean([calculate_metrics(results[x]) for x in results])
    final_res = [(key, calculate_metrics(results[key])) for key in results]


def load_filenames(partition: int) -> List[Tuple[str, str]]:
    with open(f"Test_files/Test_{partition}.txt", "r") as f:
        rows = csv.reader(f)
        return list(rows)


def calculate_metrics(true_values: List[int], predicted_values: List[Tuple[str, float]]):
    threshold_values = [i/10 for i in range(11)]

    # -1, -2 are attacks, +1 is not an attack -> True when attack, False otherwise
    true_boolean_values = [int(x) < 0 for x in true_values]
    fars = []
    frrs = []
    for threshold in threshold_values:
        # if above threshold it's an attack, if below, it's normal
        threshold_results = [x >= threshold for _, x in predicted_values]

        false_acceptance_rate = sum([1 for ex, res in zip(true_boolean_values, threshold_results) if ex and not res]) / len(true_boolean_values)
        fars.append(false_acceptance_rate)

        false_rejection_rate = sum([1 for ex, res in zip(true_boolean_values, threshold_results) if not ex and res]) / len(true_boolean_values)
        frrs.append(false_rejection_rate)

    # metric = ?
    return metric

evaluate()