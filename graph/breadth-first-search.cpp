#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

#define numNodes 7

// This implementation assumes the values of the nodes themselves are the indices for the prev and visited arrays, so n is the amount of nodes.

std::vector<std::vector<int>> g(numNodes);

void addEdge(int u, int v) {
    g[u].push_back(v);
    g[v].push_back(u);
}

void bfs(int start, int target) {
    bool v[numNodes] = {}; // default initialization to False
    std::unordered_map<int, int> prev;
    std::queue<int> q;

    q.push(start);
    v[start] = true;

    while(!q.empty()) {
        int curr = q.front();
        q.pop();

        // check if current node is target
        if (curr == target) {
            break;
        }
        std::cout << curr << " ";

        for (int i: g[curr]) {
            if (!v[i]) {
                q.push(i);
                v[i] = true;
                prev[i] = curr;
            }
        }
    }
    std::vector<int> path;
    
    // Traverse from target to start and store the path
    for (int i = target; i != start; i = prev.at(i)) {
        path.push_back(i);
    }
    path.push_back(start);  // Add the start node to the path

    // Print the path in reverse order
    std::cout << "\nPath " << start << "->" << target << ": ";
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << "\n";
}

int main(int argc, char *argv[]) {
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(1, 4);
    addEdge(2, 5);
    addEdge(2, 6);

    int start = 0, target = 6;
    bfs(start, target);

}

/*
             0
           /   \
          1     2
         / \   / \
        3   4 5   6

        0, 1, 2, 3, 4, 5, 6
*/