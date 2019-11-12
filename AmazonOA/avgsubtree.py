# Definition for a binary tree node.

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inordersum(self,root,avglist):
        if root:
            leftsum,leftcount =  self.inordersum(root.left,avglist)
            rightsum,rightcount = self.inordersum(root.right,avglist)
            total  = leftsum + rightsum + root.val
            totalcount = leftcount + rightcount + 1
            avg = (total)/(totalcount)
            avglist.append(avg)
            return [total,totalcount]
        else:
            return [0,0]


    def maximumAverageSubtree(self, root: TreeNode) -> float:
        avglist = []
        self.inordersum(root,avglist)
        return max(avglist)






s = stringToTreeNode('[5,6,1]')
print(Solution().maximumAverageSubtree(s))
'fsdfsd'.lower()
