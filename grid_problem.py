def find_path(grid, paths, i, j, current_path=[]):
    # print(f'current_path : {current_path}')
    (m, n) = (len(grid), len(grid[0]))
    if i == m - 1 and j == n - 1:
        paths.append(current_path + [grid[i][j]])
        return
    current_path.append(grid[i][j])
    if 0 <= i < m and 0 <= j + 1 < n:
        find_path(grid, paths, i, j + 1, current_path)
    if 0 <= i + 1 < m and 0 <= j < n:
        find_path(grid, paths, i + 1, j, current_path)
    current_path.pop()


def num_of_paths(grid_size):
    grid = [[i for i in range(grid_size)] for j in range(grid_size)]
    paths = []

    print(f'grid : {grid}')
    find_path(grid, paths, 0, 0)

    print(f'paths: {paths}')
    return len(paths)


def number_of_paths_dynamic(grid_size):
    paths = [[0 for i in range(grid_size)] for j in range(grid_size)]

    paths[0][0] = 1
    queue = [(0, 0)]
    while queue:
        current = queue.pop(0)
        current_x = current[1]
        current_y = current[0]

        # if there is a neighbor underneath it
        under_neighbor_y = current_y + 1
        if 0 <= under_neighbor_y < grid_size:
            if (under_neighbor_y, current_x) not in queue:
                queue.append((under_neighbor_y, current_x))
            paths[under_neighbor_y][current_x] += paths[current_y][current_x]
        # if there is a neighbor to its right
        right_neighbor_x = current_x + 1
        if 0 <= right_neighbor_x < grid_size:
            if (current_y, right_neighbor_x) not in queue:
                queue.append((current_y, right_neighbor_x))

            paths[current_y][right_neighbor_x] += paths[current_y][current_x]

    return paths[grid_size - 1][grid_size - 1]


if __name__ == '__main__':
    # print(num_of_paths(3))
    print(number_of_paths_dynamic(4))

