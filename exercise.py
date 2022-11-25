open('active_members.txt','w').write('')
open('inactive_members.txt','w').write('')
open('active_members.txt','a').write('Membership No     Date Joined\n')
open('inactive_members.txt','a').write('Membership No     Date Joined\n')
to_be_written = 'dump.txt'

with open('members.txt','r') as li:
    li.readline()
    
    for s in li.readlines():
        data = [c for c in s.split(' ') if c != '' and c != '\n']

        if(data[2] == 'yes'):
            to_be_written = 'active_members.txt'
        elif (data[2] == 'no'):
            to_be_written = 'inactive_members.txt'
        
        open(to_be_written, 'a').write(f'   {data[0]}           {data[1]}\n')
