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
#check the valid chain and valid block
    def isChainValid(self):
        for i in range(1,len(self.chain)):
            prevb=self.chain[i-1]
            currb=self.chain[i]
            if(currb.hash != currb.calcHash()):
                print("Invalid Block")
                return False
            if(currb.prevhash != prevb.hash):
                print("Invalid Chain")
                return False
        return True



osaCoin=Blockchain()
osaCoin.addBlock(Block(1,'13/04/2020',100))
osaCoin.addBlock(Block(2,'14/04/2020',20))
#osaCoin.chain[1].transaction=333
#osaCoin.chain[1].hash=osaCoin.chain[1].calcHash()

for b in osaCoin.chain:
    print(b)
print(osaCoin.isChainValid()) #text for valid or not

