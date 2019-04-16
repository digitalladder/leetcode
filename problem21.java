//problem 21 /merge two sorted list
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newlist = new ListNode(0);
        ListNode dummy = newlist;
        while (l1 != null || l2 != null) {
            if (l1 != null && l2 != null) {
                if (l1.val > l2.val) {
                    dummy.next = l2;;
                    dummy = dummy.next;
                    l2 = l2.next;
                }
                else {
                    dummy.next = l1;
                    dummy = dummy.next;
                    l1 = l1.next;
                }
            }
            else if (l1 == null) {
                dummy.next = l2;
                break;
            }
            else {
                dummy.next = l1;
                break;
            }
        }
        return newlist.next;
    }
}