# =============================================================================
# Enostavne naloge z rekurzijo
# =====================================================================@011120=
# 1. podnaloga
# Sestavite funkcijo `fakulteta(n)`, ki izračuna fakulteto števila `n`.
# Argument `n` je nenegativno celo število. Zgled:
# 
#     >>> fakulteta(5)
#     120
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def fakulteta(n):
    assert n>=0
    if n==0:
        return 1
    return n*fakulteta(n-1)


# =====================================================================@011121=
# 2. podnaloga
# Sestavite funkcijo `gcd(m, n)`, ki izračuna največji skupni delitelj
# števil `m` in `n`. Argumenta `m` in `n` sta nenegativni celi števili.
# Če je $m = 0$ in $n = 0$, naj funkcija vrne vrednost `None`. Zgled:
# 
#     >>> gcd(10, 15)
#     5
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def gcd(m,n):
    if m==n==0:
        return None
    if n==0:
        return m
    return gcd(n,m%n)

# =====================================================================@011122=
# 3. podnaloga
# Sestavite funkcijo `cantor(n)`, ki kot argument dobi nenegativno celo
# število `n`. Funkcija naj vrne niz dolžine $3^n$ z $n$-tim približkom
# [Cantorjeve množice](http://sl.wikipedia.org/wiki/Cantorjeva_množica).
# Srednja tretjina niza sestoji iz samih presledkov, prva in zadnja tretjina
# niza pa sta $(n-1)$-ta približka Cantorjeve množice; $0$-ti približek
# Cantorjeve množice je niz `'*'`. Zgled:
# 
#     >>> cantor(0)
#     '*'
#     >>> cantor(1)
#     '* *'
#     >>> cantor(2)
#     '* *   * *'
#     >>> cantor(3)
#     '* *   * *         * *   * *'
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def cantor(n):
    niz = ''
    if n==0:
        return '*'
    cantorn1 = cantor(n-1)
    return cantorn1 + ' '*len(cantorn1) + cantorn1
    

# =====================================================================@011123=
# 4. podnaloga
# Sestavite funkcijo `fibonacci(n)`, ki vrne $n$-to Fibonaccijevo število.
# Nalogo bomo rešili z rekurzivno funkcijo, ki uporabi _akumulatorja_, to sta
# pomožna argumenta, v katerih si podajamo delne rezultate.
# 
# Najprej primer uporabe akumulatorjev (`x` je akumulator):
# 
#     def potenca(a, n, x=1):
#         """Izračunaj n-to potenco a."""
#         if n == 0:
#             return x
#         else:
#             return potenca(a, n-1, a*x)
# 
# Na začetku je `x` enak `1`. V vsakem klicu ga množimo z `a`, torej bo po
# `k` klicih enak `a ** k`. Ko pridemo do `n == 0`, je bilo klicev `n` in
# ima `x` želeno vrednost `a ** n`. V nekem smislu smo z rekurzijo simulirali
# zanko, katere števec je `n` in pomožna spremenljivka `x`:
# 
#      x = 1
#      while n > 0:
#          x = a * x
#          n = n - 1
#      return x
# 
# Funkcija `fibonacci` bo imela _dva_ akumulatorja, `fibonacci(n, x=0, y=1)` in
# bo simulirala zanko
# 
#      x = 0
#      y = 1
#      while n > 0:
#          x, y = y, x + y
#          n = n -1
#      return x
# 
# Zgled:
# 
#     >>> fibonacci(7)
#     13
# 
# Testi bodo vašo rešitev preizkusili pri velikih vrednostih argumenta `n`,
# zato rešitev napišite učinkovito.
# =============================================================================

def fibonacci_1(n, _cache={}):
    '''unčinkovita rekurzija
    https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci(n-1) + fibonacci(n-2))
    return n

def fibonacci(n,x=0,y=1):
    if n==0:
        return x
    return fibonacci(n-1,y,x+y)




































































































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
                ("""fakulteta(3)""", 6),
                ("""fakulteta(5)""", 120),
                ("""fakulteta(8)""", 40320),
                ("""fakulteta(10)""", 3628800),
                ("""fakulteta(1)""", 1),
                ("""fakulteta(0)""", 1),
                ("""fakulteta(2)""", 2),
                ("""fakulteta(20)""", 2432902008176640000),
                ("""fakulteta(50)""", 30414093201713378043612608166064768844377641568960512000000000000),
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
                ("""gcd(31, 6)""", 1),
                ("""gcd(315, 0)""", 315),
                ("""gcd(80, 1240)""", 40),
                ("""gcd(124, 80)""", 4),
                ("""gcd(163, 0)""", 163),
                ("""gcd(0, 0)""", None),
                ("""gcd(10533170, 3188141)""", 1),
                ("""gcd(16316360996, 5123428533)""", 1),
                ("""gcd(8538406945, 29509180780)""", 5),
                ("""gcd(290988149, 1024019863)""", 2357),
                ("""gcd(26514440627, 176555737627)""", 21434471),
                ("""gcd(21434471, 1)""", 1),
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
                ("cantor(0)", "*"),
                ("cantor(1)", "* *"),
                ("cantor(2)", "* *   * *"),
                ("cantor(3)", "* *   * *         * *   * *"),
                ("cantor(4)", "* *   * *         * *   * *                           * *   * *         * *   * *"),
                ("cantor(5)", "* *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *"),
                ("cantor(6)", "* *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *                                                                                                                                                                                                                                                   * *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *"),
                ("cantor(7)", "* *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *                                                                                                                                                                                                                                                   * *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         * *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *                                                                                                                                                                                                                                                   * *   * *         * *   * *                           * *   * *         * *   * *                                                                                 * *   * *         * *   * *                           * *   * *         * *   * *"),
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
                ("""fibonacci(1)""", 1),
                ("""fibonacci(3)""", 2),
                ("""fibonacci(4)""", 3),
                ("""fibonacci(9)""", 34),
                ("""fibonacci(20)""", 6765),
                ("""fibonacci(0)""", 0),
                ("""fibonacci(30)""", 832040),
                ("""fibonacci(100)""", 354224848179261915075),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            for i in range(1, 500):
                Check.secret(fibonacci(i), i)
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
