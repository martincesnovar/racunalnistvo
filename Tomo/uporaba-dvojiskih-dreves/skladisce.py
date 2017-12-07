# =============================================================================
# Skladišče
#
# Neko podjetje ima skladišče svojih izdelkov organizirano v obliki drevesne
# strukture. Skladišče je sestavljeno iz več prostorov (vozlišč), vhod v
# skladišče je samo en (pri korenu), iz vsakega prostora pa vodita hodnika do
# največ dveh drugih prostorov (levo in desno poddrevo).
# 
# Oznaka prostora je kar opis poti, kako pridemo od vhoda do ustreznega
# prostora, pri čemer črka `L` pomeni levi hodnik, črka `D` pa desni hodnik.
# Oznaka `DLD` tako pomeni, da pri vhodu zavijemo desno, v naslednjem
# prostoru levo in nato še enkrat desno. V vhodu izdelkov ne hranimo.
# 
# Skladiščnik Stanko je pri zlaganju škatel z izdelki izjemno sistematičen, saj
# da novo škatlo vedno desno od zadnje škatle. Pri pobiranju pa Stanko malo bolj
# improvizira. Če v zadnjo sobo zavije na levo, bo tudi pobral najbolj levo
# škatlo, torej prvo, ki jo je odložil (tako kot pri vrsti). Če pa v zadnjo sobo
# zavije na desno, pa bo pobral najbolj desno, torej tisto, ki jo je odložil
# nazadnje (tako kot pri skladu).
# 
# Če bo v škatli več izdelkov, kot jih je treba, bo preostanek odložil nazaj na
# desno, če pa jih bo premalo, bo odprl še naslednjo škatlo. Če v sobi izdelkov
# ne bo dovolj, bo stvari pustil pri miru, vendar bo težavo zapisal v končno
# poročilo.
# =====================================================================@011432=
# 1. podnaloga
# Napišite funkcijo `stanko(narocila, porocilo)`, ki iz datoteke z imenom
# `narocila` prebere podatke o oznaki, cilju ter količini izdelkov (pozitivno
# za dobavo in negativno za naročilo), nato pa v datoteko z imenom `porocilo`
# najprej izpiše vsa naročila, ki jih ni mogel izvesti, na dnu pa še končno
# stanje v skladišču, urejeno po prostorih, kot si sledijo pri premem pregledu.
# V izpis naj vključi tudi vse prazne prostore, preko katerih dostopamo do
# nepraznih prostorov. Če so bila vsa naročila uspešno izvedena, naj program
# izpiše le končno stanje.
# 
# Na primer, za datoteko `narocila.txt` z vsebino
# 
#     D1 LL 2
#     D2 LD 3
#     D3 D 2
#     D4 D 4
#     N1 LL -3
#     N2 D -1
#     D5 D 1
#     D6 LL 4
#     N3 LL -1
# 
# naj `stanko('narocila.txt', 'porocilo.txt')` v datoteko `porocilo.txt` zapiše:
# 
#     OPOZORILA:
#     Naročilo N1: V prostoru LL je premalo izdelkov
# 
#     KONČNO STANJE:
#     L: /
#     LL: 1, 4
#     LD: 3
#     D: 2, 3, 1
# 
# Namig: kljub temu, da je treba napisati le eno funkcijo, bo dobro, če jo
# razbijete na pomožne funkcije.
# =============================================================================

from dvojisko_drevo import Drevo
from vrsta import Vrsta
from sklad import Sklad

# 8 pomožnih funkcij

def preberi_narocila_iz_dat(narocila_dat):
    '''prebere datoteko'''
    narocila = []
    with open(narocila_dat, 'r') as f:
        for vrstica in f:
            oznaka, pot, kolicina = vrstica.split()
            narocila.append((oznaka, pot, int(kolicina)))
    return narocila

def vzemi_vrsta(vrsta, kolicina):
    '''iz vrste vzame število izdelkov ali vrže izjemo'''
    vr = Vrsta()
    odv_kol = 0
    while odv_kol < kolicina and not vr.prazna():
        vr.vstavi(vrsta.zacetek())
        vrsta.odstrani()
        odv_kol += vr.zacetek()
    if odv_kol > kolicina:
        vrsta.vstavi(odv_kol-kolicina)
    elif odv_kol < kolicina:
        while not vr.prazna():
            vrsta.vstavi(vr.zacetek())
            vr.odstrani()
        raise IndexError

def vzemi_sklad(sklad, kolicina):
    '''iz sklada vzame število izdelkov ali vrže izjemo'''
    pom = Sklad()
    odv_kol = 0
    while odv_kol < kolicina and not sklad.prazen():
        pom.vstavi(sklad.vrh())
        sklad.odstrani()
        odv_kol += pom.vrh()
    if odv_kol > kolicina:
        sklad.vstavi(odv_kol - kolicina)
    elif odvzeta_kolicina < kolicina:
        while not pom.prazen():
            sklad.vstavi(pom.vrh())
            pom.odstrani()
        raise IndexError

def poisci_sobo(skladisce, pot, smer=None):
    '''Vrne iskano sobo ter skladišče s po potrebi dodanimi praznimi sobami.'''
    if skladisce.prazno:
        if smer == 'L':
            skladisce = Drevo(Vrsta())
        elif smer == 'D':
            skladisce = Drevo(Sklad())
    if pot == '':
        return skladisce, skladisce.podatek
    elif pot[0] == 'L':
        levo_skladisce, soba = poisci_sobo(skladisce.levo, pot[1:], smer='L')
        return Drevo(skladisce.podatek, levo=levo_skladisce, desno=skladisce.desno), soba
    elif pot[0] == 'D':
        desno_skladisce, soba = poisci_sobo(skladisce.desno, pot[1:], smer='D')
        return Drevo(skladisce.podatek, levo=skladisce.levo, desno=desno_skladisce), soba

def vzemi_iz_sobe(soba, kolicina):
    '''Vzame elemente iz sobe'''
    if isinstance(soba, Vrsta):
        vzemi_vrsta(soba, kolicina)
    elif isinstance(soba, Sklad):
        vzemi_sklad(soba, kolicina)

def izvedi_narocilo(skladisce, oznaka, pot, kolicina):
    '''Spremeni stanje sob in vrne po potrebi razširjeno skladišče.'''
    skladisce, soba = poisci_sobo(skladisce, pot)
    if kolicina > 0:
        soba.vstavi(kolicina)
    elif kolicina < 0:
        vzemi_iz_sobe(soba, -kolicina)
    return skladisce


def pregled_skladisca(skladisce, smer = None):
    '''Pregleda skladišče'''
    if not skladisce.prazno:
        soba = skladisce.podatek
        vs = []
        if smer == 'L':
            while not soba.prazna():
                vs.append(soba.zacetek())
                soba.odstrani()
        elif smer == 'D':
            while not soba.prazen():
                vs.append(soba.vrh())
                soba.odstrani()
            vs.reverse()
        yield '', vs
        for soba, vs in pregled_skladisca(skladisce.levo, smer ='L'):
            yield 'L' + soba, vs
        for soba, vs in pregled_skladisca(skladisce.desno, smer = 'D'):
            yield 'D' + soba, vs

def porocilo_zapisi(ime_dat, opozorila, skladisce):
    '''Na datoteko izpisi porocilo'''
    with open(ime_dat, 'w') as f:
        if opozorila:
            print('OPOZORILA: ', file = f)
        print(file=f)
        print('KONCNO STANJE:', file = f)
        for skladisce, smer in [(skladisce.levo, 'L'), (skladisce.desno, 'D')]:
            for soba, vsebina_sobe in pregled_skladisca(skladisce, smer=smer):
                print('{}{}: {}'.format(smer, soba, ', '.join(map(str, vsebina_sobe)) if vsebina_sobe else '/'), file=f)
    return


def stanko(narocila, porocilo):
    '''v datoteko porocilo zapise opozorila'''
    skladisce = Drevo(None)
    napake = []
    for (oznaka, pot, kolicina) in preberi_narocila_iz_dat(narocila):
        try: skladisce = izvedi_narocilo(skladisce, oznaka, pot, kolicina)
        except IndexError:
            napake.append('Naročilo {}: V prostoru {} je premalo izdelkov'.format(oznaka, pot))
    porocilo_zapisi(porocilo, napake, skladisce)




































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import io, json, os, re, sys, shutil, traceback, urllib.error, urllib.request


from contextlib import contextmanager

class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = clean or Check.clean
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env={}):
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        actual_result = eval(expression, globals(), local_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env={}):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        s = {}
        s.update(env)
        clean = clean or Check.clean
        exec(code, globals(), s)
        errors = []
        for (x, v) in expected_state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, encoding=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        sys.stdin = io.StringIO('\n'.join(content))
        try:
            yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, use_globals=False):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt):
                inp = input(prompt)
                print(inp)
                return inp
            exec(expression, globals() if use_globals else {'input': visible_input})
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['je enaka'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def generator(expression, expected_values, should_stop=False, further_iter=0, env={}, clean=None):
        from types import GeneratorType
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        gen = eval(expression, globals(), local_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(further_iter):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if should_stop:
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\n'  # beginning of header
            r'(#( [^\n]*)?\n)+'       # description
            r'# =+\n'                 # end of header
            r'(?P<solution>.*?)'      # solution
            r'(?=\n# =+@)',           # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExNDMyfQ:1eMqUH:9eezIHY7GEOWaksFanmZzuQbSV4'
        
        try:
            with Check.in_file('narocila1.txt', ['D1 LL 2', 'D2 LD 3', 'D3 D 2', 'D4 D 4', 'N1 LL -3', 'N2 D -1', 'D5 D 1', 'D6 LL 4', 'N3 LL -1']):
                stanko('narocila1.txt', 'porocilo1.txt')
                Check.out_file('porocilo1.txt', [
                    'OPOZORILA:',
                    'Naročilo N1: V prostoru LL je premalo izdelkov',
                    '',
                    'KONČNO STANJE:',
                    'L: /',
                    'LL: 4, 1',
                    'LD: 3',
                    'D: 2, 3, 1',
                ])
            
            with Check.in_file('narocila2.txt', ['D1 LL 2', 'D2 LD 3', 'D3 D 2', 'D4 D 4', 'N2 D -1', 'D5 D 1', 'D6 LL 4', 'N3 LL -1']):
                stanko('narocila2.txt', 'porocilo2.txt')
                Check.out_file('porocilo2.txt', [
                    'KONČNO STANJE:',
                    'L: /',
                    'LL: 4, 1',
                    'LD: 3',
                    'D: 2, 3, 1',
                ])
            
            with Check.in_file('narocila3.txt', ['D1 LL 2', 'D2 LD 3', 'D3 D 2', 'D4 D 4', 'N2 D -1', 'D5 D 1', 'D6 LL 4', 'N3 LL -1', 'N4 LL -2']):
                stanko('narocila3.txt', 'porocilo3.txt')
                Check.out_file('porocilo3.txt', [
                    'KONČNO STANJE:',
                    'L: /',
                    'LL: 1, 2',
                    'LD: 3',
                    'D: 2, 3, 1',
                ])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token c472a38d99b7c846d8c802c906a562f4354cc53b'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print("Posodabljam datoteko... ", end="")
            backup_filename = backup(filename)
            r = urlopen(response['update'])
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
