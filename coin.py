#credits: https://github.com/samrushing/caesure (code helped me a lot <3 )

import hashlib
import time
#https://en.bitcoin.it/wiki/Block_hashing_algorithm
class Block ():
    def __init__(self, prev_block, nonce, merkle_root):
        #Header
        self.prev_block,
        self.timestamp = time.time (),
        self.nonce,
        self.merkle_root
        #Body
        self.transactions = []

    def __len__(self):
        return len(transactions)

    @property
    def gen_merkle_root (self):
        hashed_transactions = [hashlib.sha256(t.encode()).hexdigest() for t in transactions]
        while True:
            if len(hashed_transactions) == 1:
                return hashed_transactions[0]
            if len(hashed_transactions) % 2 != 0:
                hashed_transactions.append (hashed_transactions[-1])
            reduced_transactions = []
            for i in range (0, len(hashed_transactions), 2):
                ## TODO: cant turn object into string, need to change when I created the transactions
                combined_transaction = "{}{}".format(hashed_transactions[i], hashed_transactions[i+1])
                reduced_transactions.append(hashlib.sha256(combined_transaction.encode()).hexdigest())
            hashed_transactions = reduced_transactions

    @property
    def block_hash (self):
        all_values = str(self.prev_block) + str(self.merkle_root) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(all_values.encode()).hexdigest()
