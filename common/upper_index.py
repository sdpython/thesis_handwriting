# coding: cp1252
import sys, re, copy

def get_lines (file) :
    try :
        f = open (file, "r")
        li = f.readlines ()
        f.close ()
        return li
    except Exception as e :
        print ("unable to open file ", file)
        print (e)
        sys.exit (0)
        
remplace = {"é":"e", "à":"a", "è":"e", "î":"i", "ô":"o", "ê":"e", "ë":"e", \
            "ï":"i", "ä":"a", "ö":"o", "ô":"o", "ù":"u", "û":"u", "ü":"u", \
            }

def supper (s) :
    r = ""
    for c in s :
        if 'a' <= c <= 'z' or '0' <= c <= '9' : r += c.upper ()
        elif c in remplace : r += remplace [c].upper ()
        else : r += c
    return r

def modify (line, debug) :
    # textit
    exp = "{\\\\textit[ ]*{.*}@"
    r   = re.compile (exp).search (line, 0)
    if r != None :
        #print line.replace ("\n", "")
        z = re.sub ("{\\\\textit[ ]*{(.*)}@", "{\\1@", line)
        #print r.span ()
        #print z.replace ("\n", "")
        #print
        line = z
        
    r = re.compile ("[{!]?(http://([-\\\\.a-zA-Z0-9_/ ~]*))(}|hyperpage|\\dotfill)?[}]?")
    r = r.search (line)
    r2 = re.compile ("[a-zA_Z0_9]_[a-zA_Z0_9]")
    
    if debug :
        if "http" in line : 
            print ("-------------------------------")
            print ("http ", line.replace ("\n", ""))
    
    if True and r != None :
        url = r.groups () [0]
        print ("url ", "|" + url + "|")
        if len (url) > len ("http://tortoisesvn.tigris.org/")-2 :
            if True :
                url2 = url.replace ("/", "/ ").replace (".", ". ").replace ("#", "# ")
                url2 = url2.replace ("/ / ", "// ")
                if r2.search (url) != None : 
                    url2 = url2.replace ("_", "\\_")
                    url2 = url2.replace ("\\\\_", "\\_")
                url2 = url2.replace ("  ", " ")
                line = line.replace (url, url2)
            else :
                url2 = url.replace (" ", "")
                url2 = url2.replace ("/", "/ ")
                url2 = url2.replace ("/ / ", "// ")
                url2 = url2.replace ("  ", " ")
                if r2.search (url) != None : 
                    url2 = url2.replace ("_", "\\_")
                    url2 = url2.replace ("\\\\_", "\\_")
                url2 = url2.replace ("  ", " ")
                line = line.replace (url, url2)
            print ("-2-", line.replace ("\n", ""))
        
    # suite
    exp  = "(!|{).*?@"
    r    = re.compile (exp).search (line, 0)
    pos  = []
    while r != None and len (r.group ()) != 0 :
        pos.append (r.span ())
        r = re.compile (exp).search (line, r.span () [1]+1)
        
    if len (pos) > 0 :
        old = copy.copy (pos)
        if pos [0][0] != 0 : pos.insert (0, (0,pos [0][0]))
        if pos [len (pos)-1][1] != len (line) : 
            pos.append ( (pos [len (pos)-1][1], len (line)))
        res = []
        for i in range (0, len (pos)-1) :
            res.append (pos [i])
            if pos [i][1] < pos [i+1][0] :
                res.append ( (pos [i][1], pos [i+1][0]) )
        res.append ( pos [len (pos)-1] )
        
        r = ""
        for p in res :
            h = line [ p[0]:p[1] ]
            if p in old : r += supper ( h )
            else : r += h  
    else : r = line
    

    if len (line) != len (r) :
        print (line)
        print (r)

    r = r.replace ("E@ê!LIEN@lien", "zzzz@liens")
    r = r.replace ("§@§", "zzz@numéros")
    r = r.replace ("\\TEXTIT", "\\textit")
    r = r.replace (r"\indexentry{SYMBOLE@", r"\indexentry{(@")
    r = r.replace (r"\indexentry{SYMBOLES \textit  {PYTHON}@", r"\indexentry{(@")
    r = r.replace (r"\indexentry{SYMBOLES PYTHON@", r"\indexentry{(@")
    r = r.replace (r"\indexentry{$\MATHTT", r"\indexentry{$\mathtt")
    r = r.replace ("\\delimiter \"026E30F ", "\\backslash ")
    r = r.replace ("\\DELIMITER \"026E30F ", "\\backslash ")
    
    link = [  "http:// scintilla.sourceforge.net/ SciTEFAQ.html" \
            , "http:// sourceforge.net/ projects/ directpython/ " \
            , "http:// www.die-offenbachs.de/ eric/ index.html" \
            , "http://www.gnu.org/software/emacs/windows/" \
            , "C:/Python25/Lib/site-packages/PythonSample" \
            , "http:// docs.python.org/ dev/ howto/ regex.html" \
            , "http:// gnuprog.info/ prog/ python/ pwidget.php" \
            , "http://docs.python.org/lib/re-syntax.html" \
            , "http://www.xavierdupre.fr/ hal\_python/ hal\_python\_help\_html/ index.html" \
            , "paramètres contenant des espaces" \
            , "événement associé à une méthode" \
            , "Tkinter, séquence d'événéments" \
            , "fonctions et chaînes de caractères" \
            , "appel à une méthode de l’ancêtre" \
            , "http:// docs.python.org/ library/ os.path.html" \
            , "http:// docs.python.org/ library/ datetime.html" \
            , "http:// sourceforge.net/ projects/ mysql-python" \
            , "http:// docs.python.org/ library/ os.path.html" \
            , "http://docs.python.org/library/codecs.html\#id3" \
            , "http://docs.python.org/library/stdtypes.html#set" \
            , "http:// sourceforge.net/ projects/ mysql-python" \
            , "http:// sourceforge. net/  projects/  directpython/" \
            , "http://docs.python.org/library/stdtypes.html\#id4" \
            , "http:// sourceforge. net/ projects/ directpython/" \
            , "http:// sourceforge.net/ projects/ mysql-python" \
            , "http:// docs.python.org/ library/ os.path.html" \
            , "appel à une méthode de l'ancêtre" \
            , "zone de saisie à plusieurs lignes" \
            , "dictionnaire et clé de type tuple" \
            , "Tkinter, séquence d'événements" \
            , "héritage multiple et constructeur" \
            , "return\_internal\_reference}$" \
            , "écriture, lecture de fichier binaire" \
            , "import dynamique d’un module" \
            ]
    
    for l in link :
        if l in r : 
            print ("replacing ", l)
            n = l + " ..."
            r = r.replace (l, n)
    
    r = r.replace ( r"\indexentry{BOOST PYTHON@\textit  {BOOST PYTHON}!",
                    r"\indexentry{BOOST PYTHON@\textit  {Boost Python}!")
    r = r.replace ( r"\indexentry{PROGRAMMES \textit  {PYTHON}@programmes \textit  {PYTHON}!",
                    r"\indexentry{PROGRAMMES \textit  {Python}@programmes \textit  {Python}!")
    r  = r.replace (r"\indexentry{(@symboles \textit  {PYTHON}!",
                    r"\indexentry{(@symboles \textit  {Python}!")
    if "BOOST" in r.upper () : print ("rrr",r)
    
    return r

def main (argv) :
    debug = False
    if len (argv) <= 1 :
        #argv = ["upper_index",  r"D:\Dupre\_data\informatique\support\python_cours\chap1_introduction.idx", "2"]
        argv = ["upper_index",  r"D:\Dupre\_data\informatique\support\python_collection\initiation_via_python_ellipse.idx", "2", "copy"]
        argv = ["upper_index",  r"C:\xadupre\myhome\informatique\support\python_td_minute\python_td_minute.idx", "2", "copy"]
        debug = True

    for i in range (0, len (argv)) :
        print ("argument ", i, " : ", argv [i])

    print ("reading file ", argv [1])
    li = get_lines (argv [1])
    for i in range (0, len (li)) :
        li [i] = modify (li [i], debug)

    file = argv [1]
    if "copy" in argv : file += ".2.idx"
    print ("writing file ", file)

    if len (argv) > 2 and "copy" not in argv : f = open (argv [1] + file, "w")
    else : f = open (file, "w")
    for l in li :
        f.write (l)
    f.close ()
    
    print ("end")
    
if __name__ == "__main__" :
    main (sys.argv)
    
