#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <string>

struct PathResult {
    int length;
    std::vector<std::pair<int, int>> path;
};

bool is_valid(const std::vector<std::vector<char>>& grid, int r, int c, int lr, int lc, bool use_slope, const std::set<std::pair<int, int>>& visited) {
    int rows = grid.size();
    int cols = grid[0].size();
    if (!use_slope) return r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] != '#';

    int dr = r - lr;
    int dc = c - lc;
    char cur_sqr = grid[lr][lc];
    if (visited.find({r, c}) != visited.end()) return false;
    if (cur_sqr == '>' && !(dr == 0 && dc == 1)) return false;
    if (cur_sqr == '<' && !(dr == 0 && dc == -1)) return false;
    if (cur_sqr == '^' && !(dr == -1 && dc == 0)) return false;
    if (cur_sqr == 'v' && !(dr == 1 && dc == 0)) return false;
    return r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] != '#';
}

void dfs(const std::vector<std::vector<char>>& grid, int r, int c, std::vector<std::pair<int, int>>& path, PathResult& longest_path, std::set<std::pair<int, int>>& visited, const std::pair<int, int>& end) {
    if (std::make_pair(r, c) == end) {
        if (path.size() > longest_path.length) {
            longest_path.length = path.size();
            longest_path.path = path;

            // Print the current longest path
            std::cout << "Current Longest Path Length: " << longest_path.length - 1 << std::endl;
        }
        return;
    }
    std::cout << "FOUND PATH" << longest_path.length -1 << std::endl;

    visited.insert({r, c});
    const std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (const auto& dir : directions) {
        int nr = r + dir.first;
        int nc = c + dir.second;
        if (is_valid(grid, nr, nc, r, c, false, visited)) {
            path.push_back({nr, nc});
            dfs(grid, nr, nc, path, longest_path, visited, end);
            path.pop_back();
        }
    }
    visited.erase({r, c});
}

std::string visualize_path(const std::vector<std::vector<char>>& grid, const std::vector<std::pair<int, int>>& path) {
    std::vector<std::vector<char>> grid_with_path = grid;
    for (const auto& p : path) {
        grid_with_path[p.first][p.second] = '*';
    }

    std::string result;
    for (const auto& row : grid_with_path) {
        for (char c : row) {
            result.push_back(c);
        }
        result.push_back('\n');
    }
    return result;
}

int main() {
    std::ifstream file("../data/24.txt");
    std::string line;
    std::vector<std::vector<char>> grid;

    while (std::getline(file, line)) {
        grid.push_back(std::vector<char>(line.begin(), line.end()));
    }

    int start_r = 0, start_c = 0, end_r = grid.size() - 1, end_c = 0;
    for (int c = 0; c < grid[0].size(); ++c) {
        if (grid[0][c] == '.') {
            start_c = c;
            break;
        }
    }
    for (int c = 0; c < grid[end_r].size(); ++c) {
        if (grid[end_r][c] == '.') {
            end_c = c;
            break;
        }
    }

    std::vector<std::pair<int, int>> path;
    std::set<std::pair<int, int>> visited;
    PathResult longest_path {0, {}};

    dfs(grid, start_r, start_c, path, longest_path, visited, {end_r, end_c});
    std::cout << "Longest Path Length: " << longest_path.length - 1 << std::endl;
    std::cout << visualize_path(grid, longest_path.path) << std::endl;

    return 0;
}
