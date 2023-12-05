import random

def generate_custom_data(data_size) -> (set, list, list):
    universe_set = set(range(1, data_size + 1))
    subsets_list = []
    covered_set = set() 
    max_list_size = data_size // 200
    while len(subsets_list) < max_list_size or covered_set != universe_set:  
        temp_subset = sorted(list(random.sample(list(universe_set), random.randint(1, data_size))))
        subsets_list.append(temp_subset)
        covered_set.update(temp_subset)
    costs_list = [random.randint(1, 100) for _ in range(len(subsets_list))]
    return universe_set, subsets_list, costs_list

def save_to_custom_txt(file_path, universe_set, subsets_list, costs_list):
    with open(file_path, 'w') as file:
        file.write(f"{len(universe_set)}\n")
        for subset, cost in zip(subsets_list, costs_list):
            file.write(" ".join(map(str, subset)) + f" {cost}\n")

if __name__ == "__main__":
    sizes = [20, 200, 2000]

    for size in sizes:
        universe, subsets, costs = generate_custom_data(size)
        save_to_custom_txt(f"custom_data_{size}.txt", universe, subsets, costs)
