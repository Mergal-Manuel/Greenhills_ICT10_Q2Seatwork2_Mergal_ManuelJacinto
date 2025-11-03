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
    
    Subjects = [math, sci, eng, ict, filo, pe]
    Units = (5, 5, 5, 2, 3, 1)

    mathFinal = Subjects[0] * Units[0]
    sciFinal = Subjects[1] * Units[1]
    engFinal = Subjects[2] * Units[2]
    ictFinal = Subjects[3] * Units[3]
    filoFinal = Subjects[4] * Units[4]
    peFinal = Subjects[5] * Units[5]

    gen_ave = (mathFinal + sciFinal + engFinal + ictFinal + filoFinal + peFinal)/21

    display(f'Math: {math}', target ='outputMath')
    display(f'Science: {sci}', target ='outputSci')
    display(f'English: {eng}', target ='outputEng')
    display(f'ICT: {ict}', target ='outputICT')
    display(f'Filipino: {filo}', target ='outputFilo')
    display(f'PE: {pe}', target ='outputPE')
    display(f'General Average: {gen_ave:.2f}', target='outputGradeAve')

