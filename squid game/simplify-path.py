class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        path_stack = []
        for sth in dirs:
            if sth == "" or sth == ".":
                continue
            elif sth == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(sth)
        return "/" + "/".join(path_stack)
