#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Το πρόβλημα με τις τρεις καρδάρες
Αναζήτηση σε βάθος
"""
#    Ιωάννης Πρωτονοτάριος <ioannis@protonotarios.eu>
#    Εργασία για το μάθημα Ευφυή συστήματα
#    21 Μαρτίου 2016
#    GNU license

k=[0,0,10]
katastaseis_poy_exoyme_e3etasei=[k]
seira_afethriwn=[2,1,0]
seira_proteraiothtas_proorismwn=[2,1,0]
bhma=0
bre8hke_katastash=0
bre8hke_lysh=0
synoliko_gala_poy_metaggisthke=0
print 'Βήμα 0: Αρχική κατάσταση',k

#for z in range(0,20):
while bre8hke_lysh==0:
	
	# Υπολογισμός σειράς προτεραιότητας αφετηριών
	if k[2]>0:
		megalyterh_dia8esimh_afethria=2
	elif k[1]>0:
		megalyterh_dia8esimh_afethria=1
	else:
		megalyterh_dia8esimh_afethria=0
	
	#print 'megalyterh_dia8esimh_afethria',megalyterh_dia8esimh_afethria #Εκτύπωση ελέγχου
		
	seira_afethriwn.remove(megalyterh_dia8esimh_afethria)
	#print 'seira_afethriwn',seira_afethriwn #Εκτύπωση ελέγχου
	
	pio_gemath=k.index(max(k))
	#print 'pio_gemath',pio_gemath #Εκτύπωση ελέγχου
	if megalyterh_dia8esimh_afethria==pio_gemath:
		seira_proteraiothtas_afethriwn=[megalyterh_dia8esimh_afethria]
		seira_proteraiothtas_afethriwn.extend(seira_afethriwn)
	else:
		seira_afethriwn.remove(pio_gemath)
		#print 'seira_afethriwn',seira_afethriwn #Εκτύπωση ελέγχου
		seira_proteraiothtas_afethriwn=[megalyterh_dia8esimh_afethria,pio_gemath]
		seira_proteraiothtas_afethriwn.extend(seira_afethriwn)
	#print 'seira_proteraiothtas_afethriwn',seira_proteraiothtas_afethriwn #Εκτύπωση ελέγχου
	#print 'seira_proteraiothtas_proorismwn',seira_proteraiothtas_proorismwn #Εκτύπωση ελέγχου
	seira_afethriwn=[2,1,0]
	
	# Εύρεση της κατάλληλης μετάγγισης
	for afethria in seira_proteraiothtas_afethriwn:
		for proorismos in seira_proteraiothtas_proorismwn:
			if afethria<>proorismos:
				#print 'afethria,proorismos',afethria,proorismos #Εκτύπωση ελέγχου
				
				if proorismos==2:
					keno=10-k[proorismos]
				elif proorismos==1:
					keno=7-k[proorismos]
				else:
					keno=3-k[proorismos]
				if keno>0:
					#print 'Afethria-keno',k[afethria],keno #Εκτύπωση ελέγχου
					poso_metagishs=min(k[afethria],keno)
					#print 'poso_metagishs',poso_metagishs #Εκτύπωση ελέγχου
					
					testk=k[:]
					testk[afethria]=testk[afethria]-poso_metagishs
					testk[proorismos]=testk[proorismos]+poso_metagishs
					#print 'K -- testk',k,testk #Εκτύπωση ελέγχου
					#print #Εκτύπωση ελέγχου
					
					if testk in katastaseis_poy_exoyme_e3etasei:
						#print 'yparxei'
						pass
					else:
						#print 'den yparxei' #Εκτύπωση ελέγχου
						bre8hke_katastash=bre8hke_katastash+1
						if bre8hke_katastash==1: #Για πλάτος θα το κάνουμε >0 και επίσης ...
							print 'Βρέθηκε νέα κατάσταση',bre8hke_katastash #Εκτύπωση ελέγχου
							k=testk[:]
							katastaseis_poy_exoyme_e3etasei.append(testk)
							bhma=bhma+1
							synoliko_gala_poy_metaggisthke=synoliko_gala_poy_metaggisthke+poso_metagishs
							#print bhma #Εκτύπωση ελέγχου
							#print 'katastaseis_poy_exoyme_e3etasei',katastaseis_poy_exoyme_e3etasei #Εκτύπωση ελέγχου
							#print '------' #Εκτύπωση ελέγχου
							#print 'Τα από δω και κάτω αγνοούνται' #Εκτύπωση ελέγχου
							#Σημείο ΑΑ
	bre8hke_katastash=0	
	
	#Για πλάτος αυτό το πακέτο πάει στο σημείο ΑΑ
	print		
	print 'Βήμα',bhma,': Τρέχουσα κατάσταση',k
	print 'Καταστάσεις που έχουμε εξετάσει',katastaseis_poy_exoyme_e3etasei
	if max(k)==5: 
	#Αυτό μας δίνει τη λύση [3,2,5] που κατ' εμέ είναι σωστή.
	#Εναλλακτικά, για τη λύση [0,5,5] αλλάζουμε το if ως εξής:
	#if k=[0,5,5]:
		bre8hke_lysh=1
		
print '--------------------'
print 'ΒΡΕΘΗΚΕ ΛΥΣΗ!'
print 'Είναι η κατάσταση:',k
print 'Συνολικά εξετάστηκαν οι καταστάσεις:',katastaseis_poy_exoyme_e3etasei
print 'Σύνολο βημάτων:',bhma
print 'Συνολικά μεταγγίστηκαν',synoliko_gala_poy_metaggisthke,'κιλά γάλα.'
