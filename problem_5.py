#%% [markdown]
# # Problem 5: Autocomplete with Tries
# 
# ## Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# ###  Finding Suffixes
# 
# Once we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code we wrote for the `TrieNode`, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)
#%% [markdown]
# ### Trie and TrieNode

#%%
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        """
        Initializes the TrieNode.
        """
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        """
        Adds a child TrieNode.
        """
        assert(type(char) == str), "char has to be a string"
        if char not in self:
            self.children[char] = TrieNode()
            
    def get_node(self, char):
        """
        Returns a child TrieNode.
        """
        assert(type(char) == str), "char has to be a string"
        return self.children[char]
    
    def suffixes(self):
        """
        Collects the suffixes for all complete words found in this node's children.
        
        This function uses recursion.
        """
        suffixes = []
        if self.is_word:
            suffixes.append('')
        for ch, child_node in self.children.items():
            child_suffixes = child_node.suffixes()
            if len(child_suffixes) > 0:
                for suffix in child_suffixes:
                    suffixes.append(ch + suffix)
            else:
                suffixes.append(ch)
        return suffixes
            
    def __contains__(self, char):
        """
        Checks if the character is stored in this node's children.
        """
        assert(type(char) == str), "char has to be a string"
        return char in self.children
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        """
        Initializes the Trie.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Adds a word to the Trie.
        """
        assert(type(word) == str), "Word has to be a string"
        node = self.root
        for char in word:
            node.insert(char)
            node = node.get_node(char)
        node.is_word = True

    def find(self, prefix):
        """
        Finds the TrieNode that represents this prefix.
        """
        assert(type(prefix) == str), "Prefix has to be a string"
        node = self.root
        for char in prefix:
            if char in node:
                node = node.get_node(char)
            else:
                return None
        return node
            
    def __contains__(self, word):
        """
        Checks if the word is stored in this Trie.
        """
        assert(type(word) == str), "Word has to be a string"
        node = self.find(word)
        return node.is_word if node else False

#%% [markdown]
# ## Tests

#%%
trie = Trie()
for word in ['hi', 'this', 'is', 'Kat']:
    trie.insert(word)
    
print('hi' in trie)
print('nope' in trie)
    
for word in ['hi', 'this', 'is', 'Kat']:
    assert((word in trie) == True), "Word should be in the trie"
    
for word in ['can', 'not', 'find']:
    assert((word in trie) == False), "Word should not be in the trie"


#%%
for word in ['fun', 'function', 'factory']:
    trie.insert(word)
    
f_node = trie.find('f')
suffixes = f_node.suffixes()
print("suffixes: ", suffixes)

#%% [markdown]
# ## Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

#%%
trie = Trie()
words = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in words:
    trie.insert(word)


#%%
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = trie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='')


