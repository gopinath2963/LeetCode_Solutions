class Solution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.strStr("sadbutsad", "sad"));
    }
}