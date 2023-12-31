import time
import memory_profiler
from branchbound import main as branch_and_bound_main
from Greedy import main as greedy_main
from tabulate import tabulate  # Perlu instalasi library tabulate

def measure_execution_time_and_memory_usage(algorithm, *args):
    start_time = time.time()
    memory_usage = memory_profiler.memory_usage((algorithm, args), interval=0.1)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Ubah ke milidetik
    max_memory_usage = max(memory_usage)
    return execution_time, max_memory_usage

def save_results_to_txt(file_path, algorithm_name, execution_time, memory_usage, minimum_cost):
    with open(file_path, 'a') as file:
        file.write(f"Algorithm: {algorithm_name}\n")
        file.write(f"Execution Time: {execution_time:.4f} ms\n")  # Tambahkan ms di sini
        file.write(f"Memory Usage: {memory_usage} MB\n")
        file.write(f"Minimum Cost: {minimum_cost}\n")
        file.write("\n")

def print_table(header, data):
    print(tabulate(data, headers=header, tablefmt='fancy_grid'))

if __name__ == "__main__":
    dataset_files = ["custom_data_20.txt", "custom_data_200.txt", "custom_data_2000.txt"]

    output_file_path = f"results_all_datasets.txt"
    minimum_cost_file_path = f"minimum_costs.txt"

    header = ["Dataset", "Algorithm", "Execution Time (ms)", "Memory Usage (MB)", "Minimum Cost"]
    table_data = []

    for file_path in dataset_files:
        with open(file_path, 'r') as file:
            data_size = int(file.readline().strip())
            subsets = []
            costs = []
            
            # Skip the first line since it only contains the size
            file.readline()
            
            for line in file:
                line_data = line.strip().split()
                subsets.append(list(map(int, line_data[:-1])))
                costs.append(int(line_data[-1]))

        print(f"\nDataset: {file_path}")

        row_data_branch = ["Branch and Bound"]
        row_data_greedy = ["Greedy Algorithm"]

        print("\nBranch and Bound:")
        branch_execution_time, branch_memory_usage = measure_execution_time_and_memory_usage(branch_and_bound_main, data_size, subsets, costs)
        branch_result = branch_and_bound_main(data_size, subsets, costs)
        branch_cost = branch_result[0] if branch_result else None
        row_data_branch.extend([f"{branch_execution_time:.4f} ms", branch_memory_usage, min(costs)])
        print(f"Execution Time: {branch_execution_time:.4f} ms")
        print(f"Memory Usage: {branch_memory_usage} MB")
        print(f"Minimum Cost: {min(costs)}")

        print("\nGreedy Algorithm:")
        greedy_execution_time, greedy_memory_usage = measure_execution_time_and_memory_usage(greedy_main, data_size, subsets, costs)
        greedy_result = greedy_main(data_size, subsets, costs)
        greedy_cost = greedy_result[1] if greedy_result else None
        row_data_greedy.extend([f"{greedy_execution_time:.4f} ms", greedy_memory_usage, min(costs)])
        print(f"Execution Time: {greedy_execution_time:.4f} ms")
        print(f"Memory Usage: {greedy_memory_usage} MB")
        print(f"Minimum Cost: {min(costs)}")

        table_data.append([file_path, *row_data_branch])
        table_data.append([file_path, *row_data_greedy])

        # Menyimpan minimum cost ke dalam file txt
        with open(minimum_cost_file_path, 'a') as min_cost_file:
            min_cost_file.write(f"Dataset: {file_path}, Minimum Cost: {min(costs)}\n")

    print_table(header, table_data)
    print(f"\nResults appended to: {output_file_path}")
    print(f"Minimum costs saved to: {minimum_cost_file_path}\n")
