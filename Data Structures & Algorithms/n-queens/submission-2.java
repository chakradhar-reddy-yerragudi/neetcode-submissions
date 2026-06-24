class Solution {
    public void backtrack(int n,int i,HashSet<Integer> cols,HashSet<Integer> lrDiag,HashSet<Integer> rlDiag,List<StringBuilder> curr,List<List<String>> res){
        if(i==n){
            List<String> currRes=new ArrayList<>();
            for(int j=0;j<n;j++){
                currRes.add(curr.get(j).toString());
            }

            res.add(currRes);
            return;
        }
        for(int j=0;j<n;j++){
            if((!cols.contains(j))&&(!lrDiag.contains(i+j))&&(!rlDiag.contains(i-j))){
                cols.add(j);
                lrDiag.add(i+j);
                rlDiag.add(i-j);
                curr.get(i).setCharAt(j,'Q');
                backtrack(n,i+1,cols,lrDiag,rlDiag,curr,res);
                cols.remove(j);
                lrDiag.remove(i+j);
                rlDiag.remove(i-j);
                curr.get(i).setCharAt(j,'.');

            }
        }

    }
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res=new ArrayList<>();
        List<StringBuilder> curr=new ArrayList<>();
        for(int i=0;i<n;i++){
            curr.add(new StringBuilder(".".repeat(n)));
        }

        HashSet<Integer> cols=new HashSet<>();
        HashSet<Integer> lrDiag=new HashSet<>();
        HashSet<Integer> rlDiag=new HashSet<>();

        backtrack(n,0,cols,lrDiag,rlDiag,curr,res);
        return res;

      
        

  






        
    }
}
