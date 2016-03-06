@echo 			\filextensionnum=2 \correctionenonce=1 > ../../common/compile.tex

del %1.log
del %1.aux
del %1.bbl
del %1.blg
del %1.idx
del %1.ilg
del %1.toc
del %1.ind
del %1.lot
del %1.out
del %1.lof
del image\*.eps
del argument.log
del argument.blg
del argument.aux
del argument.bbl

rem xelatex ?
pdflatex.exe --enable-write18 %1.tex
c:\python33\python ..\..\common\upper_index.py %1.idx
makeindex.exe -s ../../common/index.ist %1.idx 
c:\python33\python ..\..\common\index_ind.py %1.ind
pdflatex.exe --enable-write18 %1.tex %1.ind
c:\python33\python ..\..\common\upper_index.py %1.idx
makeindex.exe 		-s ../../common/index.ist 	%1.idx 
rem c:\python33\python ..\..\common\index_ind.py %1.ind
pdflatex.exe --enable-write18 %1.tex %1.ind

del %1.log
del %1.aux
del %1.bbl
del %1.blg
rem del %1.idx
del %1.ilg
del %1.toc
rem del %1.ind
del %1.lot
del %1.out
del %1.lof
del image\*.eps
del argument.log
del argument.blg
del argument.aux
del argument.bbl



