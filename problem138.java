//problem 138 /copy list with random pointer
class Solution {
    public Node copyRandomList(Node head) {
         if (head == null) {
             return null;
         }
        copynext(head);
        copyrandom(head);
        return splitlist(head);
    }
    private void copynext(Node head) {
        while (head != null) {
            Node newnode = new Node(head.val,head.next,head.random);
            //newnode.random = head.random;
            //newnode.next = head.next;
            head.next = newnode;
            head = head.next.next;
        }
    }
    private void copyrandom(Node head) {
        while (head != null) {
            if (head.next.random != null) {
                head.next.random = head.random.next;
            }
            head = head.next.next;
        }
    }
    private Node splitlist(Node head) {
        Node newhead = head.next;
        while (head != null) {
            Node temp = head.next;
            head.next = temp.next;
            head = head.next;
            if (temp.next != null) {
                temp.next = temp.next.next;
            }
        }
        return newhead;
    }
}