"""
HelloWorld.py
====================================
Document créé à 15h19.
Doc généré par Sphinx2.0.
"""

def confession(your_name):
    """
    Return the most important secret of a person.
    
    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """
    print("The wise {} loves Python.".format(your_name))

def WhoAmI():
    """
    Return the name of a person.
    """
    return("Abderrahmen")

confession(WhoAmI())