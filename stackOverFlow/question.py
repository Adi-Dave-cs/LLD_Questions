from typing import List
from datetime import datetime
from votable import Votable
from commentable import Commentable
from tag import Tag
from comment import Comment
from answer import Answer
from vote import Vote

class Question(Votable,Commentable):
    def __init__(self,author,title,content,tag_names):
        self.id = id(self)
        self.author = author
        self.title = title
        self.creation_date = datetime.now()
        self.answers = list()
        self.content = content
        self.votes = list()
        self.comments = list()
        self.tags = [Tag(tag) for tag in tag_names]
    
    def add_answer(self,answer):
        if(answer not in self.answers):
            self.answers.append(answer)
        return 
    
    def vote(self,user,value):
        if(value not in [-1,1]):
            raise ValueError('The vote has invalid value')
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user,value))
        self.author.update_reputation(value*5)
    
    def get_vote_count(self):
        return sum([v.value for v in self.votes])
    
    def add_comment(self, comment):
        return self.comments.append(comment)
    
    def get_comments(self):
        return self.comments