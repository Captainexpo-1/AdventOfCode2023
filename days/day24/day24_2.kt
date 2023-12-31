import java.io.File
import kotlin.collections.HashSet

fun main() {
    val f = File("../data/24.txt").readLines().map { it.toList() }

    val start = Pair(0, f[0].indexOf('.'))
    val end = Pair(f.size - 1, f.last().indexOf('.'))

    val longestPath = longestPathInGridWithPathVisualization(f, start, end)
    println(longestPath.length - 1)
    println(visualizePath(f, longestPath.path))
}

data class PathResult(var length: Int, var path: MutableList<Pair<Int, Int>>)

fun longestPathInGridWithPathVisualization(grid: List<List<Char>>, start: Pair<Int, Int>, end: Pair<Int, Int>): PathResult {
    val rows = grid.size
    val cols = grid[0].size
    val longestPath = PathResult(0, mutableListOf())
    val visited = HashSet<Pair<Int, Int>>()

    fun is_valid(r: Int, c: Int, lr: Int, lc: Int, useSlope: Boolean = false): Boolean {
        if (!useSlope) return r in 0 until rows && c in 0 until cols && grid[r][c] != '#'
        val diff = Pair(r - lr, c - lc)
        val curSqr = grid[lr][lc]
        if (Pair(r, c) in visited) return false
        return when (curSqr) {
            '>' -> diff == Pair(0, 1)
            '<' -> diff == Pair(0, -1)
            '^' -> diff == Pair(-1, 0)
            'v' -> diff == Pair(1, 0)
            else -> r in 0 until rows && c in 0 until cols && grid[r][c] != '#'
        }
    }

    fun dfs(r: Int, c: Int, path: MutableList<Pair<Int, Int>>) {
        if (Pair(r, c) == end) {
            if (path.size > longestPath.length) {
                longestPath.length = path.size
                longestPath.path = ArrayList(path)
            }
            return
        }

        visited.add(Pair(r, c))

        val directions = listOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))
        for ((dr, dc) in directions) {
            val nr = r + dr
            val nc = c + dc
            if (is_valid(nr, nc, r, c)) {
                path.add(Pair(nr, nc))
                dfs(nr, nc, path)
                path.removeAt(path.size - 1)
            }
        }

        visited.remove(Pair(r, c))
    }

    dfs(start.first, start.second, mutableListOf(start))
    return longestPath
}

fun visualizePath(grid: List<List<Char>>, path: List<Pair<Int, Int>>): String {
    val gridWithPath = grid.map { it.toMutableList() }
    path.forEach { (r, c) -> gridWithPath[r][c] = '*' }

    return gridWithPath.joinToString("\n") { it.joinToString("") }
}
