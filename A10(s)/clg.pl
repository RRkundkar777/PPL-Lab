/*Defining Teachers*/
teacher(vaibhav).   
teacher(sumit). 
teacher(shrida). 
teacher(ashwini). 
teacher(pravin).
teacher(jagruti). 
teacher(rohini). 
teacher(vibhavari). 
teacher(sandeep). 
teacher(jagannath). 
teacher(shalaka). 
teacher(kshipra). 
teacher(jatin). 
teacher(datta).

/*Definiing subjects+*/
issubject(ppl).
issubject(dld).
issubject(dsa).
issubject(odemc).
issubject(dsgt).
issubject(fcs).
issubject(dtl).
issubject(ic).
issubject(plevh).

/*Specialisations*/
specialist(vaibhav,ppl).
specialist(vaibhav,nlp).
specialist(sumit,ppl).
specialist(shrida,dsa).
specialist(ashwini,dsa).
specialist(pravin,dld).
specialist(jagruti,dld).
specialist(vibhavari,dsgt).
specialist(rohini,dsgt).
specialist(sandeep,fcs).
specialist(jagannath,dtl).
specialist(shalaka,plevh).
specialist(kshipra,plevh).
specialist(jatin,odemc).
specialist(datta,odemc).

/*haslab*/
haslab(dld).
haslab(ppl).
haslab(dsa).
haslab(dtl).

/*comfirm_lab*/
confirm_lab(A) :- issubject(A),haslab(A).

/*isdiv*/
isdiv(1).
isdiv(2).

/*div teachers*/
teaches_to(vaibhav,1).
teaches_to(sumit,2).
teaches_to(shrida,1).
teaches_to(ashwini,2).
teaches_to(pravin,1).
teaches_to(jagruti,2).
teaches_to(vibhavari,1).
teaches_to(rohini,2).
teaches_to(sandeep,1).
teaches_to(sandeep,2).
teaches_to(jagannath,1).
teaches_to(jagannath,2).
teaches_to(shalaka,1).
teaches_to(kshipra,2).
teaches_to(jatin,1).
teaches_to(datta,2).
teaches_to(swapnil,1).
teaches_to(divya,1).
teaches_to(divya,2).
teaches_to(pushparaj,2).

tdata(A,B,C) :- teacher(A),specialist(A,B),issubject(B),isdiv(C),teaches_to(A,C).

/*Takes_Lab*/
takes_lab(swapnil,ppl,1).
takes_lab(pushparaj,ppl,2).
takes_lab(divya,dtl,1).
takes_lab(divya,dtl,2).
takes_lab(pravin,dld,1).
takes_lab(jagruti,dld,2).
takes_lab(shrida,dsa,1).
takes_lab(ashwini,dsa,2).

ldata(A,B,C) :- takes_lab(A,B,C),confirm_lab(B).

/*batches*/
batch(s1).
batch(s2).
batch(s3).
batch(s4).
batch(s5).

/*Student*/
student(adesh).
student(arya).
student(bharat).
student(apurva).
student(mihir).
student(nikita).
student(omkar).
student(pratik).
student(rushikesh).
student(sagar).
student(tanmay).
student(tushar).
student(sarvadnya).

/*MIS*/

has_mis(adesh,asc).
has_mis(arya,amc).
has_mis(bharat,kbn).
has_mis(apurva,dav).
has_mis(mihir,mym).
has_mis(nikita,tns).
has_mis(onkar,koa).
has_mis(pratik,pdb).
has_mis(rushikesh,krr).
has_mis(sagar,psg).
has_mis(tanmay,pts).
has_mis(tushar,ptc).
has_mis(sarvadnya,psv).

/*div*/
divof(adesh,1).
divof(arya,1).

divof(bharat,1).
divof(apurva,1).

divof(mihir,1).
divof(nikita,1).

divof(omkar,1).
divof(pratik,1).

divof(rushikesh,1).
divof(sagar,1).

divof(tanmay,2).
divof(tushar,2).
divof(sarvadnya,2).

isin_div(A,B) :- student(A),divof(A,B), isdiv(B).

/*batch*/
batch_of(adesh,s1).
batch_of(arya,s1).

batch_of(bharat,s2).
batch_of(apurva,s2).

batch_of(mihir,s3).
batch_of(nikita,s3).

batch_of(omkar,s4).
batch_of(pratik,s4).

batch_of(rushikesh,s5).
batch_of(sagar,s5).

batch_of(tanmay,s5).
batch_of(tushar,s5).
batch_of(sarvadnya,s5).

isin_batch(A,B) :- student(A),batch_of(A,B),batch(B).

/*Enrolments*/
enrols(adesh,ppl).
enrols(adesh,dld).
enrols(adesh,dsa).
enrols(adesh,odemc).
enrols(adesh,dsgt).
enrols(adesh,fcs).
enrols(adesh,dtl).
enrols(adesh,ic).
enrols(adesh,plevh).

enrols(arya,ppl).
enrols(arya,dld).
enrols(arya,dsa).
enrols(arya,odemc).
enrols(arya,dsgt).
enrols(arya,fcs).
enrols(arya,plevh).

enrols(bharat,ppl).
enrols(bharat,dld).
enrols(bharat,dsgt).
enrols(bharat,dtl).

enrols(mihir,ppl).
enrols(mihir,dld).
enrols(mihir,dsa).
enrols(mihir,odemc).
enrols(mihir,dsgt).

enrols(nikita,ppl).
enrols(nikita,dld).
enrols(nikita,dsa).
enrols(nikita,odemc).
enrols(nikita,dsgt).
enrols(nikita,fcs).
enrols(nikita,dtl).
enrols(nikita,ic).

enrols(omkar,ppl).
enrols(omkar,dld).
enrols(omkar,dsa).
enrols(omkar,odemc).
enrols(omkar,dsgt).
enrols(omkar,fcs).
enrols(omkar,dtl).
enrols(omkar,ic).
enrols(omkar,plevh).


enrols(pratik,dld).
enrols(pratik,odemc).
enrols(pratik,dsgt).
enrols(pratik,fcs).
enrols(pratik,dtl).

enrols(sagar,ppl).
enrols(sagar,dld).
enrols(sagar,dsa).
enrols(sagar,odemc).
enrols(sagar,fcs).
enrols(sagar,plevh).

enrols(tanmay,ppl).
enrols(tanmay,dld).
enrols(tanmay,dsa).
enrols(tanmay,odemc).
enrols(tanmay,dsgt).
enrols(tanmay,fcs).
enrols(tanmay,dtl).
enrols(tanmay,ic).
enrols(tanmay,plevh).

enrols(tushar,ppl).
enrols(tushar,dld).
enrols(tushar,dsa).
enrols(tushar,odemc).
enrols(tushar,dsgt).
enrols(tushar,fcs).
enrols(tushar,dtl).
enrols(tushar,ic).
enrols(tushar,plevh).

enrols(sarvadnya,ppl).
enrols(sarvadnya,dld).
enrols(sarvadnya,odemc).
enrols(sarvadnya,dsgt).
enrols(sarvadnya,dtl).
enrols(sarvadnya,plevh).

enrolment(A,B) :- enrols(A,B),student(A),issubject(B).

sinfo(A,B,C,D) :- student(A),has_mis(A,B),isin_div(A,C),isin_batch(A,D).

mentor(A,B) :- teacher(A),student(B),specialist(A,C),enrolment(B,C),teaches_to(A,D),isin_div(B,D).