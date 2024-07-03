"""
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.


"""
import copy


class Traveler():
    def __init__(self):
        self.path = [] # where he walk already
        self.cost = 0  # should be sum of path

    def calculate_cost(self):
        cost_sum = 0
        for node in self.path:
            cost_sum+= node.cost
        self.cost = cost_sum
        return self.cost 
    
    def clone(self):
        new_traveler = Traveler()
        new_traveler.path = copy.deepcopy(self.path)
        new_traveler.calculate_cost()
        return new_traveler

    def travel(self, node):
        self.path.append(node)


class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None
        self.lowest_cost = 100001

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def add_children(self, node_list):
        for node in node_list:
            self.add_child(node)


def create_example():
    head_node = Node(0)
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3)
    node6 = Node(6)
    node2 = Node(2)
    node0 = Node(0)
    node1 = Node(1)
    node5_2 = Node(5)
    node1_2 = Node(1)
    node_10 = Node(10)
    node1_3 = Node(1)
    total_node = [head_node, node5, node4, node3, node6, node2, node0, node1, node5_2, node1_2, node_10, node1_3]

    head_node.add_children([node5, node3, node6])
    node5.add_child(node4)
    node3.add_children([node2, node0])
    node6.add_children((node1, node5_2))
    node2.add_child(node1_2)
    node1_2.add_child(node1_3)
    node0.add_child(node_10)
    return head_node, total_node


def get_cheapest_cost(rootNode):
    walked, edges = walk_algo2(rootNode)
    list_cost = [e.lowest_cost for e in edges]
    return min(list_cost)


def walk_algo2(root_node):
    stck = []
    stck.append(root_node)
    walked = []
    edge = []
    while len(stck) > 0:
        node = stck.pop()
        # walk function
        print(node.cost)
        if node.parent is None:
            node.lowest_cost = node.cost
        else:
            cost = node.parent.lowest_cost + node.cost
            if cost < node.lowest_cost:
                node.lowest_cost = cost
        walked.append(node)
        # add child to node
        for n in node.children:
            stck.append(n)
        if len(node.children) == 0:
            edge.append(node)
    print("============")
    return walked, edge



def walk_algo(root_node):
    stck = []
    stck.append(root_node)
    walked = []
    while len(stck) > 0:
        node = stck.pop()
        # walk function
        print(node.cost)
        walked.append(node)
        # add child to node
        for n in node.children:
            stck.append(n)
    print("============")
    return walked


if __name__ == "__main__":
    root_node, node_list = create_example()
    # walk_algo(root_node)
    walked, edges = walk_algo2(root_node)
    print("list of edge")
    for node in edges:
        print(node.lowest_cost)
    # get_cheapest_cost(root_node)
