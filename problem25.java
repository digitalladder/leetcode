//problem 25 /reverse nodes in k-group
//ListNode definition in ListNode.java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        while(prev != null) {
            prev = reverseknodes(prev, k);
        }
        
        return dummy.next;
    }
    
    private ListNode reverseknodes(ListNode prev, int k) {
        
        if (k <= 0) {
            return null;
        }
        if (prev == null) {
            return null;
        }
        ListNode nodek = prev;
        ListNode node1 = prev.next;
        for (int i = 0; i < k; i++) {
            if (nodek == null) {
                return null;
            }
            nodek = nodek.next;
        }
        if (nodek == null) {
            return null;
        }
        ListNode nextnode = nodek.next;
        
        ListNode prev1 = prev;
        ListNode curt = prev.next;
        for (int i = 0; i < k; i++) {
            ListNode temp = curt.next;
            temp = curt.next;
            curt.next = prev1;
            prev1 = curt;
            curt = temp;
        }
        node1.next = nextnode;
        prev.next = nodek;
        
        return node1;
    }
}