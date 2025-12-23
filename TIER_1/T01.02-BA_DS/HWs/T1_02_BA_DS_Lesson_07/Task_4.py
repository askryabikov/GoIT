"""
Comment system as a tree

Plan:
- Each Comment is a NODE
- Each comment can have multiple replies
- Each reply is a Child node
- A reply is also a Comment, so it can have its own replies in nested structure
- First comment is the ROOT of the tree
- display() prints the tree using recursion (DFS)

Example hierarchy:
root_comment
├── reply1
│   └── reply1_1
└── reply2

Deleted comments:
- Replace its text with a standard message.
- Replies under a deleted comment remain visible.
"""


class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author

        # List of replies (children nodes). Each reply is also a Comment object.
        self.replies = []

        # True = comment was deleted
        self.is_deleted = False

    def add_reply(self, reply_comment): 
        """
        - Adds a new reply (child)
        """
        self.replies.append(reply_comment)


    def remove_reply(self):
        """
        - Replace its text with a standard message
        - Mark is_deleted becomes True
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True


    def display(self, level=0):
        """
        Recursively print this comment and all nested replies

        levels:
        - level = 0 (root comment)
        - level = 1 (reply)
        - level = 2 (reply to reply), etc.
        """
        indent = "    " * level  # 4 spaces per nested level

        # If deleted: print the standard message
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        # DFS: print all child replies
        for reply in self.replies:
            reply.display(level + 1)



# Task example

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()


