import java.util.Stack;

class Solution {
    public boolean check(String u){
        Stack<Character> st = new Stack<>();
        int length = 0;
        for(int i = 0; i < u.length(); ++i){
            char ele = u.charAt(i);
            if (ele == '('){
                st.push(ele);
                length += 1;
            }
            else{
                if (length == 0){
                    return false;
                }
                else if(st.peek() == '('){
                    st.pop();
                    length -= 1;
                }
            }
        }
        return true;
    }
    public String solution(String p) {
        if(p.length() == 0){
            return p;
        }

        int left = 0;
        int right = 0;
        int idx = 0;
        while(idx < p.length() && (left != right || left + right == 0)){
            if(p.charAt(idx) == '(')
                left += 1;
            else if(p.charAt(idx) == ')')
                right += 1;
            idx += 1;
        }

        String u = p.substring(0, idx);
        String v = "";
        if(idx + 1 < p.length()){
            v = p.substring(idx);
        }

        if(left != right){
            u = "";
            v = p;
        }

        if(check(u))
            return u + solution(v);
        else{
            String s = "";
            if(u.length() > 2)
                u = u.substring(1, u.length()-1);
            else u = "";
            for(int i = 0; i < u.length(); ++i){
                if(u.charAt(i) == '(') s += ')';
                else s += '(';
            }
            return '(' + solution(v) + ')' + s;
        }
    }
}