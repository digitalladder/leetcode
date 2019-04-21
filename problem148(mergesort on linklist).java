//problem 148 /sortlist
//using merge sort
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode left = head;
        ListNode mid = partition(head);
        ListNode right = null;
        if (mid.next == null) {
            left.next = null;
            right = mid;
        }
        else {
            right = mid.next;
            mid.next = null;
        }
        
        ListNode l1 = sortList(left);
        ListNode l2 = sortList(right);
        ListNode result = merge(l1,l2);
        
        return result;
        
    }
    
    protected ListNode partition(ListNode head) {
        ListNode p1 = head;
        ListNode p2 = head;
        while (p2 != null && p2.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
        }
        return p1;
    }
    
    protected ListNode merge(ListNode l1, ListNode l2) {
        ListNode prev = null;
        ListNode head = null;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                if (prev == null) {
                    prev = l1;
                    head = l1;
                    l1 = l1.next;
                }
                else {
                    prev.next = l1;
                    prev = l1;
                    l1 = l1.next;
                }
            }
            else {
                if (prev == null) {
                    prev = l2;
                    head = l2;
                    l2 = l2.next;
                }
                else {
                    prev.next = l2;
                    prev = l2;
                    l2 = l2.next;
                }
            }
        }
        if (l1 == null) {
            prev.next = l2;
        }
        else if (l2 == null) {
            prev.next = l1;
        }
        return head;
    }
}