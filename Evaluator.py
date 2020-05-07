from pathlib import Path
from time import perf_counter_ns
from statistics import mean
from typing import List, Tuple, Dict
import csv

# import team class 1
# from KerasExample.KerasLoader import KerasLoader as Loader

# ...
# import team class 2
from PyTorchExample.PyTorchLoader import PyTorchLoader as Loader

# You have to change this to the name of the folder which you are importing
TEAM_NAME = "PyTorchExample"

def evaluate():
    # import team class 1
    # base_path = Path("./KerasExample").resolve()

    # import team class 1
    base_path = Path(f"./{TEAM_NAME}").resolve()
    timings = []
    results = {}

    for i in range(1, 7):
        loader = Loader(i, str(base_path))
        filenames = load_filenames(i)
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
        results[str(i)] = partition_results

    print(f"Average time evaluating a partition: {mean(timings)}")

    #final_res = mean([calculate_metrics(results[x]) for x in results])
    final_res = [(key, calculate_metrics(results[key])) for key in results]

    # Calculate average execution time and append to end of list
    timings.append(mean(timings))

    avg_apcer = mean([x["apcer"] for _, x in final_res])
    avg_bpcer = mean([x["bpcer"] for _, x in final_res])
    avg_acer = mean([x["acer"] for _, x in final_res])

    final_res.append(("avg", {"apcer": avg_apcer, "bpcer": avg_bpcer, "acer" : avg_acer}))
    save_results(final_res, timings)


def save_results(results: List[Tuple[str, Dict]], timings: List[int]):
    filename = f"{TEAM_NAME}_results.csv"
    with open(filename, 'w') as fp:
        fp.write("model, apcer, bpcer, acer, time(ns)\n")
        for (model, result), timing in zip(results, timings):
            fp.write(f"{model}, {result['apcer']}, {result['bpcer']}, {result['acer']}, {timing}\n")


def load_filenames(partition: int) -> List[Tuple[str, str]]:
    with open(f"Test_files/Test_{partition}.txt", "r") as f:
        rows = csv.reader(f)
        return list(rows)


def calculate_metrics(values: List[Tuple[float, str]]) -> Tuple[float, float, float]:
    predicted_values = [x for (x, _) in values]
    true_values = [x for (_, x) in values]

    threshold_values = [i/100 for i in range(101)]

    # -1, -2 are attacks, +1 is not an attack -> True when attack, False otherwise
    true_boolean_values = [int(x) < 0 for x in true_values]

    attack_count = true_boolean_values.count(False)
    bonafide_count = true_boolean_values.count(True)

    apcers = []
    bpcers = []
    acers = []

    for threshold in threshold_values:
        # if above threshold it's an attack, if below, it's normal
        threshold_results = [x >= threshold for x in predicted_values]

        # APCER
        false_acceptance_rate = 1 - (1/attack_count) * sum([1 for ex, res in zip(true_boolean_values, threshold_results) if ex and res])
        apcers.append(false_acceptance_rate)

        # BPCER
        false_rejection_rate = sum([1 for ex, res in zip(true_boolean_values, threshold_results) if not ex and res]) / bonafide_count
        bpcers.append(false_rejection_rate)

        # ACER
        acer = (false_acceptance_rate + false_rejection_rate) / 2
        acers.append(acer)

    min_i = 0
    min_val = 100000
    for i, (apcer, bpcer) in enumerate(zip(bpcers, apcers)):
        dif = abs(apcer - bpcer)
        if dif < min_val:
            min_i = i
            min_val = dif

    return {"apcer": apcers[min_i], "bpcer": bpcers[min_i], "acer" : acers[min_i]}


evaluate()