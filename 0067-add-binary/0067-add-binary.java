class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        // Iterate from right to left while there are bits or a carry remaining
        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                // Convert char to int ('1' becomes 1, '0' becomes 0)
                carry += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                carry += b.charAt(j--) - '0';
            }
            
            // Append the remainder (0 or 1) to our result
            sb.append(carry % 2);
            // Update carry for the next position (0 or 1)
            carry /= 2;
        }

        // Since we appended from right to left, reverse the string at the end
        return sb.reverse().toString();
    }
}
