# =============================================================================
# Delo z vrsto
# =====================================================================@010435=
# 1. podnaloga
# Napišite funkcijo `prestej_elemente(v)`, ki kot argument dobi vrsto `v` in
# vrne število elementov v vrsti. Ko funkcija konča, mora biti vrsta `v` enakem
# stanju kot na začetku.
# 
# Zgled:
# 
#     >>> v = Vrsta([4, 5, 6])
#     >>> v.vstavi(7)
#     >>> prestej_elemente(v)
#     4
#     >>> v
#     Vrsta([4, 5, 6, 7])
# =============================================================================
from vrsta import *


# Spodnja funkcija sicer prešteje elemente, ampak jih pri tem tudi vse zavrže.
def prestej_elemente(v):
    '''presteje elemente'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        stevec += 1
        pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec
# =====================================================================@010436=
# 2. podnaloga
# Sestavite funkcijo `prestej_pogojno(v, p)`, ki kot argument dobi vrsto `v`
# in funkcijo `p` (funkcija `p` dobi en argument in vrne logično vrednost) ter
# prešteje koliko je takih elementov v vrsti, za katere funkcija `p` vrne True.
# Ko funkcija konča, mora biti vrsta `v` enakem stanju kot na začetku.
# 
# Zgled:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])
#     >>> prestej_pogojno(v, lambda x: x % 2 == 0)
#     4
# =============================================================================

def prestej_pogojno(v, p):
    '''presteje tiste elemente vrste, ki vrnejo true'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        if p(v.zacetek()):
            stevec+=1
        pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec

# =====================================================================@010437=
# 3. podnaloga
# Sestavite funkcijo `odstrani_ntega(v, n)`, ki kot argumenta dobi vrsto `v`
# in celo število `n`. Funkcija naj iz vrste `v` odstrani $n$-ti zaporedni
# element (šteti začnemo pri 0). Če vrsta ne vsebuje $n$-tega (ker je prekratka),
# naj je funkcija ne spremeni.
# 
# Primer:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7])
#     >>> odstrani_ntega(v, 3)
#     >>> v
#     Vrsta([1, 2, 3, 5, 6, 7])
# =============================================================================

def odstrani_ntega(v, n):
    '''odstrani n-ti element vrste štejemo z 0'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        if stevec!=n:
            pomozna.vstavi(v.zacetek())
        stevec += 1
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec

# =====================================================================@010438=
# 4. podnaloga
# Sestavite funkcijo `odstrani_pogojno(v, p)`, ki kot argumenta dobi vrsto `v`
# in funkcijo `p` (funkcija `p` dobi en argument in vrne logično vrednost) ter
# odstrani tiste elemente v vrsti, za katere funkcija `p` vrne `True`.
# 
# Primer:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])
#     >>> odstrani_pogojno(v, lambda x: x % 2 == 0)
#     >>> v
#     Vrsta([1, 3, 5, 7])
# =============================================================================

def odstrani_pogojno(v, p):
    '''odstrani tiste elemente, kjer vrne fukncija p True'''
    pomozna = Vrsta(None)
    while not v.prazna():
        if not p(v.zacetek()):
            pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()

# =====================================================================@010439=
# 5. podnaloga
# Sestavite funkcijo `obrni(v)`, ki obrne vrsto `v`. Pri tem si pomagajte s
# skladom.
# 
# Zgled:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5])
#     >>> obrni(v)
#     >>> v
#     Vrsta([5, 4, 3, 2, 1])
# =============================================================================
from sklad import *
def obrni(v):
    '''s pomočjo sklada obrne vrsto'''
    s = Sklad()
    while not v.prazna(): #damo na sklad
        s.vstavi(v.zacetek())
        v.odstrani()
    while not s.prazen(): #vrnemo nazaj v vrsto -obratni vrstni red
        v.vstavi(s.vrh())
        s.odstrani()




































































































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
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "st = prestej_elemente(v)",
                       "potem = str(v)"],
                      {'st': 8,
                       'potem': 'ZACETEK : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : KONEC'})
            Check.run(["v = Vrsta([1, 2])",
                       "v.vstavi(3)",
                       "st = prestej_elemente(v)",
                       "v.vstavi(4)",
                       "potem = str(v)"],
                      {'st': 3,
                       'potem': 'ZACETEK : 1 : 2 : 3 : 4 : KONEC'})
            Check.run(["v = Vrsta()",
                       "st = prestej_elemente(v)",
                       "potem = str(v)"],
                      {'st': 0,
                       'potem': 'ZACETEK : KONEC'})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "st = prestej_pogojno(v, lambda x: x % 2 == 0)",
                       "potem = str(v)"],
                      {'st': 4,
                       'potem': 'ZACETEK : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : KONEC'})
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])",
                       "st = prestej_pogojno(v, lambda x: x > 7)",
                       "potem = str(v)"],
                      {'st': 3,
                       'potem': 'ZACETEK : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10 : KONEC'})
            Check.run(["v = Vrsta([1, 2])",
                       "v.vstavi(3)",
                       "st = prestej_pogojno(v, lambda x: x % 2 == 0)",
                       "v.vstavi(4)",
                       "potem = str(v)"],
                      {'st': 1,
                       'potem': 'ZACETEK : 1 : 2 : 3 : 4 : KONEC'})
            Check.run(["v = Vrsta()",
                       "st = prestej_pogojno(v, lambda x: x % 2 == 0)",
                       "potem = str(v)"],
                      {'st': 0,
                       'potem': 'ZACETEK : KONEC'})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "odstrani_ntega(v, 3)",
                       "potem1 = str(v)",
                       "odstrani_ntega(v, 5)",
                       "potem2 = str(v)",
                       "odstrani_ntega(v, 3)",
                       "potem3 = str(v)"],
                      {'potem1': 'ZACETEK : 1 : 2 : 3 : 5 : 6 : 7 : 8 : KONEC',
                       'potem2': 'ZACETEK : 1 : 2 : 3 : 5 : 6 : 8 : KONEC',
                       'potem3': 'ZACETEK : 1 : 2 : 3 : 6 : 8 : KONEC'})
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "odstrani_ntega(v, 8)",
                       "odstrani_ntega(v, 9)",
                       "odstrani_ntega(v, 10)",
                       "potem = str(v)"],
                      {'potem': 'ZACETEK : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : KONEC'})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "odstrani_pogojno(v, lambda x: x % 2 == 0)",
                       "potem = str(v)"],
                      {'potem': 'ZACETEK : 1 : 3 : 5 : 7 : KONEC'})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            Check.run(["v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])",
                       "obrni(v)",
                       "potem = str(v)"],
                      {'potem': 'ZACETEK : 8 : 7 : 6 : 5 : 4 : 3 : 2 : 1 : KONEC'})
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
