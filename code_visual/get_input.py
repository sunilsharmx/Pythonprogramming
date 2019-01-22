import json
with open(r'input.json', 'r')  as input:
    obj = json.load(input)
    with open(r'output.txt','w') as output:
        output.write(obj['name'] + "`s Hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + '\n')

    print('hello ' + obj['name'])
