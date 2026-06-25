class Solution {
    public double myPow(double x, int n) {
        long N = n; // Use long to prevent overflow if n is Integer.MIN_VALUE
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        
        double result = 1;
        double currentProduct = x;
        
        while (N > 0) {
            // If exponent is odd, multiply the result by current base
            if (N % 2 == 1) {
                result *= currentProduct;
            }
            // Square the base and halve the exponent
            currentProduct *= currentProduct;
            N /= 2;
        }
        
        return result;
    }
}
