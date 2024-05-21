from ..models import Student

def gen_stid() -> str:

    #SID001
    last_student = Student.objects.last()

    if last_student:
        l_stid: str = last_student.stid 
        l_un = len(l_stid)
        n_stid = l_stid.split('D')
        n_stid = int(n_stid[1])
        n_stid = n_stid + 1
        l = len(str(n_stid))
        
        if l >= 3:
            return f'SID{n_stid}'
        elif l == 2:
            return f'SID0{n_stid}'
        elif l == 1:
            return f'SID00{n_stid}'

    return 'SID001'