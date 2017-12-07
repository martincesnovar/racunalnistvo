# =============================================================================
# Preurejanje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@010464=
# 1. podnaloga
# Sestavite funkcijo `preuredi_parnost(v)`, ki kot argument prejme referenco na
# vozel ter verigo vozlov tako preuredi, da postavi vse vozle, ki vsebujejo lih
# podatek na začetek, vozle, ki vsebujejo sod podatek pa na konec. Funkcija naj
# vrne referenco na začetek preurejene verige. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v = preuredi_parnost(v)
#     >>> v.vrni_seznam()
#     [7, 5, 1, 3, 9, 2, 4, 8]
# =============================================================================

def pridruzi(v1,v2):
    '''priduzi verigo'''
    p = v1
    while p.naslednji is not None:
        p = p.naslednji
    p.naslednji = v2
    return v1

def preuredi_parnost(v):
    '''lihe postavi pred sode'''
    sodi, lihi = sodi_in_lihi(v)
    return pridruzi(lihi,sodi)

# =====================================================================@010465=
# 2. podnaloga
# Pepi je sestavil verigo vozlov in ugotovil, da je elemente nizal v seznam
# v napačnem vrstnem redu. Zdaj je treba seznam obrniti, tako da obstoječih
# vozlov ne brišemo in ne dodajamo novih. Sestavite funkcijo `obrni_na_mestu(v)`,
# ki dobi verigo vozlov in jo obrne na mestu. Funkcijo mora vrniti referenco
# na prvi vozel. Zgled:
# 
#     >>> v = iz_seznama([7, 5, 2, 1])
#     >>> v = obrni_na_mestu(v)
#     >>> v.vrni_seznam()
#     [1, 2, 5, 7]
# =============================================================================

def obrni_na_mestu(v):
    '''obrne verižni seznam na mestu'''
    predhodni = None
    while v is not None:
        naslednji = v.naslednji
        v.naslednji = predhodni
        predhodni = v
        v = naslednji
    return predhodni
# =====================================================================@010466=
# 3. podnaloga
# Napišite funkcijo `uredi_z_izbiranjem(v)`, ki verigo vozlov uredi z izbiranjem.
# Funkcija naj deluje tako, da najprej ustvari novo prazno verigo. V seznamu
# `v` naj poišče največji element ter ga prestavi na začetek nove verige. To naj
# ponavlja, doker v seznamu `v` ne zmanjka elementov. Funkcija naj vrne referenco
# na prvi vozel v urejeni verigi. Zgled:
# 
#     >>> v = iz_seznama([4, 7, 3, 6, 5, 2, 1])
#     >>> v = uredi_z_izbiranjem(v)
#     >>> vrni_seznam(v)
#     [1, 2, 3, 4, 5, 6, 7]
# =============================================================================

class Vozel:
    """
    Osnovni sestavni del verižnega seznama.
    """

    def __init__(self, podatek=None, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        return str(self.podatek)


def vrni_seznam(prvi):
    '''Vrne seznam'''
    sez = []
    p = prvi
    if p.podatek is None and p.naslednji is None:
        return []
    while p is not None:
        sez.append(p.podatek)
        p = p.naslednji
    return sez

def iz_seznama(sez):
    '''Vrni verižni seznam, ki bo imel kot podatke elemente seznama sez.'''
    if len(sez) == 0:
        return Vozel()
    prvi = v = Vozel(sez[0])
    for i in range(1,len(sez)):
        v.naslednji = Vozel(sez[i])
        v = v.naslednji
    return prvi

def uredi_z_izbiranjem(v):
    '''Uredi verižni seznam z izbiranjem'''
    vozel = None
    while v is not None:
        p = v
        naj = p.podatek
        vozel_pred_p = None
        pred = None #Vozel pred največjim
        while p is not None:
            if p.podatek > naj:
                naj = p.podatek
                pred = vozel_pred_p
            vozel_pred_p = p
            p = p.naslednji
        if pred is None:
            p = v
            v = p.naslednji
        else:
            p = pred.naslednji
            pred.naslednji = p.naslednji
        p.naslednji = vozel
        vozel = p
    return vozel




































































































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
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjEwNDY0fQ:1eMqU0:EIPxKoxtsamDiqaMSxHLrzbYaUM'
        
        try:
            test_data = [
                (["v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])",
                  "v = preuredi_parnost(v)",
                  "l = vrni_seznam(v)"],
                 {'l': [7, 5, 1, 3, 9, 2, 4, 8]}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjEwNDY1fQ:1eMqU0:EeSITdo4lN_piIhMPLBjP9C5zAs'
        
        try:
            test_data = [
                (["v = iz_seznama([7, 5, 2, 1])",
                  "v = obrni_na_mestu(v)",
                  "l = vrni_seznam(v)"],
                 {'l': [1, 2, 5, 7]}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjEwNDY2fQ:1eMqU0:ZKt7zqwsQFgMTdhnlO08Oj4NSPE'
        
        try:
            Check.run(["v = iz_seznama([4, 7, 3, 6, 5, 2, 1])",
                       "v = uredi_z_izbiranjem(v)",
                       "s = vrni_seznam(v)"],
                      {'s': [1, 2, 3, 4, 5, 6, 7]})
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
