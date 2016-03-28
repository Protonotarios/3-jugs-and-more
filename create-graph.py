#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Το πρόβλημα με τις τρεις καρδάρες
Γενικό γράφημα καταστάσεων
"""
#    Ιωάννης Πρωτονοτάριος <ioannis@protonotarios.eu>
#    Εργασία για το μάθημα Ευφυή συστήματα
#    21 Μαρτίου 2016
#    cc-by-sa

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

__author__ = """Ioannis Protonotarios (ioannis@protonotarios.eu)"""

# Εισαγωγή της βιβλιοθήκης pygraphviz
from pygraphviz import *


G=AGraph(strict=False,directed=True)
G.graph_attr['label']='καρδάρες'
G.graph_attr['ranksep']='.5' # Επιλέχθηκε αυτή η τιμή ως η βέλτιστη. 
                             #   Με μικρότερο ranksep πέφτουν το ένα πάνω στο άλλο.
                             #   Με μεγαλύτερο ranksep το διάγραμμα γίνεται τεράστιο.
G.node_attr['shape']='record'
G.node_attr['height']='.1'

# Δημιουργία όλων των δυνατών καταστάσεων (κόμβων)
for k3 in range(0,4):
        for k7 in range(0,8):
                for k10 in range(0,11):
                        if k3+k7+k10==10: #Συνθήκη για να υπάρχει η τρέχουσα κατάσταση
                                G.add_node(str(k3)+str(k7)+str(k10), color='grey', label="<3>"+str(k3)+"|<7>"+str(k7)+"|<10>"+str(k10))

# Δημιουργία όλων των ακμών
etiketa=''
xroma='black'
akmi='όχι'
for k3 in range(0,4):
        for k7 in range(0,8):
                for k10 in range(0,11):
                        if k3+k7+k10==10:
                                arxikoskombos=str(k3)+str(k7)+str(k10)
                                #Για κάθε αρχικό κόμβο δοκιμάζουμε τους 6 δυνατούς συνδυασμούς και σχεδιάζουμε όποιον από αυτούς υπάρχει
                                for i in range(1,7):
                                        
                                        neo3=k3
                                        neo7=k7
                                        neo10=k10
                                        if i==1:                                
                                                if k3>0 and k7<7:
                                                        # Στην αρχή κάθε ακμής γράφεται η περιγραφή του συνδυασμού, 
                                                        #   π.χ. «3>7» σημαίνει «άδειασμα της 3 στην 7».
                                                        etiketa='3>7'
                                                        akmi='ναι'
                                                        # Για κάθε ένας από τους συνδυασμούς χρησιμοποιούμε άλλο χρώμα
                                                        #   τόσο για το βελάκι όσο και για το κειμενάκι, για να ξεχωρίζουν.
                                                        xroma='blue'
                                                        neo10=k10
                                                        if k3<=7-k7:
                                                                neo3=0
                                                                neo7=k7+k3
                                                        else:
                                                                neo3=k3-(7-k7)
                                                                neo7=7
                                        if i==2:
                                                if k3>0 and k10<10:
                                                        etiketa='3>10'
                                                        akmi='ναι'
                                                        xroma='cyan'
                                                        neo7=k7
                                                        if k3<=10-k10:
                                                                neo3=0
                                                                neo10=k10+k3
                                                        else:
                                                                neo3=k3-(10-k10)
                                                                neo10=10
                                        if i==3:
                                                if k7>0 and k10<10:
                                                        etiketa='7>10'
                                                        akmi='ναι'
                                                        xroma='forestgreen'
                                                        neo3=k3
                                                        if k7<=10-k10:
                                                                neo7=0
                                                                neo10=k10+k7
                                                        else:
                                                                neo7=k7-(10-k10)
                                                                neo10=10
                                        if i==4:
                                                if k7>0 and k3<3:
                                                        etiketa='7>3'
                                                        akmi='ναι'
                                                        xroma='chartreuse3'
                                                        neo10=k10
                                                        if k7<=3-k3:
                                                                neo7=0
                                                                neo3=k3+k7
                                                        else:
                                                                neo7=k7-(3-k3)
                                                                neo3=3
                                        if i==5:
                                                if k10>0 and k3<3:
                                                        etiketa='10>3'
                                                        akmi='ναι'
                                                        xroma='orange'
                                                        neo7=k7
                                                        if k10<=3-k3:
                                                                neo10=0
                                                                neo3=k3+k10
                                                        else:
                                                                neo10=k10-(3-k3)
                                                                neo3=3
                                        if i==6:
                                                if k10>0 and k7<7:
                                                        etiketa='10>7'
                                                        akmi='ναι'
                                                        xroma='red'
                                                        neo3=k3
                                                        if k10<=7-k7:
                                                                neo10=0
                                                                neo7=k7+k10
                                                        else:
                                                                neo10=k10-(7-k7)
                                                                neo7=7
                                                
                                        if akmi=='ναι':
                                                telikoskombos=str(neo3)+str(neo7)+str(neo10)
                                                G.add_edge(arxikoskombos, telikoskombos, color=xroma, taillabel=etiketa, fontcolor=xroma, fontsize=8)
                                        akmi='όχι'



print(G) # Εκτύπωση του προγράμματος dot στην οθόνη
G.write("graph1.dot") # Εγγραφή του προγράμματος dot σε αρχείο 
print('Ο παραχθείς κώδικας dot αποθηκεύτηκε στο αρχείο graph1.dot')
G.draw('graph1.png',prog="dot") # Δημιουργία png με μέθοδο dot
print('Η παραχθείσα εικόνα αποθηκεύτηκε ως graph1.png')
