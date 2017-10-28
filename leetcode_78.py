class Solution {
public:

    vector<vector<int>> subsets(vector<int>& nums) {
    
        vector<vector<int>> results_final;
        vector<int> result;
        
        if (nums.size() < 0)
            return results_final;
        generateSubset(nums, 0, result, results_final);
        
        return results_final;
        
    }
    void generateSubset(vector<int>& input, int i_, vector<int>& result, vector<vector<int>>& result_final)
    {
        /*
        //Print the subset
        for (int q = 0; q < result.size(); q++)
            cout << result[q] << "\t";
        cout << endl;
        */
        result_final.push_back(result);
        //if the input is done, return
        if (i_ == input.size())
            return;
        for (int i = i_; i < input.size(); i++)
        {	
            result.push_back(input[i]);
            generateSubset(input, i + 1, result, result_final);
            result.pop_back();
        }
    }
    
};
