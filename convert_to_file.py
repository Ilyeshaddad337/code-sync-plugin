import json



d = 'public/code-snippets/'

def sanitize_snippet_name( name: str ) :
    return "-".join(name.strip().lower().split(' ')) + ".php"


def main (): 
    f = json.load(open('bb-development.code-snippets.json'))
    for snippet in f['snippets'] :
        name = sanitize_snippet_name(snippet['name'])
        print(name)
        desc = snippet['desc'].split('\n')
        desc  = "\n".join(["// " + r for r in desc])
        
        code = snippet['code']
        
        with open(d + name, 'w') as file:
            file.write('<?php\n')
            
            file.write(desc + "\n")
            
            file.write(code)
        
            
            
main()