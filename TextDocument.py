"""
command pattern
	- The Command Pattern decouples the orchestration from implementation.
		○ The TextDocument doesn't need to know how to undo an Operation, it simply tells the Operation to undo, and provides the necessary execution context. 
	- implements open-closed principle: open for extension, closed for modification 

read >> write (apply_operation >> get_current_content)
	- immutable str -> mutable list[char]
		○ str: write O(n), read O(1)
		○ list[char]: write O(1), read O(n) -> lazy cache

"""


from abc import ABC, abstractmethod
class Operation(ABC):
    # @abstractmethod
    def execute(self, document: 'TextDocument') -> None:
        pass
    # @abstractmethod
    def undo(self, document: 'TextDocument'):
        # raise NotImplementedError
        pass

class InsertAtEndOperation(Operation):
    def __init__(self, chars_to_insert: str):
        self.chars_to_insert = chars_to_insert

    def execute(self, document: 'TextDocument'):
        document._doc += self.chars_to_insert
        # document._doc.extend(self.chars_to_insert)

    def undo(self, document: 'TextDocument'):
        n = len(self.chars_to_insert)
        document._doc = document._doc[:-n]
        # del document._doc[-n:]

class DeleteFromEndOperation(Operation):
    def __init__(self, num_chars_to_delete: int):
        self.num_chars_to_delete = num_chars_to_delete
        self._deleted_text = None

    def execute(self, document: 'TextDocument') -> None:
        n = min(self.num_chars_to_delete, len(document._doc))
        if n == 0:
            return 
        self._deleted_text = document._doc[-n:]
        document._doc = document._doc[:-n]
        # del document._doc[-n:]

    def undo(self, document: 'TextDocument') -> None:
        if self._deleted_text:
            document._doc += self._deleted_text
            # document._doc.extend(self._deleted_text)


class TextDocument:
    def __init__(self) -> None:
        self._doc = ""          
        # self.doc = []
        self._undo_stack = []   
        self._redo_stack = []   
        # self._cache = ""
        # self._dirty = False
        
    def get_current_content(self) -> str:
        return self._doc
        # if self._dirty:
        #     self._cache = "".join(self._doc)
        #     self._dirty = False
        # return self._cache

    def apply_operation(self, op: Operation) -> None:
        op.execute(self) 
        # self._dirty = True
        self._undo_stack.append(op)
        self._redo_stack.clear() 

    def undo_last(self) -> None:
        if self._undo_stack:
            op = self._undo_stack.pop()
            op.undo(self)
            # self._dirty = True  
            self._redo_stack.append(op)

    def redo_last(self) -> None:
        if self._redo_stack:
            op = self._redo_stack.pop()
            op.execute(self)
            # self._dirty = True  
            self._undo_stack.append(op)
