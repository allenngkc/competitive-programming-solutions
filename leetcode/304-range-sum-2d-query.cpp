class NumMatrix {
    vector<vector<int>> ps;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        ps.assign(n + 1, vector<int>(m + 1, 0));
        for (auto i = 1; i <= n; ++i) {
            for(auto j = 1; j <= m; ++j) {
                ps[i][j] = matrix[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return ps[row2+1][col2+1] - ps[row2+1][col1] - ps[row1][col2+1] + ps[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */