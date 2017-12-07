# =============================================================================
# Verižni seznam
#
# Verižni seznam predstavimo z verigo vozlov ter kazalcema, ki kažeta na
# začetni in končni vozel v tej verigi. Za osnovo si bomo vzeli razred `Vozel`,
# kot ga poznamo že od prej:
# 
#     class Vozel:
#         '''
#         Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
#         '''
#         def __init__(self, podatek, naslednji=None):
#             self.podatek = podatek
#             self.naslednji = naslednji
# 
# ter razred `VerizniSeznam`:
# 
#     class VerizniSeznam:
#         '''
#         Razred, ki predstavlja verižni seznam z začetkom in koncem.
#         '''
#         def __init__(self):
#             self._zacetek = None
#             self._konec = None
#    
#         def __str__(self):
#             niz = ''
#             vozel = self._zacetek
#             while vozel is not None:
#                 niz += '{} -> '.format(repr(vozel.podatek))
#                 vozel = vozel.naslednji
#             return niz + '•'
# 
# Pozorni bodite, da se imeni atributov, v katerih sta shranjena kazalca na
# začetek in konec verige vozlov, začneta s podčrtajem, s čimer želimo povedati,
# da naj uporabnik podatkovne strukture do njih ne dostopa direktno. V ta namen
# bomo raje malo kasneje definirali metodi `zacetek` in `konec`.
# =====================================================================@011065=
# 1. podnaloga
# Dopolnite obstoječi razred `VerizniSeznam` tako, da dopišete še
# metodo `vstavi_na_zacetek(self, podatek)`, ki `podatek` vstavi na
# začetek seznama (pazite pri vstavljanju v prazen seznam).
# =============================================================================
class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'

    def vstavi_na_zacetek(self, podatek):
        '''vstavi podatek na zacetek'''
        if self._zacetek is None and self._konec is None: # če je prazen
            self._zacetek = Vozel(podatek)
            self._konec = Vozel(podatek)
        else:
            self._zacetek = Vozel(podatek, self._zacetek)
            
        
# =====================================================================@011066=
# 2. podnaloga
# Dopišite še metodo `zacetek(self)`, ki vrne podatek na začetku
# verižnega seznama. Če je seznam prazen, naj metoda sproži izjemo
# `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def zacetek(self):
        '''vrne podatek na začetku'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        return self._zacetek.podatek

# =====================================================================@011067=
# 3. podnaloga
# Dodajte še metodo `izbrisi_zacetek(self)`, ki izbriše element na začetku
# verižnega seznama (pazite na seznam dolžine 1). Če je seznam prazen, naj
# metoda sproži izjemo `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def izbrisi_zacetek(self):
        '''izbriše začetek'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        if self._zacetek == self._konec: #če je le 1 element ga odstranimo
            self._zacetek = self._konec = None
        self._zacetek = self._zacetek.naslednji

# =====================================================================@011068=
# 4. podnaloga
# Razred `VerizniSeznam` naj sedaj pozna še metodo
# `vstavi_na_konec(self, podatek)`, ki `podatek` vstavi na
# konec seznama (pazite pri vstavljanju v prazen seznam).
# =============================================================================

    def vstavi_na_konec(self, podatek):
        '''Vstavi na konec'''
        if self._konec: # če ni prazen
            self._konec.naslednji = Vozel(podatek)
            self._konec = self._konec.naslednji
        else:
            self._zacetek = self._konec = Vozel(podatek)

        

# =====================================================================@011069=
# 5. podnaloga
# Dopišite še metodo `konec(self)`, ki vrne podatek na koncu
# verižnega seznama. Če je seznam prazen, naj metoda sproži izjemo
# `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def konec(self):
        '''vrne konec'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        return self._konec.podatek

# =====================================================================@011070=
# 6. podnaloga
# Sestavite metodo `izbrisi_konec(self)`, ki izbriše element na koncu
# verižnega seznama (pazite na seznam dolžine 1). Če je seznam prazen, naj
# metoda sproži izjemo `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def izbrisi_konec_N(self):
        '''izbriše konec'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        elif self._zacetek == self._konec: #če je le 1 element ga odstranimo
            self._zacetek = self._konec = None
        else:
            if self._zacetek.naslednji:
                prvi = self._zacetek
                while prvi.naslednji.naslednji is not None:
                    prvi = prvi.naslednji #smo na novem zadnjem
                self._konec = prvi
                prvi.naslenji = None
                self._konec = prvi
                self._konec.naslednji = None
    def izbrisi_konec(self):
        '''Izbriši podatek na koncu seznama.'''
        if self._zacetek and self._zacetek.naslednji:
            vozel = self._zacetek
            while vozel.naslednji.naslednji is not None:
                vozel = vozel.naslednji
            self._konec = vozel
            vozel.naslednji = None
        elif self._zacetek:
            self._zacetek = self._konec = None
        else: raise IndexError('Verižni seznam je prazen') 
        

# =====================================================================@011071=
# 7. podnaloga
# Definicijo razreda `VerizniSeznam` zaključimo z metodo `je_prazen(self)`,
# ki vrne `True`, če je verižni seznam prazen, in `False`, če ni.
# =============================================================================

    def je_prazen(self):
        '''Preverimo ali je prazen'''
        return self._zacetek is None and self._konec is None


def je_cikel(verizni_seznam):
    '''preveri ali ima verizni seznam cikel algoritem zajca in želve'''
    pocasen = hiter = verizni_seznam.zacetek()
    while hiter and hiter.naslednji:
        pocasen = pocasen.naslednji
        hiter = hiter.naslednji.naslednji
        if hiter == pocasen:
            return True
    return False




































































































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
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDY1fQ:1eMqU0:m0isakzrdlJytm-h9cwOFfzW5E4'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                'niz = str(s)',
            ], {'niz': '•'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                'niz = str(s)',
            ], {'niz': '10 -> •'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.vstavi_na_zacetek(20)',
                'niz = str(s)',
            ], {'niz': '20 -> 10 -> •'})
            Check.run([
                's = VerizniSeznam()',
                "s.vstavi_na_zacetek('10')",
                "s.vstavi_na_zacetek('20')",
                'niz = str(s)',
            ], {'niz': "'20' -> '10' -> •"})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDY2fQ:1eMqU0:5OV4qpLsHmC7FAW-ZjaLk3XkFZU'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                'zacetek = s.zacetek()',
            ], {'zacetek': 10})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.vstavi_na_zacetek(20)',
                'zacetek = s.zacetek()',
            ], {'zacetek': 20})
            try:
                VerizniSeznam().zacetek()
            except IndexError as exc:
                if exc.args != ('Verižni seznam je prazen',):
                    Check.error('Klic metode na praznem seznamu sproži IndexError z napačnim argumentom.')
            except:
                Check.error('Klic metode na praznem seznamu sproži napačno izjemo.')
            else:
                Check.error('Klic metode na praznem seznamu ne sproži izjeme.')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDY3fQ:1eMqU0:vJnOKgAQWarhyVBalPA2r83gt6k'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.izbrisi_zacetek()',
                'niz = str(s)',
            ], {'niz': '•'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.vstavi_na_zacetek(20)',
                's.izbrisi_zacetek()',
                'niz = str(s)',
            ], {'niz': '10 -> •'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.vstavi_na_zacetek(20)',
                's.vstavi_na_zacetek(30)',
                's.izbrisi_zacetek()',
                'niz = str(s)',
            ], {'niz': '20 -> 10 -> •'})
            try:
                VerizniSeznam().izbrisi_zacetek()
            except IndexError as exc:
                if exc.args != ('Verižni seznam je prazen',):
                    Check.error('Klic metode na praznem seznamu sproži IndexError z napačnim argumentom.')
            except:
                Check.error('Klic metode na praznem seznamu sproži napačno izjemo.')
            else:
                Check.error('Klic metode na praznem seznamu ne sproži izjeme.')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDY4fQ:1eMqU0:L4PLGG0n5I4-3Snl7PukKW5O2nA'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                'niz = str(s)',
            ], {'niz': '•'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                'niz = str(s)',
            ], {'niz': '10 -> •'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.vstavi_na_konec(20)',
                'niz = str(s)',
            ], {'niz': '10 -> 20 -> •'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.vstavi_na_zacetek(0)',
                's.vstavi_na_konec(20)',
                'niz = str(s)',
            ], {'niz': "0 -> 10 -> 20 -> •"})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDY5fQ:1eMqU0:FXB7d30ziYE9PJeQp1vMPyaCtPg'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                'konec = s.konec()',
            ], {'konec': 10})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.vstavi_na_konec(20)',
                'konec = s.konec()',
            ], {'konec': 20})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.vstavi_na_zacetek(20)',
                'konec = s.konec()',
            ], {'konec': 10})
            try:
                VerizniSeznam().konec()
            except IndexError as exc:
                if exc.args != ('Verižni seznam je prazen',):
                    Check.error('Klic metode na praznem seznamu sproži IndexError z napačnim argumentom.')
            except:
                Check.error('Klic metode na praznem seznamu sproži napačno izjemo.')
            else:
                Check.error('Klic metode na praznem seznamu ne sproži izjeme.')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDcwfQ:1eMqU0:oETSTHI__avlUxf6ZvOVZr0cp80'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.izbrisi_konec()',
                'niz = str(s)',
            ], {'niz': '•'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.izbrisi_konec()',
                's.vstavi_na_konec(20)',
                'niz = str(s)',
            ], {'niz': '20 -> •'})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                's.vstavi_na_konec(20)',
                's.vstavi_na_zacetek(0)',
                's.izbrisi_konec()',
                'niz = str(s)',
            ], {'niz': "0 -> 10 -> •"})
            try:
                VerizniSeznam().izbrisi_konec()
            except IndexError as exc:
                if exc.args != ('Verižni seznam je prazen',):
                    Check.error('Klic metode na praznem seznamu sproži IndexError z napačnim argumentom.')
            except:
                Check.error('Klic metode na praznem seznamu sproži napačno izjemo.')
            else:
                Check.error('Klic metode na praznem seznamu ne sproži izjeme.')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        Check.current_part['token'] = 'eyJ1c2VyIjoxMjAsInBhcnQiOjExMDcxfQ:1eMqU0:MS4AoMj6aZZlPxl21_sePLQLD6A'
        
        try:
            Check.run([
                's = VerizniSeznam()',
                'je_prazen = s.je_prazen()',
            ], {'je_prazen': True})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_konec(10)',
                'je_prazen = s.je_prazen()',
            ], {'je_prazen': False})
            Check.run([
                's = VerizniSeznam()',
                's.vstavi_na_zacetek(10)',
                's.izbrisi_konec()',
                'je_prazen = s.je_prazen()',
            ], {'je_prazen': True})
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
