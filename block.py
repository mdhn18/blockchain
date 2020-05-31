import hashlib
import json
class Block:
    def __init__(self,nonce,tstamp,transaction,prevhash=''):
        self.nonce=nonce
        self.tstamp=tstamp
        self.transaction=transaction
        self.prevhash=prevhash
        self.hash=self.calcHash()
    def calcHash(self): 
        block_string=json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transaction":self.transaction,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def __str__(self):
        string="nonce: " + str(self.nonce) + "\n"
        string+= "tstamp: " + str(self.tstamp)+ "\n"
        string+= "transction: " + str(self.transaction)+ "\n"
        string += "prevhas: " + str (self.prevhash)+ "\n"
        string += "hash: " + str (self.hash)+ "\n"
        return string

class Blockchain:
    def __init__(self):
       self.chain=[self.generateGenesisBlock(),]
    def generateGenesisBlock(self):
        return Block(0, '08/04/2020','Gensis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self,newBlock):
        newBlock.prevhash=self.getLastBlock().hash
        newBlock.hash=newBlock.calcHash()
        self.chain.append(newBlock)



osaCoin=Blockchain()
osaCoin.addBlock(Block(1,'13/04/2020',100))
osaCoin.addBlock(Block(2,'14/04/2020',20))

for b in osaCoin.chain:
    print(b)
