
#from re import compile as createRegExPattern

#pattern = createRegExPattern("(.{0,25}\b)(?:humans|human)(\b.{0,25})")
#match = pattern.search(comment.body.lower())

def comment():
    pass
    
comment.body = "There are many humans that consider themselves human, but they are really aliens."


from re import (
    compile as createRegExPattern,
    IGNORECASE
)

pattern = createRegExPattern(r"(.{0,25}\b)(?:humans|human)(\b.{0,25})", flags=IGNORECASE)
match = pattern.search(comment.body)