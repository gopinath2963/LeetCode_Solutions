class Solution {
    public boolean isValidSudoku(char[][] board) {

        Set <String>  s =new HashSet<String> ();

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char c = board[i][j];

                if(c != '.'){
                    String r = c+"r"+i;
                    String co = c+"c"+j;
                    String b = c+ "b" +(i/3)+ "-"+ (j/3);

                    if(!s.add(r) || !s.add(co) || !s.add(b)){
                        return false;
                    }
                }
            }

        }
        return true;
        
    }
}