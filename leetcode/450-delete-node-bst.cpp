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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) return root;
        else if (key < root->val) root->left = deleteNode(root->left, key);
        else if (key > root->val) root->right = deleteNode(root->right, key);
        else {
            if (root->left == nullptr && root->right == nullptr) {
                delete root;
                root = nullptr;
            } else if (root->left == nullptr || root->right == nullptr) {
                struct TreeNode *temp = root;
                if (root->left == nullptr) root = root->right;
                else root = root->left;
                delete temp;
            } else {
                struct TreeNode *temp = root->right;
                while (temp->left != nullptr) temp = temp->left;
                root->val = temp->val;
                root->right = deleteNode(root->right, temp->val);
            }  
        }
        return root;
    }
};