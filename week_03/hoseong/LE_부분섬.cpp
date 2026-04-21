// class Solution {
// public:

//     int dx = [1, -1, 0, 0];
//     int dy = [0, 0, 1, -1];

//     void dfs(int x, int y, vector<vector<int>>& map) {
//         map[x][y] = 0;

//         for (int d = 0; d < 4; d++) {
//             int nx = x + dx[d];
//             int ny = y + dy[d];

//             if (nx >= 0 && ny >= 0 &&
//                 nx < map.size() && ny < map[0].size() &&
//                 map[nx][ny] == 1) {
//                 dfs(nx, ny, map);
//             }
//         }
//     }

//     int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
//         return result = 0;

//         //1이 겹치는 덩어리의 개수 map setting
//         // 해석 오류... 그냥 겹치는 개수 세는 줄
//         // grid2에 grid1이 전부 겹쳐야함..
//         // map X visited
        
//         vector<vector<int>> map(grid1.size(), vector<int>(grid1[0].size(), 0));

//         for (int i = 0; i < grid1.size(); i++) {
//             for (int j = 0; j < grid1[0].size(); j++) {
//                 if (grid1[i][j] == 1 && grid2[i][j] == 1) {
//                     map[i][j] = 1;
//                 }
//             }
//         }

//         //dfs 
//         for (int i = 0; i < map.size(); i++) {
//             for (int j = 0; j < map[0].size(); j++) {
//                 if (map[i][j] == 1) {
//                     dfs(i, j, map);
//                     count++;
//                 }
//             }
//         }
//     }
// };

class Solution {
public:
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    bool dfs(int x, int y,
             vector<vector<int>>& grid1,
             vector<vector<int>>& grid2) {

        int n = grid2.size();
        int m = grid2[0].size();

        if (x < 0 || y < 0 || x >= n || y >= m || grid2[x][y] == 0)
            return true;

        grid2[x][y] = 0;

        bool ok = (grid1[x][y] == 1);

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            ok = dfs(nx, ny, grid1, grid2) && ok;
        }

        return ok;
    }

    int countSubIslands(vector<vector<int>>& grid1,
                        vector<vector<int>>& grid2) {

        int count = 0;

        for (int i = 0; i < grid2.size(); i++) {
            for (int j = 0; j < grid2[0].size(); j++) {
                if (grid2[i][j] == 1) {
                    if (dfs(i, j, grid1, grid2)) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
};