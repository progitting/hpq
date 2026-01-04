class inode:
    def __init__(self, isDir, timeCreated):
        self.isdir = isDir
        self.time = timeCreated
        self.children = {}

    def lookUpDir(self, dirName):
        return self.children[dirName]
    
    def addDir(self, dirName, time):
        self.children[dirName] = inode(True, time)

    def print(self):
        for name, inode in self.children.items():
            print(f"[name={name}, d={inode.isdir}] ")


class Myfs:
    def __init__(self):
       self.root = inode(True, 0)
    
    def createDir(self, path, name, time):
        dirsInPath = []
        if not path == "/":
            dirsInPath = path.strip("/").split("/")

        current = self.root
        for dir in dirsInPath:
            if not current.isdir:
                print(f"invalid directory {path}")
                return
            current = current.lookUpDir(dir)

            if not current:
                print(f"invalid directory {path}")
                return

        current.addDir(name, time)

    def createFile(self, name, time):
        pass

    def appendToFile(self, path, str):
        pass

    def printFile(self, path):
        pass 
    
    def ls(self, path):
        dirsInPath = []
        if not path == "/":
            dirsInPath = path.strip("/").split("/")

        current = self.root
        for dir in dirsInPath:
            if not current.isdir:
                print(f"invalid directory {path}")
                return
            current = current.lookUpDir(dir)

            if not current:
                print(f"invalid directory {path}")
                return
            
        current.print()

    def remove(self, path):
        if path == "/":
            print("Cannot remove root directory")
            return

        # Split the path into parts
        dirsInPath = path.strip("/").split("/")
        target_name = dirsInPath[-1]  # last element is the directory to remove
        parent_path = dirsInPath[:-1] # everything before it is the parent

        # Start from root
        current = self.root
        for dir in parent_path:
            if not current.isdir:
                print(f"Invalid directory {path}")
                return
            try:
                current = current.lookUpDir(dir)
            except KeyError:
                print(f"Invalid directory {path}")
                return

        # Remove the target directory from parent's children
        if target_name in current.children:
            del current.children[target_name]
            print(f"Removed {path}")
        else:
            print(f"Directory {path} does not exist")

    

fs = Myfs()
fs.createDir("/", "a", 666)
fs.ls("/") # thid is expected to print a
fs.createDir("/a", "b", 777)
fs.ls("/a") # thid is expected to print b

print("remove /a/b")
fs.remove("/a/b")
fs.ls("/a") # should not print anything

print("2nd filesystem")

fs2 = Myfs()
fs2.createDir("/", "f", 42)
fs2.ls("/") # thid is expected to print f
