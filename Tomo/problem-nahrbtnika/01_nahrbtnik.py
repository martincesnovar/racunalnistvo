# =============================================================================
# 0/1 nahrbtnik
#
# Pri reševanju problema 0/1 nahrbtnika imamo opravka z množicami $S_i$ in $Z_i$.
# Predstavili jih bomo s seznami parov, ki so urejeni naraščajoče po prvih komponentah.
# =====================================================================@010501=
# 1. podnaloga
# Sestavi funkcijo `preveri(s)`, ki za parameter `s` dobi seznam parov.
# Funkcija naj ugotovi, ali ta seznam lahko (teoretično) predstavlja
# neko množico $S$ za nek problem 0/1 nahrbtnika.
# 
#     >>> preveri([(0,0),(3,7),(4,9),(8,12),(11,17),(20,33)])
#     True
# =============================================================================

def preveri(s):
    '''Preveri ali lahko seznam teoretično predstavlja problem 01 nahrbtnika
    s = [(0,0),(x,y),....]'''
    if s==[] or (0,0) != s[0]:
        return False
    for i in range(1, len(s)):
        if s[i-1][0]>= s[i][0]: return False
        if s[i-1][1]>= s[i][1] < 0: return False
    return True

# =====================================================================@010502=
# 2. podnaloga
# Sestavi funkcijo `sestaviZ(s, predmet)`, ki za neko množico $S_i$ in predmet,
# podan s parom `(velikost, vrednost)`, sestavi in vrne množico $Z_{i+1}$.
# 
#     >>> sestaviZ([(0,0),(1,1),(2,2),(3,3)], (4,4))
#     [(4,4),(5,5),(6,6),(7,7)]
# =============================================================================
def sestaviZ(s, predmet):
    '''Sestavi množico z'''
    vel,vred = predmet
    sez = []
    for veli,vre in s:
        sez.append((vel+veli,vred+vre))
    return sez
        
# =====================================================================@010503=
# 3. podnaloga
# Sestavi funkcijo `sestaviS(s, z)`, ki iz množic $S_i$ in $Z_{i+1}$
# sestavi in vrne množico $S_{i+1}$.
# 
#     >>> sestaviS([(0,0),(11,6),(40,9),(51,15)], [(16,4),(27,10),(56,13),(67,19)])
#     [(0,0),(11,6),(27,10),(51,15),(67,19)]
# 
# Bi lahko kaj "poenostavil", če bi poznal velikost nahrbtnika?
# =============================================================================
def sestaviS(s, z):
    '''Sestavi in vrne množico S(i+1)'''
    sez = []
    n = len(s)
    m = len(z)
    i=j=0
    while i < n and j < m:
        if s[i][0] <z[j][0]: #napišemo tistega z manjšo komponento
            sez.append(s[i])
            i+=1
        elif s[i][0] > z[j][0]:
            sez.append(z[j])
            j += 1
        else: #enaka komponenta, tistega z večjo vrednostjo
            if s[i][1] > z[j][1]:
                sez.append(s[i])
            else:
                sez.append(z[j])
            i += 1
            j += 1
        #preskočimo elemente s premajhno komponento
        while i < n and s[i][1] <= sez[-1][1]:
            i += 1
        while j < m and z[j][1] <= sez[-1][1]:
            j += 1
    #dodamo še preostanek
    sez += s[i:]
    sez += z[j:]

    return sez
    
# =====================================================================@010504=
# 4. podnaloga
# Sestavi funkcijo `mnoziceS(predmeti)`, ki za dani seznam predmetov,
# pri čemer je vsak predmet predstavljen s parom `(velikost, vrednost)`,
# sestavi in vrne seznam vseh množic $S$.
# 
#     >>> mnoziceS([(2,3),(4,5),(4,7),(6,8)])
#     [[(0,0)],[(0,0),(2,3)],[(0,0),(2,3),(4,5),(6,8)],[(0,0),(2,3),(4,7),
#        (6,10),(8,12),(10,15)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15),
#        (12,18),(14,20),(16,23)]]
# =============================================================================

def mnoziceS(predmeti):
    '''Vrne množice vseh elementov'''
    sez = [[(0,0)]]
    for predmet in predmeti:
        z = sestaviZ(sez[-1],predmet)
        sez.append(sestaviS(sez[-1],z))
    return sez

# =====================================================================@010505=
# 5. podnaloga
# Sestavi funkcijo `nahrbtnik01(predmeti, velikost)`, ki reši problem
# 0/1 nahrbtnika, kjer je `predmeti` seznam predmetov, predstavljen kot prej,
# `velikost` pa velikost nahrtnika. Funkcija naj vrne skupno velikost in vrednost
# predmetov, ki jih damo v nahrbtnik.
# 
#     >>> nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 9)
#     (8,12)
# =============================================================================

def nahrbtnik01(sez, velikost):
    '''Sestavi nahrbtnik'''
    s = mnoziceS(sez)[-1]
    i=0
    while i <len(s) and s[i][0] <= velikost:
        i+=1
    return s[i-1]

# =====================================================================@010506=
# 6. podnaloga
# Sestavi funkcijo `resitev01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam ničel in enic,
# ki določajo, katere predmete moramo izbrati. Če je rešitev več, naj vrne
# katerokoli izmed njih.
# 
#     >>> resitev01([(2,3),(4,5),(4,7),(6,8)], 9)
#     [0, 1, 1, 0]
# =============================================================================

def resitev01(predmeti, velikost):
    '''Vrne seznam vrednosti elementov, ki jih dodamo v nahrbtnik'''
    s = mnoziceS(predmeti)
    n = len(predmeti)
    sez = [0]*n
    i=0
    while i < len(s[-1]) and s[-1][i][0] <= velikost:
        i += 1
        vel, cena = s[-1][i - 1]
    for k in range(len(predmeti) - 1, -1, -1):
        #zmanjšamo velikost in ceno elementov
        vel0 = vel - predmeti[k][0]
        cena0 = cena - predmeti[k][1]
        if (vel0, cena0) in s[k]:
            sez[k] = 1
            vel, cena = vel0, cena0
    return sez

# =====================================================================@010507=
# 7. podnaloga
# Sestavi funkcijo `resitve01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam vseh možnih rešitev.
# Vrstni red rešitev v seznamu ni pomemben.
# 
#     >>> resitve01([(2,4),(4,5),(4,7),(6,8)], 9)
#     [[0, 1, 1, 0], [1, 0, 0, 1]]
# =============================================================================

def pomozna(predmeti, s, n, v, c):
    if n == 0:
        return [[]]
    v0 = v - predmeti[n - 1][0]
    c0 = c - predmeti[n - 1][1]
    resitve = []

    if (v, c) in s[n - 1]:
        resitve0 = pomozna(predmeti, s, n - 1, v, c)
        for resitev in resitve0:
            resitev.append(0)
        resitve += resitve0

    if (v0, c0) in s[n - 1]:
        v, c = v0, c0
        resitve1 = pomozna(predmeti, s, n - 1, v0, c0)
        for resitev in resitve1:
            resitev.append(1)
        resitve += resitve1

    return resitve

def resitve01(predmeti, velikost):
    '''poiščemo optimalno rešitev'''
    s = mnoziceS(predmeti)
    i = 0
    while i < len(s[-1]) and s[-1][i][0] <= velikost:
        i += 1
    v, c = s[-1][i - 1]

    return pomozna(predmeti, s, len(predmeti), v, c)

# =====================================================================@010508=
# 8. podnaloga
# Sestavi funkcijo `resitev0n(predmeti, velikost)`, ki reši malo spremenjen
# problem nahrbtnika. Vzamemo lahko več enakih predmetov, koliko posameznih
# predmetov imamo na voljo pa je dodano pri opisu posameznega predmeta.
# Namesto para (velikost, cena) imamo torej trojko (velikost, cena, količina).
# Funkcija naj vrne seznam celih števil, ki določajo, koliko katerih predmetov
# moramo vzeti. Če je rešitev več, naj vrne katerokoli izmed njih.
# Namig: pretvori problem na običajen problem 0/1 nahrbtnika.
# 
#     >>> resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 15)
#     [2, 0, 1, 1]
# =============================================================================

def resitev0n(predmeti, velikost):
    '''pretvori poseben 01 nahrbtnik v običajnega'''
    sez = []
    for v, c, k in predmeti:
        for i in range(k):
            sez.append((v, c))

    resitev = resitev01(sez, velikost) #prevedemo na običajen 01 nahrbtnik

    rez = []
    i = 0
    for v, c, k in predmeti:
        rez.append(sum(resitev[i:i+k]))
        i += k
    return rez




































































































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
                ('preveri([(0,0),(3,7),(4,9),(8,12),(11,17),(20,33)])', True),
                ('preveri([])', False),
                ('preveri([(0,0)])', True),
                ('preveri([(1,2)])', False),
                ('preveri([(0,0),(5,9)])', True),
                ('preveri([(0,0),(-5,9)])', False),
                ('preveri([(0,0),(5,-9)])', False),
                ('preveri([(0,0),(0,9)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,20),(98,19),(96,21),(103,23),(102,25),(128,28),(144,32)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,16),(98,19),(96,21),(103,23),(102,25),(128,28),(144,32)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,16),(98,19),(99,21),(103,23),(106,25),(128,28),(144,32)])', True),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('sestaviZ([(0,0),(1,1),(2,2),(3,3)], (4,4))', [(4,4),(5,5),(6,6),(7,7)]),
                ('sestaviZ([(0,0),(11,6),(27,10),(51,15),(67,19)], (32,7))', [(32,7),(43,13),(59,17),(83,22),(99,26)]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('sestaviS([(0,0)], [(11,6)])', [(0,0),(11,6)]),
                ('sestaviS([(0,0),(11,6)], [(40,9),(51,15)])', [(0,0),(11,6),(40,9),(51,15)]),
                ('sestaviS([(0,0),(11,6),(40,9),(51,15)], [(16,4),(27,10),(56,13),(67,19)])', [(0,0),(11,6),(27,10),(51,15),(67,19)]),
                ('sestaviS([(0,0),(11,6),(27,10),(51,15),(67,19)], [(32,7),(43,13),(59,17),(83,22),(99,26)])', [(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)]),
                ('sestaviS([(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)], [(45,6),(56,12),(72,16),(88,19),(96,21),(104,23),(112,25),(128,28),(144,32)])', [(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(144,32)]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('mnoziceS([(2,3),(4,5),(4,7),(6,8)])', [[(0,0)],[(0,0),(2,3)],[(0,0),(2,3),(4,5),(6,8)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15),(12,18),(14,20),(16,23)]]),
                ('mnoziceS([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)])', [[(0,0)],[(0,0),(11,6)],[(0,0),(11,6),(40,9),(51,15)],[(0,0),(11,6),(27,10),(51,15),(67,19)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(144,32)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(131,29),(144,32),(147,33),(176,35),(192,39)],[(0,0),(9,5),(11,6),(20,11),(36,15),(52,18),(60,20),(68,22),(76,24),(92,27),(108,31),(137,33),(140,34),(153,37),(156,38),(185,40),(201,44)],[(0,0),(9,5),(11,6),(20,11),(36,15),(52,18),(60,20),(68,22),(76,24),(92,27),(104,29),(108,31),(120,33),(136,36),(152,40),(181,42),(184,43),(197,46),(200,47),(229,49),(245,53)]]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 9)', (8,12)),
                ('nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 13)', (12,18)),
                ('nahrbtnik01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', (152, 40)),
                ('nahrbtnik01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', (245, 53)),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('resitev01([(2,3),(4,5),(4,7),(6,8)], 9)', [0, 1, 1, 0]),
                ('resitev01([(2,3),(4,5),(4,7),(6,8)], 13)', [1, 0, 1, 1]),
                ('resitev01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', [1, 1, 1, 1, 0, 0, 1, 1]),
                ('resitev01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', [1, 1, 1, 1, 1, 1, 1, 1]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('resitve01([(2,3),(4,5),(4,7),(6,8)], 9)', [[0, 1, 1, 0]]),
                ('resitve01([(2,3),(4,5),(4,7),(6,8)], 13)', [[1, 0, 1, 1]]),
                ('sorted(resitve01([(2,4),(4,5),(4,7),(6,8)], 9))', [[0, 1, 1, 0], [1, 0, 0, 1]]),
                ('resitve01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', [[1, 1, 1, 1, 0, 0, 1, 1]]),
                ('resitve01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', [[1, 1, 1, 1, 1, 1, 1, 1]]),
                ('sorted(resitve01([(10,8),(42,7),(16,9),(45,4),(45,3),(68,24),(9,5),(44,4)], 70))', [[0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0]]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        
        try:
            test_data = [
                ('resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 15)', [2, 0, 1, 1]),
                ('resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 25)', [2, 1, 1, 2]),
                ('resitev0n([(11,3,2),(40,9,2),(16,4,1),(32,7,3),(45,6,2),(48,7,1),(9,5,5),(44,9,1)], 200)', [2, 2, 1, 1, 0, 0, 5, 0]),
            ]
            for data in test_data:
                if not Check.equal(*data):
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
