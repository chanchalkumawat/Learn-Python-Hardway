"""The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s

Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith()."""
s=raw_input("enter the word\n")
l=len(s)-1
def singular(s):
    c='osxz'
    if s[l]=='y':
        st=s.replace("y","ies")
    else:
    
        for i in c:
            if s[l]==i:
                st=s.replace(i,"es")
        if (s[l-1]=='c'and s[l]=='h'):
               st=s.replace("ch","es")
        elif (s[l-1]=='s' and s[l]=='h'):
                st=s.replace("sh","es")    
            
        
    return st
print singular(s)

