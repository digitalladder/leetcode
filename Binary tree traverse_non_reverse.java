//Binary tree preorder traverse
public class solution{
	public list<Integer> preorderTraversal(TreeNode root) {
		Stack<TreeNode> stack = new Stack<TreeNode>();
		List<Integer> preorder = new ArrayList<Integer>();

		if(root==null){
			return preorder;
		}

		stack.push(root);
		while(!stack.empty()){
			TreeNode node = stack.pop();
			preorder.add(node.val);
			if(node.right!=null){
				stack.push(node.right);
			}
			if (node.left!=null){
				stack.push(node.left);
			}
		}

		return preorder;
	}
}

//inorder traverse
public class solution{
	public ArrayList<Integer> inorderTraversal(TreeNode root){
		Stack<TreeNode> stack =new Stack<TreeNode>();
		ArrayList<Integer> resule=new ArrayList<Integer>();
		TreeNode curt = root;
		while(curt!=null||!stack.empty()){
			while(curt!=null){
				stack.add(curt);
				curt=curt.left;
			}
			curt=stack.peek();
			stack.pop();
			result.add(curt.val);
			curt=curt.right;
		}
		return result;
	}
}

//postorder traverse
public ArrayList<integer> postorderTraversal(TreeNode root){
	ArrayList<Integer> result = new ArrayList<Integer>();
	Stack<TreeNode> stack = new Stack<TreeNode>();
	TreeNode prev =null; //previously traversed node
	TreeNode curr =root;

	if (root == null){
		return result;
	}

	stack.push(root);
	while( !stack.empty()){
		curr = stack.peek();
		if (prev == null || prev.left == curr ||prev.right ==curr){ //traverse down the tree
			if (curr.left != null){
				stack.push(curr.left);
			} else if (curr.right != null){
				stack.push(curr.right);
			}

		} else if (curr.left == prev){ //traverse up the tree from the left
			if (curr.right != null){
				stack.push(curr.right);
			}
		} else { //traverse up the tree from the right
			result.add(curr.val);
			stack.pop();
		}
		prev = curr;
	}

	return result;
}