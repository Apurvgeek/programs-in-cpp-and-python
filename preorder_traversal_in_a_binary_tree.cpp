// Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

// Time Complexity: O(N)
// Space Complexity: O(N)

//-----------------------------------Main Code Starts-------------------------------------------//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    // In Preorder : Root - Left - Right

    void preorder(TreeNode* root, vector<int>& ans)
    {
        if(root == NULL)
            return;
        
        ans.push_back(root -> val);
        preorder(root -> left, ans);
        preorder(root -> right, ans);
        
    }
    
    vector<int> preorderTraversal(TreeNode* root) 
    {
        vector<int> ans;
        preorder(root, ans);
        
        return ans;
    }
};