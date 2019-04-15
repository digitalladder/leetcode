//problem 141 /linked list cycle
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != slow) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}

//using hash map
class Solution2 {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodepass = new HashSet<>();
        while (head != null) {
            if (nodepass.contains(head)) {
                return true;
            }
            else {
                nodepass.add(head);
            }
            head = head.next;
        }
        return false;
    }
}