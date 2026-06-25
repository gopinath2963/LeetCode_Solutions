class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0; // Edge case: empty array

        // 'k' tracks the index of the last unique element found
        int k = 0; 

        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // If current element is different from the last unique one
            if (nums[i] != nums[k]) {
                k++;             // Move the unique pointer forward
                nums[k] = nums[i]; // Update the next unique position
            }
        }

        // Return the number of unique elements (index k + 1)
        return k + 1;
    }
}
