from subprocess import call
import convert, orgexport
import sys,os
def generate_from_csv(CSVname,ORGname,format='pdf'):
	dic=convert.csv2dict(CSVname)
	print dic
	return 0

def generate_from_par(dictPar,ORGname,format='pdf',dirname='./',dependencylist=[]):
	if not os.path.isfile(ORGname):
		print("generate_from_par Error: " + ORGname + " doesn't exist")
		sys.exit()
	if os.path.exists('./pyorgtex_tmp/'):
		call(['rm','-rf','./pyorgtex_tmp'])
	call(['mkdir','pyorgtex_tmp'])
	print('tmp directory created')
	if(len(dependencylist)!=0):
		for i in range(len(dependencylist)):
			call(['cp','-r',dependencylist[i],'./pyorgtex_tmp/'+convert.extractFilename(dependencylist[i])])
			print(dependencylist[i]+ 'copied')
	if not os.path.exists(dirname):
		newdir=dirname[2:-1]
		print('Create the directory: ' + newdir)
		call(['mkdir',newdir])
	call(['cp','-r',ORGname,'./pyorgtex_tmp/'+dictPar['stuid']+'.org'])
	convert.dict2json(dictPar,'./pyorgtex_tmp/'+dictPar['stuid']+'.json')
	if(format=='pdf'):
		orgexport.export2pdf('./pyorgtex_tmp/'+dictPar['stuid']+'.org')
	call(['cp','-r','./pyorgtex_tmp/'+dictPar['stuid']+'.pdf',dirname+dictPar['stuid']+'.pdf'])
	print(dictPar['stuid']+' Done!')
