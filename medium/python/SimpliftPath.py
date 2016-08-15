'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''
class Solution(object):
    def simplifyPath(self, path):
        tokens = path.split("/")
        cur = "/"
        for t in tokens:
            if t == "..":
                if cur != "/":
                    cur = "/".join(cur.split("/")[:-1])
                    if cur == "": cur = "/"
            elif t != "." and t != "":
                cur += "/" + t if cur != "/" else t
        return cur
if __name__ == "__main__":
    assert "/" == Solution().simplifyPath("/a/../")
    assert "/home/sencer/a" == Solution().simplifyPath("/home//b/../sencer/./a")