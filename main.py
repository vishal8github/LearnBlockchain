import hashlib

class  Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:
    def __init__(self, data):
        hashLast = '0000'
        hashStart = self.hashGenerator(data + hashLast)

        genesis = Block(data, hashStart, hashLast)
        self.chain = [genesis]

    def hashGenerator(self, data):
        result = hashlib.sha256(data.encode())
        return result.hexdigest()

    def addBlock(self, data):
        prev_hash = self.chain[-1].hash
        hash = self.hashGenerator(data + prev_hash)

        new_block = Block(data, hash, prev_hash)

        self.chain.append(new_block)


bc = Blockchain('GenesisBlock')

bc.addBlock('myBlock1')
bc.addBlock('myBlock2')
bc.addBlock('myBlock3')

for block in bc.chain:
    print(block.__dict__)
