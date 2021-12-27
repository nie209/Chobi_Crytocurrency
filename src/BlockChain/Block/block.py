from typing import List 
import hashlib
import pickle

class Block:
  __perviouse_hash: str
  __transactions: List[str]
  __block_hash: str

  def __init__(self, previous_hash: str, transactions: List[str]):
    self.__perviouse_hash = previous_hash
    self.__transactions = transactions
    self.__block_hash = hashlib.sha256(pickle.dumps(previous_hash) + pickle.dumps(transactions))
  
  def get_block_hash (self) -> str:
    return  self.__block_hash
  