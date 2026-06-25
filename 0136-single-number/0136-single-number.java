class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for(Map.Entry<Integer,Integer> sets : map.entrySet()){
            if(sets.getValue()==1){
                return sets.getKey();
            }
        }
        return 0;
    }


}