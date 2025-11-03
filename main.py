from pyscript import document, display

def get_grades(e):

    document.getElementById('outputInfo').innerHTML = "   "
    document.getElementById('outputMath').innerHTML = "   "
    document.getElementById('outputSci').innerHTML = "   "
    document.getElementById('outputEng').innerHTML = "   "
    document.getElementById('outputICT').innerHTML = "   "
    document.getElementById('outputFilo').innerHTML = "   "
    document.getElementById('outputPE').innerHTML = "   "
    document.getElementById('outputGradeAve').innerHTML = "   "
    
    name = document.getElementById('name').value
    section = document.getElementById('sect').value

    document.getElementById('output1').innerHTML = "   "

    display(f'{name} from {section}', target='outputInfo')

    math = int(document.getElementById('Math').value)
    sci = int(document.getElementById('Sci').value)
    eng = int(document.getElementById('Eng').value)
    ict = int(document.getElementById('ICT').value)
    filo = int(document.getElementById('Filo').value)
    pe = int(document.getElementById('PE').value)
    

    gen_ave = int((math + sci + eng + ict + filo + pe)/6)

    display(f'Math: {math}', target ='outputMath')
    display(f'Science: {sci}', target ='outputSci')
    display(f'English: {eng}', target ='outputEng')
    display(f'ICT: {ict}', target ='outputICT')
    display(f'Filipino: {filo}', target ='outputFilo')
    display(f'PE: {pe}', target ='outputPE')
    display(f'General Average: {gen_ave}', target='outputGradeAve')

