public class Solution {
    public int minCut_quitegood(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        int[] opt = new int[s.length() + 1]; // opt[i]: The optimal number of cut from i to the end.
        boolean[][] isPalm = new boolean[s.length()][s.length()]; // isPalm[i][j]: substring of s from i to j is palindrome 
        
        for (int i = 0; i <= s.length(); i ++) {
            opt[i] = s.length() - i;
        }
        
        for (int i = s.length() - 1; i >= 0; i --) {
            for (int j = i; j < s.length(); j ++) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || isPalm[i + 1][j - 1])) {
                    isPalm[i][j] = true;
                    if (opt[j + 1] + 1 < opt[i]) {
                        opt[i] = opt[j + 1] + 1;
                    } 
                }
            }
        }
        
        return opt[0] - 1;
        
    }
    
    // new try
    public int minCut(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        int[] opt = new int[s.length() + 1]; // opt[i]: The optimal number of cut from start to i (i not included).
        boolean[][] isPalm = new boolean[s.length()][s.length()]; // isPalm[i][j]: substring of s from i to j is palindrome 
        
        for (int i = 0; i <= s.length(); i ++) {
            opt[i] = s.length() - i;
        }
        
        for (int i = 0; i < s.length(); ++ i) {
            for (int j = 0; j <= i; ++ j) {
                if (s.charAt(i) == s.charAt(j) && (i - j < 2 || isPalm[j + 1][i - 1])) {
                    isPalm[j][i] = true;
                    if (opt[i] + 1 < opt[i + 1]) {
                        opt[i + 1] = opt[i] + 1;
                    }
                }
            }
        }
        
        return opt[s.length()];
        
    }
}