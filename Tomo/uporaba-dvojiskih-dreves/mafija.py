# =============================================================================
# Mafija
#
# V neki mafijski organizaciji so člani urejeni hierarhično. Vsakdo razen
# botra (vrhovnega šefa) ima natanko enega nadrejenega. Vsak mafijec ima
# lahko pod seboj največ dva podrejena (levega in desnega).
# Mafijci morajo zbirati denar s kriminalnimi dejavnostmi. Tisti, ki imajo
# podrejene, pa ga poleg tega poberejo še od svojih podrejenih. Ves
# “prisluženi” in prejeti denar morajo oddati svojemu nadrejenemu.
# 
# Boter je posumil, da nekateri člani goljufajo. Nekaj denarja, ki ga poberejo
# od podrejenih, zadržijo zase. Od vsakega člana je pridobil podatek o tem,
# koliko denarja je oddal naprej ter si podatke shranil v drevo, v katerih
# so podatki pari imena in količine oddanega denarja. Na primer:
# 
#     mafija = Drevo(('Salvatore', 320),
#                    levo=Drevo(('Bernardo', 200),
#                               levo=Drevo(('Matteo', 50)),
#                               desno=Drevo(('Carlo', 100),
#                                           levo=Drevo(('Rosalia', 70)),
#                                           desno=Drevo(('Tommaso', 50)))),
#                    desno=Drevo(('Francesco', 120),
#                                levo=Drevo(('Giuseppe', 70)),
#                                desno=Drevo(('Antonio', 60))))
# =====================================================================@010476=
# 1. podnaloga
# Botra zanima, koliko denarja zaradi goljufov “ponikne”. Želi, da
# sestavite funkcijo `koliko_ponikne(drevo)`, ki vrne skupno vsoto denarja,
# ki ponikne. Primer:
# 
#     >>> koliko_ponikne(mafija)
#     30
# =============================================================================


from sklad import Sklad

def pregled_po_skladu(zacetno_drevo):
    '''pregleda drevo s skladom'''
    sklad = Sklad()
    sklad.vstavi(zacetno_drevo)
    while not sklad.prazen():
        drevo = sklad.poberi()
        if not drevo.prazno:
            sklad.vstavi(drevo.levo)
            sklad.vstavi(drevo.desno)
            yield drevo.podatek
# =====================================================================@010477=
# 2. podnaloga
# Ko je boter dognal, koliko denarja ponikne, je totalno po████. Pri
# priči hoče imeti imena vseh goljufov! Napišite funkcijo `goljufi(drevo)`,
# ki vrne množico goljufov. Vsak goljuf naj bo predstavljen z naborom.
# Prva kompotenta naj bo ime goljufa, druga komponenta pa količina denarja,
# ki ga je utajil. Primer:
# 
#     >>> goljufi(mafija)
#     {(’Carlo’, 20), (’Francesco’, 10)}
# =============================================================================



def goljufi(mafija):
    '''vrne množico goljufov'''
    if mafija.prazno:
        return set()
    ukradel = max(denar(mafija.levo) + denar(mafija.desno) - denar(mafija),0)

    return ({(mafija.podatek[0], ukradel)} if ukradel > 0 else set()) | goljufi(mafija.levo) | goljufi(mafija.desno)

# =====================================================================@010478=
# 3. podnaloga
# Botru se dozdeva, da so najbolj pridne _majhne ribe_. To so tisti mafijci,
# ki nimajo pod seboj nobenega podrejenega. Tistim, ki imajo podrejene, se
# reče _velike ribe_. Napišite funkcijo `zasluzek(drevo)`, ki vrne par (nabor)
# dveh števili, pri čemer je:
# 
# * prvo število skupna vsota denarja, ki ga zaslužijo majhne ribe;
# * drugo število skupna vsota denarja, ki ga zaslužijo velike ribe (brez
#   pobirkov od podrejenih).
# 
# Primer:
# 
#     >>> zasluzek(mafija)
#     (300, 50)
# =============================================================================


def zasluzek(mafija):
    '''vrne nabor, koliko zaslužijo majhne ribe in koliko velike'''
    if mafija.prazno:
        return (0,0)
    ukradel = max(denar(mafija) - denar(mafija.levo) - denar(mafija.desno) ,0)
    l_mala, l_velika = zasluzek(mafija.levo)
    d_mala, d_velika = zasluzek(mafija.desno)
    m, v = l_mala + d_mala, l_velika + d_velika
    
    if mafija.levo.prazno and mafija.desno.prazno: #gre za "majhno ribo"
        m += mafija.podatek[1]
    else:
        v += ukradel
    return m, v




































































































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
        
        try:
            test_data = [
                ("""koliko_ponikne(Drevo(('Salvatore', 320), levo=Drevo(('Bernardo', 200), levo=Drevo(('Matteo', 50)), desno=Drevo(('Carlo', 100), levo=Drevo(('Rosalia', 70)), desno=Drevo(('Tommaso', 50)))), desno=Drevo(('Francesco', 120), levo=Drevo(('Giuseppe', 70)), desno=Drevo(('Antonio', 60)))))""", 30),
                ("""koliko_ponikne(Drevo(('Mirsad', 1030), levo=Drevo(('Slobodan', 570), levo=Drevo(('Vid', 220), levo=Drevo(('Ervin', 140)), desno=Drevo(('Andraž', 200))), desno=Drevo(('Rok', 430), levo=Drevo(('Ivo', 190)), desno=Drevo(('Maks', 150)))), desno=Drevo(('Miro', 460), levo=Drevo(('Leopold', 210), levo=Drevo(('Lovro', 130)), desno=Drevo(('Tine', 190))), desno=Drevo(('Jože', 300), levo=Drevo(('Maj', 200)), desno=Drevo(('Andrej', 150))))))""", 410),
                ("""koliko_ponikne(Drevo(('Rok', 1550), levo=Drevo(('Aljoša', 840), levo=Drevo(('Anže', 420), levo=Drevo(('Tomislav', 190)), desno=Drevo(('Stanko', 160))), desno=Drevo(('Cvetko', 340), levo=Drevo(('Zoran', 160)), desno=Drevo(('Ignac', 130)))), desno=Drevo(('Jani', 710), levo=Drevo(('Ernest', 360), levo=Drevo(('Bernard', 180)), desno=Drevo(('Filip', 130))), desno=Drevo(('Jernej', 400), levo=Drevo(('Božidar', 170)), desno=Drevo(('Valentin', 180))))))""", 50),
                ("""koliko_ponikne(Drevo(('Rok', 1690), levo=Drevo(('Ivo', 940), levo=Drevo(('Aljoša', 620), levo=Drevo(('Anej', 190), levo=Drevo(('Dejan', 180)), desno=Drevo(('Matic', 110))), desno=Drevo(('Stjepan', 370), levo=Drevo(('Peter', 190)), desno=Drevo(('Željko', 120)))), desno=Drevo(('Janko', 370), levo=Drevo(('Aleks', 240), levo=Drevo(('Rudolf', 140)), desno=Drevo(('Tilen', 150))), desno=Drevo(('Zdravko', 240), levo=Drevo(('Franjo', 190)), desno=Drevo(('Niko', 120))))), desno=Drevo(('Robert', 750), levo=Drevo(('Drago', 320), levo=Drevo(('Maks', 210), levo=Drevo(('Igor', 150)), desno=Drevo(('Milan', 180))), desno=Drevo(('Filip', 240), levo=Drevo(('Primož', 200)), desno=Drevo(('Joško', 150)))), desno=Drevo(('Patrik', 550), levo=Drevo(('Miro', 460), levo=Drevo(('Ivan', 190)), desno=Drevo(('Matevž', 180))), desno=Drevo(('Jožef', 160), levo=Drevo(('Nikolaj', 110)), desno=Drevo(('Gal', 160)))))))""", 1040),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ("""goljufi(Drevo(('Salvatore', 320), levo=Drevo(('Bernardo', 200), levo=Drevo(('Matteo', 50)), desno=Drevo(('Carlo', 100), levo=Drevo(('Rosalia', 70)), desno=Drevo(('Tommaso', 50)))), desno=Drevo(('Francesco', 120), levo=Drevo(('Giuseppe', 70)), desno=Drevo(('Antonio', 60)))))""",
                 {('Francesco', 10), ('Carlo', 20)}),
                ("""goljufi(Drevo(('Mirsad', 1030), levo=Drevo(('Slobodan', 570), levo=Drevo(('Vid', 220), levo=Drevo(('Ervin', 140)), desno=Drevo(('Andraž', 200))), desno=Drevo(('Rok', 430), levo=Drevo(('Ivo', 190)), desno=Drevo(('Maks', 150)))), desno=Drevo(('Miro', 460), levo=Drevo(('Leopold', 210), levo=Drevo(('Lovro', 130)), desno=Drevo(('Tine', 190))), desno=Drevo(('Jože', 300), levo=Drevo(('Maj', 200)), desno=Drevo(('Andrej', 150))))))""",
                 {('Slobodan', 80), ('Leopold', 110), ('Miro', 50), ('Vid', 120), ('Jože', 50)}),
                ("""goljufi(Drevo(('Rok', 1550), levo=Drevo(('Aljoša', 840), levo=Drevo(('Anže', 420), levo=Drevo(('Tomislav', 190)), desno=Drevo(('Stanko', 160))), desno=Drevo(('Cvetko', 340), levo=Drevo(('Zoran', 160)), desno=Drevo(('Ignac', 130)))), desno=Drevo(('Jani', 710), levo=Drevo(('Ernest', 360), levo=Drevo(('Bernard', 180)), desno=Drevo(('Filip', 130))), desno=Drevo(('Jernej', 400), levo=Drevo(('Božidar', 170)), desno=Drevo(('Valentin', 180))))))""",
                 {('Jani', 50)}),
                ("""goljufi(Drevo(('Rok', 1690), levo=Drevo(('Ivo', 940), levo=Drevo(('Aljoša', 620), levo=Drevo(('Anej', 190), levo=Drevo(('Dejan', 180)), desno=Drevo(('Matic', 110))), desno=Drevo(('Stjepan', 370), levo=Drevo(('Peter', 190)), desno=Drevo(('Željko', 120)))), desno=Drevo(('Janko', 370), levo=Drevo(('Aleks', 240), levo=Drevo(('Rudolf', 140)), desno=Drevo(('Tilen', 150))), desno=Drevo(('Zdravko', 240), levo=Drevo(('Franjo', 190)), desno=Drevo(('Niko', 120))))), desno=Drevo(('Robert', 750), levo=Drevo(('Drago', 320), levo=Drevo(('Maks', 210), levo=Drevo(('Igor', 150)), desno=Drevo(('Milan', 180))), desno=Drevo(('Filip', 240), levo=Drevo(('Primož', 200)), desno=Drevo(('Joško', 150)))), desno=Drevo(('Patrik', 550), levo=Drevo(('Miro', 460), levo=Drevo(('Ivan', 190)), desno=Drevo(('Matevž', 180))), desno=Drevo(('Jožef', 160), levo=Drevo(('Nikolaj', 110)), desno=Drevo(('Gal', 160)))))))""",
                 {('Janko', 110), ('Anej', 100), ('Robert', 120), ('Patrik', 70), ('Ivo', 50), ('Filip', 110), ('Zdravko', 70), ('Aleks', 50), ('Drago', 130), ('Maks', 120), ('Jožef', 110)}),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ("""zasluzek(Drevo(('Salvatore', 320), levo=Drevo(('Bernardo', 200), levo=Drevo(('Matteo', 50)), desno=Drevo(('Carlo', 100), levo=Drevo(('Rosalia', 70)), desno=Drevo(('Tommaso', 50)))), desno=Drevo(('Francesco', 120), levo=Drevo(('Giuseppe', 70)), desno=Drevo(('Antonio', 60)))))""",
                 (300, 50)),
                ("""zasluzek(Drevo(('Mirsad', 1030), levo=Drevo(('Slobodan', 570), levo=Drevo(('Vid', 220), levo=Drevo(('Ervin', 140)), desno=Drevo(('Andraž', 200))), desno=Drevo(('Rok', 430), levo=Drevo(('Ivo', 190)), desno=Drevo(('Maks', 150)))), desno=Drevo(('Miro', 460), levo=Drevo(('Leopold', 210), levo=Drevo(('Lovro', 130)), desno=Drevo(('Tine', 190))), desno=Drevo(('Jože', 300), levo=Drevo(('Maj', 200)), desno=Drevo(('Andrej', 150))))))""",
                 (1350, 90)),
                ("""zasluzek(Drevo(('Rok', 1550), levo=Drevo(('Aljoša', 840), levo=Drevo(('Anže', 420), levo=Drevo(('Tomislav', 190)), desno=Drevo(('Stanko', 160))), desno=Drevo(('Cvetko', 340), levo=Drevo(('Zoran', 160)), desno=Drevo(('Ignac', 130)))), desno=Drevo(('Jani', 710), levo=Drevo(('Ernest', 360), levo=Drevo(('Bernard', 180)), desno=Drevo(('Filip', 130))), desno=Drevo(('Jernej', 400), levo=Drevo(('Božidar', 170)), desno=Drevo(('Valentin', 180))))))""",
                 (1300, 300)),
                ("""zasluzek(Drevo(('Rok', 1690), levo=Drevo(('Ivo', 940), levo=Drevo(('Aljoša', 620), levo=Drevo(('Anej', 190), levo=Drevo(('Dejan', 180)), desno=Drevo(('Matic', 110))), desno=Drevo(('Stjepan', 370), levo=Drevo(('Peter', 190)), desno=Drevo(('Željko', 120)))), desno=Drevo(('Janko', 370), levo=Drevo(('Aleks', 240), levo=Drevo(('Rudolf', 140)), desno=Drevo(('Tilen', 150))), desno=Drevo(('Zdravko', 240), levo=Drevo(('Franjo', 190)), desno=Drevo(('Niko', 120))))), desno=Drevo(('Robert', 750), levo=Drevo(('Drago', 320), levo=Drevo(('Maks', 210), levo=Drevo(('Igor', 150)), desno=Drevo(('Milan', 180))), desno=Drevo(('Filip', 240), levo=Drevo(('Primož', 200)), desno=Drevo(('Joško', 150)))), desno=Drevo(('Patrik', 550), levo=Drevo(('Miro', 460), levo=Drevo(('Ivan', 190)), desno=Drevo(('Matevž', 180))), desno=Drevo(('Jožef', 160), levo=Drevo(('Nikolaj', 110)), desno=Drevo(('Gal', 160)))))))""",
                 (2520, 210)),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
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
