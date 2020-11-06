import os

def process_file(p):
    """Fetch a list of words from a URL.
    
        Args:
            url: the URL of a UTF-8 text document.
        
        Returns:
            A list of strings containing the words from 
            the document.
    """
    story = open(p, "r")
    print(story.read())
 
    return story


p = 'C:/Users/NJ86010/Development/RE auto running business objects reports question.txt'

try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')