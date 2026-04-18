//처음엔 array로 했더니 시간초과로 인하여 deque로 바꿨음

//import java.util.*;
//
//public class Main {
//    public static void main(String[] args){
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//
//        for(int i=0; i < n; i++){
//            String order = sc.next();
//
//            ArrayDeque<Integer> deque = new ArrayDeque<>();
//            int size = sc.nextInt();
//
//            String arr = sc.next();
//            arr = arr.substring(1, arr.length() - 1);
//
//            if(size > 0) {
//                String[] strArray = arr.split(",");
//                int idx = 0;
//
//                while(size > 0) {
//                    int data = Integer.parseInt(strArray[idx]);
//                    deque.add(data);
//
//                    idx++;
//                    size--;
//                }
//            }
//
//            boolean isError = false;
//            boolean isReversed = false;
//
//            for(int j=0; j<order.length(); j++){
//                if(order.charAt(j) == 'R'){
//
//                    isReversed = !isReversed;
//                }else{
//                    if(deque.isEmpty()){
//                        System.out.println("error");
//                        isError = true;
//                        break;
//                    }
//                    if(isReversed) {
//                        deque.pollLast();
//                    } else {
//                        deque.pollFirst();
//                    }
//                }
//            }
//            if(!isError) {
//                StringBuilder sb = new StringBuilder();
//                sb.append("[");
//
//                while(!deque.isEmpty()) {
//                    if(isReversed) {
//                        sb.append(deque.pollLast());
//                    } else {
//                        sb.append(deque.pollFirst());
//                    }
//
//                    if(!deque.isEmpty()) {
//                        sb.append(",");
//                    }
//                }
//                sb.append("]");
//                System.out.println(sb);
//            }
//        }
//    }
//}