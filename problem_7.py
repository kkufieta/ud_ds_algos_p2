#%% [markdown]
# # Problem 7: Request Routing in a Web Server with a Trie
# 
# For this exercise we are going to implement an HTTP Router like you would find in a typical web server using the Trie data structure we learned previously.
# 
# There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.
# 
# The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
# 
# First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
# 
# In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's [SimpleHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler) which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
# 
# We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:
# 
# (root, None) -> ("about", None) -> ("me", "About Me handler")
# 
# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
#%% [markdown]
# ## RouteTrie and RouteTrieNode

#%%
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        """
        Initializes the trie with a root node and handler.
        
        The root node is the root path or home page node.
        """
        self.root = RouteTrieNode()
        
    def _get_sub_paths(self, path):
        """
        Cleans up and splits the path into parts.
        """
        assert(type(path) == str), "Path has to be a string"
        path = path.lower()
        # Checks for and delete leading and trailing slashes.
        if len(path) > 0 and path[0] == '/':
            path = path[1:]
        if len(path) > 0 and path[-1] == '/':
            path = path[:-1]
            
        return path.split('/')

    def insert(self, full_path, handler):
        """
        Adds a path and its handler.
        
        This method uses recursion.
        """
        assert(type(full_path) == str), "Path has to be a string"
        assert(type(handler) == str), "Handler has to be a string"
        # Make sure you assign the handler to only the leaf 
        # (deepest) node of this path.
        sub_paths = self._get_sub_paths(full_path)
        node = self.root
        for path in sub_paths:
            node.insert(path)
            node = node.get_node(path)
        node.set_handler(handler)
        

    def find(self, path):
        """
        Finds a path and returns the handler.
        """
        assert(type(path) == str), "Path has to be a string"
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        sub_paths = self._get_sub_paths(path)
        node = self.root
        for p in sub_paths:
            if p in node:
                node = node.get_node(p)
            else:
                return None
        return node.handler

# Represents a single node in RouteTrie
class RouteTrieNode:
    def __init__(self):
        """
        Initializes the RouteTrieNode.
        """
        self.handler = None
        self.children = {}

    def insert(self, path):
        """
        Adds a path to its children.
        """
        assert(type(path) == str), "Path has to be a string"
        if path not in self:
            self.children[path] = RouteTrieNode()
        
    def get_node(self, path):
        """
        Finds and returns a node based on a path.
        """
        assert(type(path) == str), "Path has to be a string"
        return self.children[path]
    
    def set_handler(self, handler):
        """
        Sets a handler.
        """
        assert(type(handler) == str), "Handler has to be a string"
        self.handler = handler
            
    def __contains__(self, path):
        """
        Checks if this node contains a path.
        """
        assert(type(path) == str), "Path has to be a string"
        return path in self.children
    
    def __str__(self):
        """
        String representation of the RouteTrieNode.
        """
        s = "Handler: " + str(self.handler) + "\n"
        s += "Children: ["
        if len(self.children) == 0:
            s += "]"
            return s
        
        for i, child in enumerate(self.children):
            s += "'" + str(child) + "'"
            if i < len(self.children)-1:
                s += ", "
            else: 
                s += "]\n"
        return s

#%% [markdown]
# ## Router
#%% [markdown]
# Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.
# 
# Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
# 
# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
# 
# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

#%%
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, 
                 not_found_handler="404 - page not found"):
        """
        Initializes the Router.
        
        Creates a new RouteTrie for storing routes.
        """
        assert(type(root_handler) == str), "Root handler has to be a string"
        assert(type(not_found_handler) == str), "Not found handler has to be a string"
        self.trie = RouteTrie()
        self.trie.insert('/', root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """
        Adds a handler for a given path.
        """
        assert(type(path) == str), "Path has to be a string"
        assert(type(handler) == str), "Handler has to be a string"
        self.trie.insert(path, handler)
        

    def lookup(self, path):
        """
        Looks up a path and returns the associated handler.
        """
        assert(type(path) == str), "Path has to be a string"
        handler = self.trie.find(path)
        return handler if handler else self.not_found_handler

#%% [markdown]
# ## Test Cases
#%% [markdown]
# ### Test RouteTrie and RouteTrieNode

#%%
# Inserting a bunch of paths and handlers
routeTrie = RouteTrie()
routeTrie.insert('/', 'home_handler')
routeTrie.insert('/about/me/', 'about_me_handler')
routeTrie.insert('/sports', 'sports_handler')
routeTrie.insert('/career', 'career_handler')
routeTrie.insert('/sports/climbing', 'sports_climbing_handler')
routeTrie.insert('/sports/BJJ', 'sports_bjj_handler')
routeTrie.insert('/sports', 'NEW_sports_handler')
routeTrie.insert('/sports/judo', 'sports_judo_handler')


#%%
# Finding a path and respective handler
def find_path(path):
    return routeTrie.find(path)

paths = ['/about', '/about/me', '/about/me/', '/about/me///', '', '/', '//', '/sports',
        '/career/', '/sports/bjj', '/sports/kayaking']

expected_handlers = ['None', 'about_me_handler', 'about_me_handler', 'None', 
                     'home_handler', 'home_handler', 'home_handler', 'NEW_sports_handler',
                     'career_handler', 'sports_bjj_handler', 'None']

for i, path in enumerate(paths):
    assert(str(find_path(path)) == expected_handlers[i])
    
print("No AssertionError? We passed all tests!")

#%% [markdown]
# ### Test Router

#%%
# Create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")


# some lookups with the expected output
assert(router.lookup("/") == 'root handler')
assert(router.lookup("/home") == 'not found handler')
assert(router.lookup("/home/about") == 'about handler')
assert(router.lookup("/home/about/") == 'about handler')
assert(router.lookup("/sports") == 'not found handler')
assert(router.lookup("/home/about//") == 'not found handler')
assert(router.lookup("/career/") == 'not found handler')

router.add_handler("/home/about/", "NEW About Handler")
assert(router.lookup("/") == 'root handler')
assert(router.lookup("/home") == 'not found handler')
assert(router.lookup("/home/about") == 'NEW About Handler')
assert(router.lookup("/home/about/") == 'NEW About Handler')
assert(router.lookup("/sports") == 'not found handler')
assert(router.lookup("/home/about//") == 'not found handler')
assert(router.lookup("/career/") == 'not found handler')

print("No AssertionError? We passed all tests!")


