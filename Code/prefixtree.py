#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        current_node = self.root

        for char in string:
            # using try and except here because get_child method raises a ValueError if not found
            try:
                current_node = current_node.get_child(char)
            except:
                return False

        return current_node.terminal

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        current_node = self.root

        for char in string:
            # we add a node if not found in current node's children
            if not current_node.has_child(char):
                new_node = PrefixTreeNode(char)
                current_node.add_child(new_node)
            current_node = current_node.get_child(char)

        # only want to increment size if terminal is not False
        if not current_node.is_terminal():
            self.size += 1
            current_node.terminal = True

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        depth = 0

        for char in string:
            # runs the entirety of the string to get the last node; we are assuming 
            # that the string is a valid word in tree
            if node.has_child(char):
                node = node.get_child(char)
                depth += 1
        return node, depth

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # find last(deepest) node
        node = self._find_node(prefix)[0]

        # if node is terminal we append the prefix because the last node of the prefix is terminal it's a valid string
        if node.is_terminal():
            completions.append(prefix)

        # if prefix != '':
        if not self.root.has_child(prefix[0]):
            return completions

        for child in node.children:
            # traverse on each child with the prefix as the prefix plus the child
            # node character, and the completion is appending to the completions array
            self._traverse(child, (prefix + child.character), completions.append)

        return completions
            
    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # since we want all valid words or strings in the tree we start with the root node
        # with the prefix as empty or '', and then we append that to all_strings as our completion
        self._traverse(self.root, '', all_strings.append)
        return all_strings

        # OR but need to activate line 98
        # return self.complete('')

    # helper function to traverse the nodes
    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # like base case 
        if node.is_terminal():
            visit(prefix) # append function, and append our prefix based on traverse

        if len(node.children) > 0:
            for child in node.children:
                # we are recursively calling this function until we reach terminal or when children doesn't exist
                self._traverse(child, (prefix + child.character), visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
