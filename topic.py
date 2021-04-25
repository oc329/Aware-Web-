import textwrap 

class Topic: 
  
  def __init__(self, name, sub_topics, articles = []):
    self.name = name
    self.sub_topics = sub_topics
    self.articles = articles

  
  #Copy and Pasted Multi Line Indenter 
  #https://stackoverflow.com/questions/8234274/how-to-indent-the-contents-of-a-multi-line-string/8348914
  #https://docs.python.org/3/library/textwrap.html
   #Can't figure out this indentation's module's errors, I'll test in the morning 
  
  def indent_text(self, text, amount, ch=' '):
    try:
      textwrap.indent
    except AttributeError:  # Except + error allows the error to occur without crashing the program
      padding = amount * ch
      return ''.join(padding+line for line in text.splitlines(True))
      #splitlines is an attribute of any string through textwrap
    else:
      return textwrap.indent(text, amount * ch)
      #amount = amount of ch (space) for the indent 
  def search(self, word, level): 
    if self.name == word:
      self.recursively_list(0)
    else: 
      if len(self.articles) != 0:
        for article in self.articles: 
          if word in article: 
            print(article)
    if self.sub_topics != []: 
      for subTopic in self.sub_topics: 
        subTopic.recursively_list(level + 1)
 
    


  
  
    
    
  
  def recursively_list(self, level):
    #print("runs function", self.name) #testing

         # " " * level add spaces to the topics so they aren't all on the same line 
        # Recursive data structure traversing: https://openbookproject.net/thinkcs/python/english3e/trees.html
    spacing = "    " 
    print((spacing * level) + self.name)
    if len(self.articles) != 0:
      for article in self.articles: 
        print(self.indent_text(article, level + 1, spacing))
        #print(self.indent_text(article, level, spacing)
    elif self.sub_topics != []: 
      for subTopic in self.sub_topics: 
        subTopic.recursively_list(level + 1) 
      '''
      Doc Syntax
      textwrap.indent(text, prefix, predicate=None)
Add prefix to the beginning of selected lines in text.

Lines are separated by calling text.splitlines(True).

      '''

   

    #spaces_before = ("    " * level) #Before copied code
  
      
      
      
    
#It's not going to run rn. Give me like 20 min and I'll try and create the list feature with a search feature 
# We also have to add more topics to the instances 
class Subtopic(Topic): 
    def __init__(self, name, article_links, sub_topics = []):
      super().__init__(name, sub_topics, article_links)
