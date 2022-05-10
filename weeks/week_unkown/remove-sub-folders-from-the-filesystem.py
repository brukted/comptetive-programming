class Node:
    def __init__(self):
        self.children = {}
        self.is_folder = False

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        root = Node()
        
        for folder in folders:
            node = root
            for file in folder.split("/"):
                if file not in node.children:
                    node.children[file] = Node()
                
                node = node.children[file]
            node.is_folder = True
        
        result = []
        path = []
        
        def mainFolders(node = root):
            if node.is_folder:
                result.append("/".join(path))
                return
            
            for file, node in node.children.items():
                path.append(file)
                mainFolders(node)
                path.pop()
        
        mainFolders()
        return result
            
