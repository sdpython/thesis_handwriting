# coding: cp1252
import upper_index as UI
import sys


def modify(line, noone=False):
    line = line.replace(r"{\bfseries\hfil Symbols\hfil}\nopagebreak", "")
    line = line.replace("Symbols", "Symboles")
    line = line.replace("\\item Z", "\\item Liens")
    line = line.replace(r"{\bfseries\hfil Z\hfil}\nopagebreak",
                        r"{\bfseries\hfil Liens\hfil}\nopagebreak")

    line = line.replace(r"  \subsubitem \relax \fontsize  {6}{7}\selectfont  {C:/",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {C:/")
    line = line.replace(r"  \subsubitem \relax \fontsize  {6}{7}\selectfont  {c:/",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {c:/")
    line = line.replace(r"  \subsubitem \relax \fontsize  {6}{7}\selectfont  {http://",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {http://")
    line = line.replace(r"  \subitem \relax \fontsize  {6}{7}\selectfont  {C:/",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {C:/")
    line = line.replace(r"  \subitem \relax \fontsize  {6}{7}\selectfont  {c:/",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {c:/")
    line = line.replace(r"  \subitem \relax \fontsize  {6}{7}\selectfont  {http://",
                        r"\item \relax \fontsize  {6}{7}\selectfont  {http://")

    line = line.replace("  \\subsubitem C:/", "  \\item C:/")
    line = line.replace("  \\subsubitem c:/", "  \\item c:/")
    line = line.replace("  \\subsubitem http://", "\\item http://")
    line = line.replace("  \\subitem C:/", "  \\item C:/")
    line = line.replace("  \\subitem c:/", "  \\item c:/")
    line = line.replace("  \\subitem http://", "\\item http://")

    line = line.replace("\\subitem lien", "")
    line = line.replace("\\item liens", "")

    line = line.replace(r"\item §", r"\item numéro")
    line = line.replace(r"http://www.xavierdupre.fr/hal\_python/hal\_python\_help\_html/sample",
                        r"http://www.xavierdupre.fr/hal\_python/hal\_python\_help\_html/ sample")

    line = line.replace(r"CodeWindows\#", r"CodeWindows\# ")
    line = line.replace(r"http://www.stack.nl/$\sim $dimitri/doxygen/",
                        r"http://www. stack. nl/ $\sim $dimitri/ doxygen/")
    line = line.replace(r"http:// www. boost. org/ doc/ libs/ 1\_36\_0/libs/python/doc/index.html",
                        r"http:// www. boost. org/ doc/ libs/ 1\_36\_0/ libs/ python/ doc/ index.html")
    line = line.replace(r"//www.pythonweb.org/projects/webmodules/doc/0.5.3",
                        r"//www.pythonweb.org/projects/webmodules/doc/0.5.3 ")

    line = line.replace(r"\item http://", r"\item \footnotesize http://")
    line = line.replace(r"\item C:/Python", r"\item \footnotesize C:/Python")

    return line


def main(argv):
    if len(argv) <= 1:
        #argv = ["upper_index",  r"D:\Dupre\_data\informatique\support\python_cours\chap1_introduction.ind", "2"]
        argv = ["upper_index", r"D:\Dupre\_data\informatique\support\python_collection\initiation_via_python_ellipse.ind", "2", "copy"]

    noone = len(argv) >= 3 and argv[2] == "no"

    for i in range(0, len(argv)):
        print("argument ", i, " : ", argv[i])

    print("reading file ", argv[1])
    li = UI.get_lines(argv[1])
    for i in range(0, len(li)):
        li[i] = modify(li[i], noone)

    file = argv[1]
    if "copy" in argv:
        file += ".2.ind"
    print("writing file ", file)

    if len(argv) > 2 and "copy" not in argv:
        f = open(argv[1] + file, "w")
    else:
        f = open(file, "w")
    for l in li:
        f.write(l)
    f.close()

    print("end")


if __name__ == "__main__":
    main(sys.argv)
