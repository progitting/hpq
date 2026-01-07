# Modern computers address memory in bytes (8 bits)

# Give myself "1TB of storage" 
storageSize = 1000000000000  # 0xE8D4A51000

# Seperate the disk into blocks of 4KB each (conventional)
blockSize = 4096
BlockNum = storageSize // 4096 # 4096 = 0x1000
storage = [0] * BlockNum # 0 = 0x0
nextBlock = 0

# Create inode class so I can create inodes easier (with less lines of code)
class inode:
    def __init__(self, isDir, timeCreated):
        self.isdir = isDir
        self.time = timeCreated
        self.children = {}
        self.blocks = []   
        self.size = 0      

    def lookUpDir(self, dirName):
        return self.children[dirName]
    
    def addDir(self, dirName, time):
        self.children[dirName] = inode(True, time)
    
    def addFile(self, fileName, time):
        self.children[fileName] = inode(False, time)

root = inode(True, 0)

# Function for going through directories to find
def resolvePath(path):
   
    if path == "/": 
        return root  

    dirs = path.strip("/").split("/")
    current = root

    for dir in dirs:
        if not current.isdir:
            print(f"Invalid path: {path}")
            return None
        try:
            current = current.lookUpDir(dir)
        except KeyError:
            print(f"Directory {dir} does not exist in {path}")
            return None

    return current

# Function to create directories
def createDir(path, name, time):
    parent = resolvePath(path)
    if parent is None:
        return
    if name in parent.children:
        print(f"Directory {name} already exists in {path}")
        return
    parent.addDir(name, time)
    print(f"Created directory {name} in {path}")

# Function to create files
def createFile(path, name, time):
    parent = resolvePath(path)
    if parent is None:
        return
    if name in parent.children:
        print(f"File {name} already exists in {path}")
        return
    parent.addFile(name, time)
    print(f"Created file {name} in {path}")

# Function to add data to files
def appendToFile(path, fileName, data):

    global nextBlock  

    parent = resolvePath(path)
    if parent is None:
        print("Invalid path")
        return

    if fileName not in parent.children:
        print(f"File {fileName} does not exist in {path}")
        return

    fileNode = parent.children[fileName]

    if fileNode.isdir:
        print(f"{fileName} is a directory, cannot append")
        return

    dataBytes = data.encode()  

    block_count = (len(dataBytes) + blockSize - 1) // blockSize  

    for i in range(block_count):
        start = i * blockSize
        end = start + blockSize
        storage[nextBlock] = dataBytes[start:end]  
        fileNode.blocks.append(nextBlock)          
        nextBlock += 1                              

    fileNode.size += len(dataBytes)

    print(f"Appended {len(dataBytes)} bytes to {fileName}")


def printFile(path, fileName):
    parent = resolvePath(path)
    if parent is None:
        return
    if fileName not in parent.children:
        print(f"File {fileName} does not exist in {path}")
        return
    fileNode = parent.children[fileName]
    if fileNode.isdir:
        print(f"{fileName} is a directory")
        return
    
    data = b""
    for b in fileNode.blocks:
        data += storage[b]  
    print(data.decode())

def ls(path):
    node = resolvePath(path)
    if node is None:
        return
    if not node.isdir:
        print(f"{path} is not a directory")
        return
    for name, child in node.children.items():
        typeStr = "Dir" if child.isdir else "File"
        print(f"{name} ({typeStr})")







    



