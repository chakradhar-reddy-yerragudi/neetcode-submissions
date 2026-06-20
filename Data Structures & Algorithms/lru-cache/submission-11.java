class Node{
    int val;
    int key;
    Node next=null;
    Node prev=null;
    Node(int key,int val){
        this.val=val;
        this.key=key;
    }



}
class LRUCache {
    int capacity;
    HashMap <Integer,Node>hm=new HashMap<>();
    Node left=null;
    Node right=null;


    public LRUCache(int capacity) {
        this.capacity=capacity;     
    }
    
    public int get(int key) {
        if(this.hm.containsKey(key)){
            Node temp=this.hm.get(key);


            this.removeNode(temp);
            this.addNode(temp);
            return temp.val;
        }

        return -1;
        
    }
    public void removeNode(Node node){
        hm.remove(node.key);
        if(node==this.left){
            if(this.left==this.right){
                this.left=null;
                this.right=null;
            }
            else
                this.left=this.left.next;

            return;


        }
        if(node==this.right){
            this.right=this.right.prev;
            this.right.next=null;
            node.prev=null;
            return;
        }
        Node prev=node.prev;
        Node next=node.next;
        if(prev !=null)
            prev.next=next;

        if(next!=null)
            next.prev=prev;
        node.next=null;
        node.prev=null;
        

    }
    public void addNode(Node node){
        hm.put(node.key,node);

        if (this.left==null){
            this.left=node;
            this.right=node;
        }else{
            this.right.next=node;
            node.prev=this.right;
            this.right=this.right.next;
        }
        
        

    }
    
    
    public void put(int key, int value) {
        Node newNode=new Node(key,value);
        if(this.hm.containsKey(key)){
            Node temp=this.hm.get(key);


            this.removeNode(temp);
        }


        if(this.hm.size()==this.capacity){
            this.removeNode(this.left);
        }
        this.addNode(newNode);
    
        }

        
    
}
