


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Width of Buttons
w = "30"

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Afghanistan Information Codes
def afgmap():

    afgwinmap = Toplevel(main_window)
    afgwinmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("afghanistan-map.jpg"))
    label = tk.Label(afgwinmap, image=image)
    label.pack(expand = "yes")
    afgwinmap.mainloop()

def afgpr():

    afgwinpr = Toplevel(main_window)
    afgwinpr.title("President")
    image = ImageTk.PhotoImage(Image.open("President-Ghani.png"))
    label = tk.Label(afgwinpr, image=image)
    label.pack(expand = "yes")
    afgwinpr.mainloop()

def afglang():

    afgwin = Toplevel(main_window)
    afgwin.title("Language")
    image = ImageTk.PhotoImage(Image.open("AfgLang.png"))
    label = tk.Label(afgwin, image=image)
    label.pack(expand = "yes")
    afgwin.mainloop()

def afgcountrycode():

    afgwin = Toplevel(main_window)
    afgwin.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("DailingCode.PNG"))
    label = tk.Label(afgwin, image=image)
    label.pack(expand = "yes")
    afgwin.mainloop()

def AfgCurrency():

    afgwin = Toplevel(main_window)
    afgwin.title("Currency")
    image = ImageTk.PhotoImage(Image.open("AfgCurrency.PNG"))
    label = tk.Label(afgwin, image=image)
    label.pack(expand = "yes")
    afgwin.mainloop()

def afganthem():
	os.system("afganthem.mp3")

def afginfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)








    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)

    play = PhotoImage(file = r"play.png")
    play = play.subsample(2, 2)



  
    
    



    Map = tk.Button(win, image= mapb, width = w, command=afgmap)
    Map.place(relx=0.028, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = afgpr)
    pr.place(relx=0.028, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = afglang)
    officialLang.place(relx=0.028, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= afgcountrycode)
    country_code.place(relx=0.028, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= curb, width = w, command = AfgCurrency)
    country_code.place(relx=0.028, rely=0.30, relheight = 0.06, relwidth = 0.95)

    pr = tk.Button(win, image= play,relief="flat", width = w, bg="black", command=afganthem)
    pr.place(relx=0.005, rely=0.93, relheight = 0.06, relwidth = 0.95)



    
    
    
    win.mainloop()

#End of Afghanistan Information Code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Azerbaijan Information Codes

def azmap():

    azmap = Toplevel(main_window)
    azmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("azerbaijan-map.png"))
    label = tk.Label(azmap, image=image)
    label.pack(expand = "yes")
    azmap.mainloop()

def azpr():

    azpr = Toplevel(main_window)
    azpr.title("President")
    image = ImageTk.PhotoImage(Image.open("azerpresident.png"))
    label = tk.Label(azpr, image=image)
    label.pack(expand = "yes")
    azpr.mainloop()

def azglang():

    azglang = Toplevel(main_window)
    azglang.title("Language")
    image = ImageTk.PhotoImage(Image.open("azlang.PNG"))
    label = tk.Label(azglang, image=image)
    label.pack(expand = "yes")
    azglang.mainloop()

def azgcountrycode():

    azgcountrycode = Toplevel(main_window)
    azgcountrycode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("azcode.PNG"))
    label = tk.Label(azgcountrycode, image=image)
    label.pack(expand = "yes")
    azgcountrycode.mainloop()

def AzCurrency():

    AzCurrency = Toplevel(main_window)
    AzCurrency.title("Currency")
    image = ImageTk.PhotoImage(Image.open("azcur.PNG"))
    label = tk.Label(AzCurrency, image=image)
    label.pack(expand = "yes")
    AzCurrency.mainloop()


def azinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)

    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=azmap)
    Map.place(relx=0.028, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = azpr)
    pr.place(relx=0.028, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = azglang)
    officialLang.place(relx=0.028, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= azgcountrycode)
    country_code.place(relx=0.028, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= curb, width = w, command = AzCurrency)
    country_code.place(relx=0.028, rely=0.30, relheight = 0.06, relwidth = 0.95)
    

    
    
    win.mainloop()
#End of Azerbaijan Information Code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Bangladesh Information Codes

def bgmap():

    bgmap = Toplevel(main_window)
    bgmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("bgmap.png"))
    label = tk.Label(bgmap, image=image)
    label.pack(expand = "yes")
    bgmap.mainloop()

def bgpr():

    bgpr = Toplevel(main_window)
    bgpr.title("President")
    image = ImageTk.PhotoImage(Image.open("bgpr.png"))
    label = tk.Label(bgpr, image=image)
    label.pack(expand = "yes")
    bgpr.mainloop()

def bglang():

    bglang = Toplevel(main_window)
    bglang.title("Language")
    image = ImageTk.PhotoImage(Image.open("bglang.png"))
    label = tk.Label(bglang, image=image)
    label.pack(expand = "yes")
    bglang.mainloop()

def bgccode():

    bgccode = Toplevel(main_window)
    bgccode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("bgcode.png"))
    label = tk.Label(bgccode, image=image)
    label.pack(expand = "yes")
    bgccode.mainloop()

def bgcurrency():

    bgcurrency = Toplevel(main_window)
    bgcurrency.title("Currency")
    image = ImageTk.PhotoImage(Image.open("bgcurr.png"))
    label = tk.Label(bgcurrency, image=image)
    label.pack(expand = "yes")
    bgcurrency.mainloop()


def bginfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)

    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=bgmap)
    Map.place(relx=0.028, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = bgpr)
    pr.place(relx=0.028, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = bhlang)
    officialLang.place(relx=0.028, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= bgccode)
    country_code.place(relx=0.028, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = bgcurrency)
    Currency.place(relx=0.028, rely=0.30, relheight = 0.06, relwidth = 0.95)





    
    
    
    win.mainloop()
#End of Bangladesh Information Code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Bahrain Information Codes

def bhmap():

    bhmap = Toplevel(main_window)
    bhmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("bhmap.png"))
    label = tk.Label(bhmap, image=image)
    label.pack(expand = "yes")
    bhmap.mainloop()

def bhpr():

    bhpr = Toplevel(main_window)
    bhpr.title("President")
    image = ImageTk.PhotoImage(Image.open("bhpr.png"))
    label = tk.Label(bhpr, image=image)
    label.pack(expand = "yes")
    bhpr.mainloop()

def bhlang():

    bhlang = Toplevel(main_window)
    bhlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("bhlang.png"))
    label = tk.Label(bhlang, image=image)
    label.pack(expand = "yes")
    bhlang.mainloop()

def bhccode():

    bhccode = Toplevel(main_window)
    bhccode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("bhccode.png"))
    label = tk.Label(bhccode, image=image)
    label.pack(expand = "yes")
    bhccode.mainloop()

def bhcurr():

    bhcurr = Toplevel(main_window)
    bhcurr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("bhcurr.png"))
    label = tk.Label(bhcurr, image=image)
    label.pack(expand = "yes")
    bhcurr.mainloop()


def bhinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)

    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=bhmap)
    Map.place(relx=0.028, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = bhpr)
    pr.place(relx=0.028, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = bhlang)
    officialLang.place(relx=0.028, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= bhccode)
    country_code.place(relx=0.028, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = bhcurr)
    Currency.place(relx=0.028, rely=0.30, relheight = 0.06, relwidth = 0.95)











    
    
    
    win.mainloop()
#End of Bahrain Information Code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#China Information Codes

def chmap():

    chmap = Toplevel(main_window)
    chmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("chmap.png"))
    label = tk.Label(chmap, image=image)
    label.pack(expand = "yes")
    chmap.mainloop()

def chpr():

    chpr = Toplevel(main_window)
    chpr.title("President")
    image = ImageTk.PhotoImage(Image.open("chpr.png"))
    label = tk.Label(chpr, image=image)
    label.pack(expand = "yes")
    chpr.mainloop()

def chlang():

    chlang = Toplevel(main_window)
    chlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("chlang.png"))
    label = tk.Label(chlang, image=image)
    label.pack(expand = "yes")
    chlang.mainloop()

def chccode():

    chccode = Toplevel(main_window)
    chccode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("chccode.png"))
    label = tk.Label(chccode, image=image)
    label.pack(expand = "yes")
    chccode.mainloop()

def chcurr():

    chcurr = Toplevel(main_window)
    chcurr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("chcurr.png"))
    label = tk.Label(chcurr, image=image)
    label.pack(expand = "yes")
    chcurr.mainloop()


def chinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)

    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=chmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = chpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = chlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= chccode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = chcurr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of China information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Cyprus Information Codes

def cypmap():

    cypmap = Toplevel(main_window)
    cypmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("cypmap.png"))
    label = tk.Label(cypmap, image=image)
    label.pack(expand = "yes")
    cypmap.mainloop()

def cypr():

    cypr = Toplevel(main_window)
    cypr.title("President")
    image = ImageTk.PhotoImage(Image.open("cypr.png"))
    label = tk.Label(cypr, image=image)
    label.pack(expand = "yes")
    cypr.mainloop()

def cyplang():

    cyplang = Toplevel(main_window)
    cyplang.title("Language")
    image = ImageTk.PhotoImage(Image.open("cyplang.png"))
    label = tk.Label(cyplang, image=image)
    label.pack(expand = "yes")
    cyplang.mainloop()

def cypcode():

    cypcode = Toplevel(main_window)
    cypcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("cypcode.png"))
    label = tk.Label(cypcode, image=image)
    label.pack(expand = "yes")
    cypcode.mainloop()

def cypcur():

    cypcur = Toplevel(main_window)
    cypcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("cypcur.png"))
    label = tk.Label(cypcur, image=image)
    label.pack(expand = "yes")
    cypcur.mainloop()


def cypinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=cypmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = cypr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = cyplang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= cypcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = cypcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Cyprus information code







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#India Information Codes

def indmap():

    indmap = Toplevel(main_window)
    indmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("indmap.png"))
    label = tk.Label(indmap, image=image)
    label.pack(expand = "yes")
    indmap.mainloop()

def indpr():

    indpr = Toplevel(main_window)
    indpr.title("President")
    image = ImageTk.PhotoImage(Image.open("indpr.png"))
    label = tk.Label(indpr, image=image)
    label.pack(expand = "yes")
    indpr.mainloop()

def indlang():

    indlang = Toplevel(main_window)
    indlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("indlang.png"))
    label = tk.Label(indlang, image=image)
    label.pack(expand = "yes")
    indlang.mainloop()

def indcode():

    indcode = Toplevel(main_window)
    indcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("indcode.png"))
    label = tk.Label(indcode, image=image)
    label.pack(expand = "yes")
    indcode.mainloop()

def indcur():

    indcur = Toplevel(main_window)
    indcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("indcur.png"))
    label = tk.Label(indcur, image=image)
    label.pack(expand = "yes")
    indcur.mainloop()


def indinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=indmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = indpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = indlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= indcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = indcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of India information code







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Indonesia Information Codes

def indomap():

    indomap = Toplevel(main_window)
    indomap.title("Map")
    image = ImageTk.PhotoImage(Image.open("indomap.png"))
    label = tk.Label(indomap, image=image)
    label.pack(expand = "yes")
    indomap.mainloop()

def indopr():

    indopr = Toplevel(main_window)
    indopr.title("President")
    image = ImageTk.PhotoImage(Image.open("indopr.png"))
    label = tk.Label(indopr, image=image)
    label.pack(expand = "yes")
    indopr.mainloop()

def indolang():

    indolang = Toplevel(main_window)
    indolang.title("Language")
    image = ImageTk.PhotoImage(Image.open("indolang.png"))
    label = tk.Label(indolang, image=image)
    label.pack(expand = "yes")
    indolang.mainloop()

def indocode():

    indocode = Toplevel(main_window)
    indocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("indocode.png"))
    label = tk.Label(indocode, image=image)
    label.pack(expand = "yes")
    indocode.mainloop()

def indocur():

    indocur = Toplevel(main_window)
    indocur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("indocur.png"))
    label = tk.Label(indocur, image=image)
    label.pack(expand = "yes")
    indocur.mainloop()


def indoinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=indomap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = indopr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = indolang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= indocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = indocur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Indonesia information code







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Iran Information Codes

def irmap():

    irmap = Toplevel(main_window)
    irmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("irmap.png"))
    label = tk.Label(irmap, image=image)
    label.pack(expand = "yes")
    irmap.mainloop()

def irpr():

    irpr = Toplevel(main_window)
    irpr.title("President")
    image = ImageTk.PhotoImage(Image.open("irpr.png"))
    label = tk.Label(irpr, image=image)
    label.pack(expand = "yes")
    irpr.mainloop()

def irlang():

    irlang = Toplevel(main_window)
    irlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("irlang.png"))
    label = tk.Label(irlang, image=image)
    label.pack(expand = "yes")
    irlang.mainloop()

def ircode():

    ircode = Toplevel(main_window)
    ircode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("ircode.png"))
    label = tk.Label(ircode, image=image)
    label.pack(expand = "yes")
    ircode.mainloop()

def ircur():

    ircur = Toplevel(main_window)
    ircur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("ircur.png"))
    label = tk.Label(ircur, image=image)
    label.pack(expand = "yes")
    ircur.mainloop()


def irinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=irmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = irpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command =irlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= ircode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = ircur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Iran  information







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________






#Iraq Information Codes

def iqmap():

    iqmap = Toplevel(main_window)
    iqmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("iqmap.png"))
    label = tk.Label(iqmap, image=image)
    label.pack(expand = "yes")
    iqmap.mainloop()

def iqpr():

    iqpr = Toplevel(main_window)
    iqpr.title("President")
    image = ImageTk.PhotoImage(Image.open("iqpr.png"))
    label = tk.Label(iqpr, image=image)
    label.pack(expand = "yes")
    iqpr.mainloop()

def iqlang():

    iqlang = Toplevel(main_window)
    iqlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("iqlang.png"))
    label = tk.Label(iqlang, image=image)
    label.pack(expand = "yes")
    iqlang.mainloop()

def iqcode():

    iqcode = Toplevel(main_window)
    iqcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("iqcode.png"))
    label = tk.Label(iqcode, image=image)
    label.pack(expand = "yes")
    iqcode.mainloop()

def iqcur():

    iqcur = Toplevel(main_window)
    iqcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("iqcur.png"))
    label = tk.Label(iqcur, image=image)
    label.pack(expand = "yes")
    iqcur.mainloop()


def iqinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=iqmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = iqpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = iqlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= iqcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = iqcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Iraq information code







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Israel Information Codes

def ismap():

    ismap = Toplevel(main_window)
    ismap.title("Map")
    image = ImageTk.PhotoImage(Image.open("ismap.png"))
    label = tk.Label(ismap, image=image)
    label.pack(expand = "yes")
    ismap.mainloop()

def ispr():

    ispr = Toplevel(main_window)
    ispr.title("President")
    image = ImageTk.PhotoImage(Image.open("ispr.png"))
    label = tk.Label(ispr, image=image)
    label.pack(expand = "yes")
    ispr.mainloop()

def islang():

    islang = Toplevel(main_window)
    islang.title("Language")
    image = ImageTk.PhotoImage(Image.open("islang.png"))
    label = tk.Label(islang, image=image)
    label.pack(expand = "yes")
    islang.mainloop()

def iscode():

    iscode = Toplevel(main_window)
    iscode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("iscode.png"))
    label = tk.Label(iscode, image=image)
    label.pack(expand = "yes")
    iscode.mainloop()

def iscur():

    iscur = Toplevel(main_window)
    iscur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("iscur.png"))
    label = tk.Label(iscur, image=image)
    label.pack(expand = "yes")
    iscur.mainloop()


def isinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=ismap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = ispr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = islang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= iscode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = iscur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Israel information code







#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Japan Information Codes

def jmap():

    jmap = Toplevel(main_window)
    jmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("jmap.png"))
    label = tk.Label(jmap, image=image)
    label.pack(expand = "yes")
    jmap.mainloop()

def jpr():

    jpr = Toplevel(main_window)
    jpr.title("President")
    image = ImageTk.PhotoImage(Image.open("jpr.png"))
    label = tk.Label(jpr, image=image)
    label.pack(expand = "yes")
    jpr.mainloop()

def jlang():

    jlang = Toplevel(main_window)
    jlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("jlang.png"))
    label = tk.Label(jlang, image=image)
    label.pack(expand = "yes")
    jlang.mainloop()

def jcode():

    jcode = Toplevel(main_window)
    jcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("jcode.png"))
    label = tk.Label(jcode, image=image)
    label.pack(expand = "yes")
    jcode.mainloop()

def jcur():

    jcur = Toplevel(main_window)
    jcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("jcur.png"))
    label = tk.Label(jcur, image=image)
    label.pack(expand = "yes")
    jcur.mainloop()


def jinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=jmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = jpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = jlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= jcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = jcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Japan information code








#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Kazakhstan Information Codes

def kzmap():

    kzmap = Toplevel(main_window)
    kzmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("kzmap.png"))
    label = tk.Label(kzmap, image=image)
    label.pack(expand = "yes")
    kzmap.mainloop()

def kzpr():

    kzpr = Toplevel(main_window)
    kzpr.title("President")
    image = ImageTk.PhotoImage(Image.open("kzpr.png"))
    label = tk.Label(kzpr, image=image)
    label.pack(expand = "yes")
    kzpr.mainloop()

def kzlang():

    kzlang = Toplevel(main_window)
    kzlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("kzlang.png"))
    label = tk.Label(kzlang, image=image)
    label.pack(expand = "yes")
    kzlang.mainloop()

def kzcode():

    kzcode = Toplevel(main_window)
    kzcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("kzcode.png"))
    label = tk.Label(kzcode, image=image)
    label.pack(expand = "yes")
    kzcode.mainloop()

def kzcur():

    kzcur = Toplevel(main_window)
    kzcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("kzcur.png"))
    label = tk.Label(kzcur, image=image)
    label.pack(expand = "yes")
    kzcur.mainloop()


def kzinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=kzmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = kzpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = kzlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= kzcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = kzcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Kazakhstan information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Kuwait Information Codes

def kumap():

    kumap = Toplevel(main_window)
    kumap.title("Map")
    image = ImageTk.PhotoImage(Image.open("kumap.png"))
    label = tk.Label(kumap, image=image)
    label.pack(expand = "yes")
    kumap.mainloop()

def kupr():

    kupr = Toplevel(main_window)
    kupr.title("President")
    image = ImageTk.PhotoImage(Image.open("kupr.png"))
    label = tk.Label(kupr, image=image)
    label.pack(expand = "yes")
    kupr.mainloop()

def kulang():

    kulang = Toplevel(main_window)
    kulang.title("Language")
    image = ImageTk.PhotoImage(Image.open("kulang.png"))
    label = tk.Label(kulang, image=image)
    label.pack(expand = "yes")
    kulang.mainloop()

def kucode():

    kucode = Toplevel(main_window)
    kucode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("kucode.png"))
    label = tk.Label(kucode, image=image)
    label.pack(expand = "yes")
    kucode.mainloop()

def kucur():

    kucur = Toplevel(main_window)
    kucur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("kucur.png"))
    label = tk.Label(kucur, image=image)
    label.pack(expand = "yes")
    kucur.mainloop()


def kuinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=kumap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = kupr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = kulang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= kucode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = kucur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Kuwait information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Kyrgyzstan Information Codes

def kymap():

    kymap = Toplevel(main_window)
    kymap.title("Map")
    image = ImageTk.PhotoImage(Image.open("kymap.png"))
    label = tk.Label(kymap, image=image)
    label.pack(expand = "yes")
    kymap.mainloop()

def kypr():

    kypr = Toplevel(main_window)
    kypr.title("President")
    image = ImageTk.PhotoImage(Image.open("kypr.png"))
    label = tk.Label(kypr, image=image)
    label.pack(expand = "yes")
    kypr.mainloop()

def kylang():

    kylang = Toplevel(main_window)
    kylang.title("Language")
    image = ImageTk.PhotoImage(Image.open("kylang.png"))
    label = tk.Label(kylang, image=image)
    label.pack(expand = "yes")
    kylang.mainloop()

def kycode():

    kycode = Toplevel(main_window)
    kycode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("kycode.png"))
    label = tk.Label(kycode, image=image)
    label.pack(expand = "yes")
    kycode.mainloop()

def kycur():

    kycur = Toplevel(main_window)
    kycur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("kycur.png"))
    label = tk.Label(kycur, image=image)
    label.pack(expand = "yes")
    kycur.mainloop()


def kyinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=kymap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = kypr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = kylang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= kycode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = kycur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Kyrgyzstan information code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Lebanon Information Codes

def lmap():

    lmap = Toplevel(main_window)
    lmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("lmap.png"))
    label = tk.Label(lmap, image=image)
    label.pack(expand = "yes")
    lmap.mainloop()

def lpr():

    lpr = Toplevel(main_window)
    lpr.title("President")
    image = ImageTk.PhotoImage(Image.open("lpr.png"))
    label = tk.Label(lpr, image=image)
    label.pack(expand = "yes")
    lpr.mainloop()

def llang():

    llang = Toplevel(main_window)
    llang.title("Language")
    image = ImageTk.PhotoImage(Image.open("llang.png"))
    label = tk.Label(llang, image=image)
    label.pack(expand = "yes")
    llang.mainloop()

def lcode():

    lcode = Toplevel(main_window)
    lcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("lcode.png"))
    label = tk.Label(lcode, image=image)
    label.pack(expand = "yes")
    lcode.mainloop()

def lcur():

    lcur = Toplevel(main_window)
    lcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("lcur.png"))
    label = tk.Label(lcur, image=image)
    label.pack(expand = "yes")
    lcur.mainloop()


def linfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=lmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = lpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = llang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= lcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = lcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Lebanon information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Malaysia Information Codes

def mlmap():

    mlmap = Toplevel(main_window)
    mlmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("mlmap.png"))
    label = tk.Label(mlmap, image=image)
    label.pack(expand = "yes")
    mlmap.mainloop()

def mlpr():

    mlpr = Toplevel(main_window)
    mlpr.title("President")
    image = ImageTk.PhotoImage(Image.open("mlpr.png"))
    label = tk.Label(mlpr, image=image)
    label.pack(expand = "yes")
    mlpr.mainloop()

def mllang():

    mllang = Toplevel(main_window)
    mllang.title("Language")
    image = ImageTk.PhotoImage(Image.open("mllang.png"))
    label = tk.Label(mllang, image=image)
    label.pack(expand = "yes")
    mllang.mainloop()

def mlcode():

    mlcode = Toplevel(main_window)
    mlcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("mlcode.png"))
    label = tk.Label(mlcode, image=image)
    label.pack(expand = "yes")
    mlcode.mainloop()

def mlcur():

    mlcur = Toplevel(main_window)
    mlcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("mlcur.png"))
    label = tk.Label(mlcur, image=image)
    label.pack(expand = "yes")
    mlcur.mainloop()


def mlinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=mlmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = mlpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = mllang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= mlcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = mlcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Malaysia information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Maldives Information Codes

def mdmap():

    mdmap = Toplevel(main_window)
    mdmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("mdmap.png"))
    label = tk.Label(mdmap, image=image)
    label.pack(expand = "yes")
    mdmap.mainloop()

def mdpr():

    mdpr = Toplevel(main_window)
    mdpr.title("President")
    image = ImageTk.PhotoImage(Image.open("mdpr.png"))
    label = tk.Label(mdpr, image=image)
    label.pack(expand = "yes")
    mdpr.mainloop()

def mdlang():

    mdlang = Toplevel(main_window)
    mdlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("mdlang.png"))
    label = tk.Label(mdlang, image=image)
    label.pack(expand = "yes")
    mdlang.mainloop()

def mdcode():

    mdcode = Toplevel(main_window)
    mdcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("mdcode.png"))
    label = tk.Label(mdcode, image=image)
    label.pack(expand = "yes")
    mdcode.mainloop()

def mdcur():

    mdcur = Toplevel(main_window)
    mdcur.title("Currency")
    image = ImageTk.PhotoImage(Image.open("mdcur.png"))
    label = tk.Label(mdcur, image=image)
    label.pack(expand = "yes")
    mdcur.mainloop()


def mdinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=mdmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = mdpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = mdlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= mdcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = mdcur)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Maldives information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Myanmar Information Codes

def mymap():

    mymap = Toplevel(main_window)
    mymap.title("Map")
    image = ImageTk.PhotoImage(Image.open("mymap.png"))
    label = tk.Label(mymap, image=image)
    label.pack(expand = "yes")
    mymap.mainloop()

def mypr():

    mypr = Toplevel(main_window)
    mypr.title("President")
    image = ImageTk.PhotoImage(Image.open("mypr.png"))
    label = tk.Label(mypr, image=image)
    label.pack(expand = "yes")
    mypr.mainloop()

def mylang():

    mylang = Toplevel(main_window)
    mylang.title("Language")
    image = ImageTk.PhotoImage(Image.open("mylang.png"))
    label = tk.Label(mylang, image=image)
    label.pack(expand = "yes")
    mylang.mainloop()

def mycode():

    mycode = Toplevel(main_window)
    mycode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("mycode.png"))
    label = tk.Label(mycode, image=image)
    label.pack(expand = "yes")
    mycode.mainloop()

def mycr():

    mycr = Toplevel(main_window)
    mycr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("mycr.png"))
    label = tk.Label(mycr, image=image)
    label.pack(expand = "yes")
    mycr.mainloop()


def myinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=mymap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = mypr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = mylang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= mycode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = mycr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Myanmar  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Nepal Information Codes

def nmap():

    nmap = Toplevel(main_window)
    nmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("nmap.png"))
    label = tk.Label(nmap, image=image)
    label.pack(expand = "yes")
    nmap.mainloop()

def npr():

    npr = Toplevel(main_window)
    npr.title("President")
    image = ImageTk.PhotoImage(Image.open("npr.png"))
    label = tk.Label(npr, image=image)
    label.pack(expand = "yes")
    npr.mainloop()

def nlang():

    nlang = Toplevel(main_window)
    nlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("nlang.png"))
    label = tk.Label(nlang, image=image)
    label.pack(expand = "yes")
    nlang.mainloop()

def ncode():

    ncode = Toplevel(main_window)
    ncode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("ncode.png"))
    label = tk.Label(ncode, image=image)
    label.pack(expand = "yes")
    ncode.mainloop()

def ncr():

    ncr = Toplevel(main_window)
    ncr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("ncr.png"))
    label = tk.Label(ncr, image=image)
    label.pack(expand = "yes")
    ncr.mainloop()


def ninfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=nmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = npr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = nlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= ncode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = ncr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Nepal  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#North Korea Information Codes

def nkmap():

    nkmap = Toplevel(main_window)
    nkmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("nkmap.png"))
    label = tk.Label(nkmap, image=image)
    label.pack(expand = "yes")
    nkmap.mainloop()

def nkpr():

    nkpr = Toplevel(main_window)
    nkpr.title("President")
    image = ImageTk.PhotoImage(Image.open("nkpr.png"))
    label = tk.Label(nkpr, image=image)
    label.pack(expand = "yes")
    nkpr.mainloop()

def nklang():

    nklang = Toplevel(main_window)
    nklang.title("Language")
    image = ImageTk.PhotoImage(Image.open("nklang.png"))
    label = tk.Label(nklang, image=image)
    label.pack(expand = "yes")
    nklang.mainloop()

def nkcode():

    nkcode = Toplevel(main_window)
    nkcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("nkcode.png"))
    label = tk.Label(nkcode, image=image)
    label.pack(expand = "yes")
    nkcode.mainloop()

def nkcr():

    nkcr = Toplevel(main_window)
    nkcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("nkcr.png"))
    label = tk.Label(nkcr, image=image)
    label.pack(expand = "yes")
    nkcr.mainloop()


def nkinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=nkmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = nkpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = nklang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= nkcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = nkcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of North Korea  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Oman Information Codes

def omap():

    omap = Toplevel(main_window)
    omap.title("Map")
    image = ImageTk.PhotoImage(Image.open("omap.png"))
    label = tk.Label(omap, image=image)
    label.pack(expand = "yes")
    omap.mainloop()

def opr():

    opr = Toplevel(main_window)
    opr.title("President")
    image = ImageTk.PhotoImage(Image.open("opr.png"))
    label = tk.Label(opr, image=image)
    label.pack(expand = "yes")
    opr.mainloop()

def olang():

    olang = Toplevel(main_window)
    olang.title("Language")
    image = ImageTk.PhotoImage(Image.open("olang.png"))
    label = tk.Label(olang, image=image)
    label.pack(expand = "yes")
    olang.mainloop()

def ocode():

    ocode = Toplevel(main_window)
    ocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("ocode.png"))
    label = tk.Label(ocode, image=image)
    label.pack(expand = "yes")
    ocode.mainloop()

def ocr():

    ocr = Toplevel(main_window)
    ocr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("ocr.png"))
    label = tk.Label(ocr, image=image)
    label.pack(expand = "yes")
    ocr.mainloop()


def oinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=omap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = opr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = olang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= ocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = ocr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Oman  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Philippines Information Codes

def phmap():

    phmap = Toplevel(main_window)
    phmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("phmap.png"))
    label = tk.Label(phmap, image=image)
    label.pack(expand = "yes")
    phmap.mainloop()

def phpr():

    phpr = Toplevel(main_window)
    phpr.title("President")
    image = ImageTk.PhotoImage(Image.open("phpr.png"))
    label = tk.Label(phpr, image=image)
    label.pack(expand = "yes")
    phpr.mainloop()

def phlang():

    phlang = Toplevel(main_window)
    phlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("phlang.png"))
    label = tk.Label(phlang, image=image)
    label.pack(expand = "yes")
    phlang.mainloop()

def phcode():

    phcode = Toplevel(main_window)
    phcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("phcode.png"))
    label = tk.Label(phcode, image=image)
    label.pack(expand = "yes")
    phcode.mainloop()

def phcr():

    phcr = Toplevel(main_window)
    phcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("phcr.png"))
    label = tk.Label(phcr, image=image)
    label.pack(expand = "yes")
    phcr.mainloop()


def phinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=phmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = phpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = phlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= phcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = phcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Philippines  information code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Pakistan Information Codes

def pkmap():

    pkmap = Toplevel(main_window)
    pkmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("pkmap.png"))
    label = tk.Label(pkmap, image=image)
    label.pack(expand = "yes")
    pkmap.mainloop()

def pkpr():

    pkpr = Toplevel(main_window)
    pkpr.title("President")
    image = ImageTk.PhotoImage(Image.open("pkpr.png"))
    label = tk.Label(pkpr, image=image)
    label.pack(expand = "yes")
    pkpr.mainloop()

def pkpm():

    pkpm = Toplevel(main_window)
    pkpm.title("President")
    image = ImageTk.PhotoImage(Image.open("pkpm.png"))
    label = tk.Label(pkpm, image=image)
    label.pack(expand = "yes")
    pkpm.mainloop()



def pklang():

    pklang = Toplevel(main_window)
    pklang.title("Language")
    image = ImageTk.PhotoImage(Image.open("pklang.png"))
    label = tk.Label(pklang, image=image)
    label.pack(expand = "yes")
    pklang.mainloop()

def pkcode():

    pkcode = Toplevel(main_window)
    pkcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("pkcode.png"))
    label = tk.Label(pkcode, image=image)
    label.pack(expand = "yes")
    pkcode.mainloop()

def pkcr():

    pkcr = Toplevel(main_window)
    pkcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("pkcr.png"))
    label = tk.Label(pkcr, image=image)
    label.pack(expand = "yes")
    pkcr.mainloop()

def pakanthem():
	os.system("pakanthem.mp3")


def pkinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    pm = PhotoImage(file = r"pm.png")
    pm = pm.subsample(2, 2)


    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)
    

    play = PhotoImage(file = r"play.png")
    play = play.subsample(2, 2)



    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=pkmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = pkpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)

    pr = tk.Button(win, image= pm, width = w, command = pkpm)
    pr.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = pklang)
    officialLang.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= pkcode)
    country_code.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = pkcr)
    Currency.place(relx=0.030, rely=0.37, relheight = 0.06, relwidth = 0.95)

    pr = tk.Button(win, image= play,relief="flat", width = w, bg="black", command=pakanthem)
    pr.place(relx=0.005, rely=0.93, relheight = 0.06, relwidth = 0.95)




    
    
    
    win.mainloop()


#End of Pakistan  information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Palestine Information Codes

def plmap():

    plmap = Toplevel(main_window)
    plmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("plmap.png"))
    label = tk.Label(plmap, image=image)
    label.pack(expand = "yes")
    plmap.mainloop()

def plpr():

    plpr = Toplevel(main_window)
    plpr.title("President")
    image = ImageTk.PhotoImage(Image.open("plpr.png"))
    label = tk.Label(plpr, image=image)
    label.pack(expand = "yes")
    plpr.mainloop()

def pllang():

    pllang = Toplevel(main_window)
    pllang.title("Language")
    image = ImageTk.PhotoImage(Image.open("pllang.png"))
    label = tk.Label(pllang, image=image)
    label.pack(expand = "yes")
    pllang.mainloop()

def plcode():

    plcode = Toplevel(main_window)
    plcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("plcode.png"))
    label = tk.Label(plcode, image=image)
    label.pack(expand = "yes")
    plcode.mainloop()

def plcr():

    plcr = Toplevel(main_window)
    plcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("plcr.png"))
    label = tk.Label(plcr, image=image)
    label.pack(expand = "yes")
    plcr.mainloop()


def plinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=plmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = plpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = pllang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= plcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = plcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Palestine  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Qatar Information Codes

def qmap():

    qmap = Toplevel(main_window)
    qmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("qmap.png"))
    label = tk.Label(qmap, image=image)
    label.pack(expand = "yes")
    qmap.mainloop()

def qpr():

    qpr = Toplevel(main_window)
    qpr.title("President")
    image = ImageTk.PhotoImage(Image.open("qpr.png"))
    label = tk.Label(qpr, image=image)
    label.pack(expand = "yes")
    qpr.mainloop()

def qlang():

    qlang = Toplevel(main_window)
    qlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("qlang.png"))
    label = tk.Label(qlang, image=image)
    label.pack(expand = "yes")
    qlang.mainloop()

def qcode():

    qcode = Toplevel(main_window)
    qcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("qcode.png"))
    label = tk.Label(qcode, image=image)
    label.pack(expand = "yes")
    qcode.mainloop()

def qcr():

    qcr = Toplevel(main_window)
    qcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("qcr.png"))
    label = tk.Label(qcr, image=image)
    label.pack(expand = "yes")
    qcr.mainloop()


def qinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=qmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = qpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = qlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= qcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = qcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Qatar  information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Russia Information Codes

def rmap():

    rmap = Toplevel(main_window)
    rmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("rmap.png"))
    label = tk.Label(rmap, image=image)
    label.pack(expand = "yes")
    rmap.mainloop()

def rpr():

    rpr = Toplevel(main_window)
    rpr.title("President")
    image = ImageTk.PhotoImage(Image.open("rpr.png"))
    label = tk.Label(rpr, image=image)
    label.pack(expand = "yes")
    rpr.mainloop()

def rlang():

    rlang = Toplevel(main_window)
    rlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("rlang.png"))
    label = tk.Label(rlang, image=image)
    label.pack(expand = "yes")
    rlang.mainloop()

def rcode():

    rcode = Toplevel(main_window)
    rcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("rcode.png"))
    label = tk.Label(rcode, image=image)
    label.pack(expand = "yes")
    rcode.mainloop()

def rcr():

    rcr = Toplevel(main_window)
    rcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("rcr.png"))
    label = tk.Label(rcr, image=image)
    label.pack(expand = "yes")
    rcr.mainloop()


def rinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=rmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = rpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = rlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= rcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = rcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Russia  information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Saudi Arabia Information Codes

def samap():

    samap = Toplevel(main_window)
    samap.title("Map")
    image = ImageTk.PhotoImage(Image.open("samap.png"))
    label = tk.Label(samap, image=image)
    label.pack(expand = "yes")
    samap.mainloop()

def sapr():

    sapr = Toplevel(main_window)
    sapr.title("President")
    image = ImageTk.PhotoImage(Image.open("sapr.png"))
    label = tk.Label(sapr, image=image)
    label.pack(expand = "yes")
    sapr.mainloop()

def salang():

    salang = Toplevel(main_window)
    salang.title("Language")
    image = ImageTk.PhotoImage(Image.open("salang.png"))
    label = tk.Label(salang, image=image)
    label.pack(expand = "yes")
    salang.mainloop()

def sacode():

    sacode = Toplevel(main_window)
    sacode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("sacode.png"))
    label = tk.Label(sacode, image=image)
    label.pack(expand = "yes")
    sacode.mainloop()

def sacr():

    sacr = Toplevel(main_window)
    sacr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("sacr.png"))
    label = tk.Label(sacr, image=image)
    label.pack(expand = "yes")
    sacr.mainloop()


def sainfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"king.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=samap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = sapr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = salang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= sacode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = sacr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Saudi Arabia information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Singapore Information Codes

def simap():

    simap = Toplevel(main_window)
    simap.title("Map")
    image = ImageTk.PhotoImage(Image.open("simap.png"))
    label = tk.Label(simap, image=image)
    label.pack(expand = "yes")
    simap.mainloop()

def sipr():

    sipr = Toplevel(main_window)
    sipr.title("President")
    image = ImageTk.PhotoImage(Image.open("sipr.png"))
    label = tk.Label(sipr, image=image)
    label.pack(expand = "yes")
    sipr.mainloop()

def silang():

    silang = Toplevel(main_window)
    silang.title("Language")
    image = ImageTk.PhotoImage(Image.open("silang.png"))
    label = tk.Label(silang, image=image)
    label.pack(expand = "yes")
    silang.mainloop()

def sicode():

    sicode = Toplevel(main_window)
    sicode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("sicode.png"))
    label = tk.Label(sicode, image=image)
    label.pack(expand = "yes")
    sicode.mainloop()

def sicr():

    sicr = Toplevel(main_window)
    sicr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("sicr.png"))
    label = tk.Label(sicr, image=image)
    label.pack(expand = "yes")
    sicr.mainloop()


def siinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=simap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = sipr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = silang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= sicode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = sicr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Singapore information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Sri Lanka Information Codes

def srmap():

    srmap = Toplevel(main_window)
    srmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("srmap.png"))
    label = tk.Label(srmap, image=image)
    label.pack(expand = "yes")
    srmap.mainloop()

def srpr():

    srpr = Toplevel(main_window)
    srpr.title("President")
    image = ImageTk.PhotoImage(Image.open("srpr.png"))
    label = tk.Label(srpr, image=image)
    label.pack(expand = "yes")
    srpr.mainloop()

def srlang():

    srlang = Toplevel(main_window)
    srlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("srlang.png"))
    label = tk.Label(srlang, image=image)
    label.pack(expand = "yes")
    srlang.mainloop()

def srcode():

    srcode = Toplevel(main_window)
    srcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("srcode.png"))
    label = tk.Label(srcode, image=image)
    label.pack(expand = "yes")
    srcode.mainloop()

def srcr():

    srcr = Toplevel(main_window)
    srcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("srcr.png"))
    label = tk.Label(srcr, image=image)
    label.pack(expand = "yes")
    srcr.mainloop()


def srinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=srmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = srpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = srlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= srcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = srcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Sri Lanka information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Syria Information Codes

def symap():

    symap = Toplevel(main_window)
    symap.title("Map")
    image = ImageTk.PhotoImage(Image.open("symap.png"))
    label = tk.Label(symap, image=image)
    label.pack(expand = "yes")
    symap.mainloop()

def sypr():

    sypr = Toplevel(main_window)
    sypr.title("President")
    image = ImageTk.PhotoImage(Image.open("sypr.png"))
    label = tk.Label(sypr, image=image)
    label.pack(expand = "yes")
    sypr.mainloop()

def sylang():

    sylang = Toplevel(main_window)
    sylang.title("Language")
    image = ImageTk.PhotoImage(Image.open("sylang.png"))
    label = tk.Label(sylang, image=image)
    label.pack(expand = "yes")
    sylang.mainloop()

def sycode():

    sycode = Toplevel(main_window)
    sycode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("sycode.png"))
    label = tk.Label(sycode, image=image)
    label.pack(expand = "yes")
    sycode.mainloop()

def sycr():

    sycr = Toplevel(main_window)
    sycr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("sycr.png"))
    label = tk.Label(sycr, image=image)
    label.pack(expand = "yes")
    sycr.mainloop()


def syinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=symap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = sypr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = sylang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= sycode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = sycr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Syria Information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Thailand Information Codes

def thmap():

    thmap = Toplevel(main_window)
    thmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("thmap.png"))
    label = tk.Label(thmap, image=image)
    label.pack(expand = "yes")
    thmap.mainloop()

def thpr():

    thpr = Toplevel(main_window)
    thpr.title("President")
    image = ImageTk.PhotoImage(Image.open("thpr.png"))
    label = tk.Label(thpr, image=image)
    label.pack(expand = "yes")
    thpr.mainloop()

def thlang():

    thlang = Toplevel(main_window)
    thlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("thlang.png"))
    label = tk.Label(thlang, image=image)
    label.pack(expand = "yes")
    thlang.mainloop()

def thcode():

    thcode = Toplevel(main_window)
    thcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("thcode.png"))
    label = tk.Label(thcode, image=image)
    label.pack(expand = "yes")
    thcode.mainloop()

def thcr():

    thcr = Toplevel(main_window)
    thcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("thcr.png"))
    label = tk.Label(thcr, image=image)
    label.pack(expand = "yes")
    thcr.mainloop()


def thinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=thmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = thpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = thlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= thcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = thcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Thailand Information code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Tajikistan Information Codes

def tajmap():

    tajmap = Toplevel(main_window)
    tajmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("tajmap.png"))
    label = tk.Label(tajmap, image=image)
    label.pack(expand = "yes")
    tajmap.mainloop()

def tajpr():

    tajpr = Toplevel(main_window)
    tajpr.title("President")
    image = ImageTk.PhotoImage(Image.open("tajpr.png"))
    label = tk.Label(tajpr, image=image)
    label.pack(expand = "yes")
    tajpr.mainloop()

def tajlang():

    tajlang = Toplevel(main_window)
    tajlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("tajlang.png"))
    label = tk.Label(tajlang, image=image)
    label.pack(expand = "yes")
    tajlang.mainloop()

def tajcode():

    tajcode = Toplevel(main_window)
    tajcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("tajcode.png"))
    label = tk.Label(tajcode, image=image)
    label.pack(expand = "yes")
    tajcode.mainloop()

def tajcr():

    tajcr = Toplevel(main_window)
    tajcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("tajcr.png"))
    label = tk.Label(tajcr, image=image)
    label.pack(expand = "yes")
    tajcr.mainloop()


def tajinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=tajmap)
    Map.place(relx=0.028, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = tajpr)
    pr.place(relx=0.028, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = tajlang)
    officialLang.place(relx=0.028, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= tajcode)
    country_code.place(relx=0.028, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = tajcr)
    Currency.place(relx=0.028, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Tajikistan Information code

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Turkey Information Codes

def turmap():

    turmap = Toplevel(main_window)
    turmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("turmap.png"))
    label = tk.Label(turmap, image=image)
    label.pack(expand = "yes")
    turmap.mainloop()

def turpr():

    turpr = Toplevel(main_window)
    turpr.title("President")
    image = ImageTk.PhotoImage(Image.open("turpr.png"))
    label = tk.Label(turpr, image=image)
    label.pack(expand = "yes")
    turpr.mainloop()

def turlang():

    turlang = Toplevel(main_window)
    turlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("turlang.png"))
    label = tk.Label(turlang, image=image)
    label.pack(expand = "yes")
    turlang.mainloop()

def turcode():

    turcode = Toplevel(main_window)
    turcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("turcode.png"))
    label = tk.Label(turcode, image=image)
    label.pack(expand = "yes")
    turcode.mainloop()

def turcr():

    turcr = Toplevel(main_window)
    turcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("turcr.png"))
    label = tk.Label(turcr, image=image)
    label.pack(expand = "yes")
    turcr.mainloop()


def turinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=turmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = turpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = turlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= turcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = turcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Turkey Information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Turkmenistan Information Codes

def turkmap():

    turkmap = Toplevel(main_window)
    turkmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("turkmap.png"))
    label = tk.Label(turkmap, image=image)
    label.pack(expand = "yes")
    turkmap.mainloop()

def turkpr():

    turkpr = Toplevel(main_window)
    turkpr.title("President")
    image = ImageTk.PhotoImage(Image.open("turkpr.png"))
    label = tk.Label(turkpr, image=image)
    label.pack(expand = "yes")
    turkpr.mainloop()

def turklang():

    turklang = Toplevel(main_window)
    turklang.title("Language")
    image = ImageTk.PhotoImage(Image.open("turklang.png"))
    label = tk.Label(turklang, image=image)
    label.pack(expand = "yes")
    turklang.mainloop()

def turkcode():

    turkcode = Toplevel(main_window)
    turkcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("turkcode.png"))
    label = tk.Label(turkcode, image=image)
    label.pack(expand = "yes")
    turkcode.mainloop()

def turkcr():

    turkcr = Toplevel(main_window)
    turkcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("turkcr.png"))
    label = tk.Label(turkcr, image=image)
    label.pack(expand = "yes")
    turkcr.mainloop()


def turkinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=turkmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = turkpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = turklang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= turkcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = turkcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Turkmenistan Information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Taiwan Information Codes

def taimap():

    taimap = Toplevel(main_window)
    taimap.title("Map")
    image = ImageTk.PhotoImage(Image.open("taimap.png"))
    label = tk.Label(taimap, image=image)
    label.pack(expand = "yes")
    taimap.mainloop()

def taipr():

    taipr = Toplevel(main_window)
    taipr.title("President")
    image = ImageTk.PhotoImage(Image.open("taipr.png"))
    label = tk.Label(taipr, image=image)
    label.pack(expand = "yes")
    taipr.mainloop()

def tailang():

    tailang = Toplevel(main_window)
    tailang.title("Language")
    image = ImageTk.PhotoImage(Image.open("tailang.png"))
    label = tk.Label(tailang, image=image)
    label.pack(expand = "yes")
    tailang.mainloop()

def taicode():

    taicode = Toplevel(main_window)
    taicode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("taicode.png"))
    label = tk.Label(taicode, image=image)
    label.pack(expand = "yes")
    taicode.mainloop()

def taicr():

    taicr = Toplevel(main_window)
    taicr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("taicr.png"))
    label = tk.Label(taicr, image=image)
    label.pack(expand = "yes")
    taicr.mainloop()


def taiinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=taimap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = taipr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = tailang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= taicode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = taicr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Taiwan Information code



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#UAE Information Codes

def umap():

    umap = Toplevel(main_window)
    umap.title("Map")
    image = ImageTk.PhotoImage(Image.open("umap.png"))
    label = tk.Label(umap, image=image)
    label.pack(expand = "yes")
    umap.mainloop()

def upr():

    upr = Toplevel(main_window)
    upr.title("President")
    image = ImageTk.PhotoImage(Image.open("upr.png"))
    label = tk.Label(upr, image=image)
    label.pack(expand = "yes")
    upr.mainloop()

def ulang():

    ulang = Toplevel(main_window)
    ulang.title("Language")
    image = ImageTk.PhotoImage(Image.open("ulang.png"))
    label = tk.Label(ulang, image=image)
    label.pack(expand = "yes")
    ulang.mainloop()

def ucode():

    ucode = Toplevel(main_window)
    ucode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("ucode.png"))
    label = tk.Label(ucode, image=image)
    label.pack(expand = "yes")
    ucode.mainloop()

def ucr():

    ucr = Toplevel(main_window)
    ucr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("ucr.png"))
    label = tk.Label(ucr, image=image)
    label.pack(expand = "yes")
    ucr.mainloop()


def uinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=umap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = upr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = ulang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= ucode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = ucr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of UAE Information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Uzbekistan Codes

def uzmap():

    uzmap = Toplevel(main_window)
    uzmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("uzmap.png"))
    label = tk.Label(uzmap, image=image)
    label.pack(expand = "yes")
    uzmap.mainloop()

def uzpr():

    uzpr = Toplevel(main_window)
    uzpr.title("President")
    image = ImageTk.PhotoImage(Image.open("uzpr.png"))
    label = tk.Label(uzpr, image=image)
    label.pack(expand = "yes")
    uzpr.mainloop()

def uzlang():

    uzlang = Toplevel(main_window)
    uzlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("uzlang.png"))
    label = tk.Label(uzlang, image=image)
    label.pack(expand = "yes")
    uzlang.mainloop()

def uzcode():

    uzcode = Toplevel(main_window)
    uzcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("uzcode.png"))
    label = tk.Label(uzcode, image=image)
    label.pack(expand = "yes")
    uzcode.mainloop()

def uzcr():

    uzcr = Toplevel(main_window)
    uzcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("uzcr.png"))
    label = tk.Label(uzcr, image=image)
    label.pack(expand = "yes")
    uzcr.mainloop()


def uzinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)






    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    
    
    
    



    Map = tk.Button(win, image= mapb, width = w, command=uzmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = uzpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = uzlang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= uzcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = uzcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    
    
    win.mainloop()


#End of Uzbekistan Information code


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Europe Counteries

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Albania Codes

def albmap():

    albmap = Toplevel(main_window)
    albmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("albmap.png"))
    label = tk.Label(albmap, image=image)
    label.pack(expand = "yes")
    albmap.mainloop()

def albpr():

    albpr = Toplevel(main_window)
    albpr.title("President")
    image = ImageTk.PhotoImage(Image.open("albpr.png"))
    label = tk.Label(albpr, image=image)
    label.pack(expand = "yes")
    albpr.mainloop()

def alblang():

    alblang = Toplevel(main_window)
    alblang.title("Language")
    image = ImageTk.PhotoImage(Image.open("alblang.png"))
    label = tk.Label(alblang, image=image)
    label.pack(expand = "yes")
    alblang.mainloop()

def albcode():

    albcode = Toplevel(main_window)
    albcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("albcode.png"))
    label = tk.Label(albcode, image=image)
    label.pack(expand = "yes")
    albcode.mainloop()

def albcr():

    albcr = Toplevel(main_window)
    albcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("albcr.png"))
    label = tk.Label(albcr, image=image)
    label.pack(expand = "yes")
    albcr.mainloop()


def albinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=albmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = albpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = alblang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= albcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = albcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)


    
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Austria Code


def ausmap():

    ausmap = Toplevel(main_window)
    ausmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("ausmap.png"))
    label = tk.Label(ausmap, image=image)
    label.pack(expand = "yes")
    ausmap.mainloop()

def auspr():

    auspr = Toplevel(main_window)
    auspr.title("President")
    image = ImageTk.PhotoImage(Image.open("auspr.png"))
    label = tk.Label(auspr, image=image)
    label.pack(expand = "yes")
    auspr.mainloop()

def auslang():

    auslang = Toplevel(main_window)
    auslang.title("Language")
    image = ImageTk.PhotoImage(Image.open("auslang.png"))
    label = tk.Label(auslang, image=image)
    label.pack(expand = "yes")
    auslang.mainloop()

def auscode():

    auscode = Toplevel(main_window)
    auscode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("auscode.png"))
    label = tk.Label(auscode, image=image)
    label.pack(expand = "yes")
    auscode.mainloop()

def auscr():

    auscr = Toplevel(main_window)
    auscr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("auscr.png"))
    label = tk.Label(auscr, image=image)
    label.pack(expand = "yes")
    auscr.mainloop()


def ausinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=ausmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = auspr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = auslang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= auscode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = auscr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Belgium Code


def belmap():

    belmap = Toplevel(main_window)
    belmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("belmap.png"))
    label = tk.Label(belmap, image=image)
    label.pack(expand = "yes")
    belmap.mainloop()

def belpr():

    belpr = Toplevel(main_window)
    belpr.title("President")
    image = ImageTk.PhotoImage(Image.open("belpr.png"))
    label = tk.Label(belpr, image=image)
    label.pack(expand = "yes")
    belpr.mainloop()

def bellang():

    bellang = Toplevel(main_window)
    bellang.title("Language")
    image = ImageTk.PhotoImage(Image.open("bellang.png"))
    label = tk.Label(bellang, image=image)
    label.pack(expand = "yes")
    bellang.mainloop()

def belcode():

    belcode = Toplevel(main_window)
    belcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("belcode.png"))
    label = tk.Label(belcode, image=image)
    label.pack(expand = "yes")
    belcode.mainloop()

def belcr():

    belcr = Toplevel(main_window)
    belcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("belcr.png"))
    label = tk.Label(belcr, image=image)
    label.pack(expand = "yes")
    belcr.mainloop()


def belinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=belmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = belpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = bellang)
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= belcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = belcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Bulgaria Code


def bulmap():

    bulmap = Toplevel(main_window)
    bulmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("bulmap.png"))
    label = tk.Label(bulmap, image=image)
    label.pack(expand = "yes")
    bulmap.mainloop()

def bulpr():

    bulpr = Toplevel(main_window)
    bulpr.title("President")
    image = ImageTk.PhotoImage(Image.open("bulpr.png"))
    label = tk.Label(bulpr, image=image)
    label.pack(expand = "yes")
    bulpr.mainloop()

def bullang():

    bullang = Toplevel(main_window)
    bullang.title("Language")
    image = ImageTk.PhotoImage(Image.open("bullang.png"))
    label = tk.Label(bullang, image=image)
    label.pack(expand = "yes")
    bullang.mainloop()

def bulcode():

    bulcode = Toplevel(main_window)
    bulcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("bulcode.png"))
    label = tk.Label(bulcode, image=image)
    label.pack(expand = "yes")
    bulcode.mainloop()

def bulcr():

    bulcr = Toplevel(main_window)
    bulcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("bulcr.png"))
    label = tk.Label(bulcr, image=image)
    label.pack(expand = "yes")
    bulcr.mainloop()


def bulinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=bulmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = bulpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = bullang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= bulcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = bulcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Croatia Code


def cromap():

    cromap = Toplevel(main_window)
    cromap.title("Map")
    image = ImageTk.PhotoImage(Image.open("cromap.png"))
    label = tk.Label(cromap, image=image)
    label.pack(expand = "yes")
    cromap.mainloop()

def cropr():

    cropr = Toplevel(main_window)
    cropr.title("President")
    image = ImageTk.PhotoImage(Image.open("cropr.png"))
    label = tk.Label(cropr, image=image)
    label.pack(expand = "yes")
    cropr.mainloop()

def crolang():

    crolang = Toplevel(main_window)
    crolang.title("Language")
    image = ImageTk.PhotoImage(Image.open("crolang.png"))
    label = tk.Label(crolang, image=image)
    label.pack(expand = "yes")
    crolang.mainloop()

def crocode():

    crocode = Toplevel(main_window)
    crocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("crocode.png"))
    label = tk.Label(crocode, image=image)
    label.pack(expand = "yes")
    crocode.mainloop()

def crocr():

    crocr = Toplevel(main_window)
    crocr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("crocr.png"))
    label = tk.Label(crocr, image=image)
    label.pack(expand = "yes")
    crocr.mainloop()


def croinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=cromap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = cropr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = crolang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= crocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = crocr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Czechia  Code


def czmap():

    czmap = Toplevel(main_window)
    czmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("czmap.png"))
    label = tk.Label(czmap, image=image)
    label.pack(expand = "yes")
    czmap.mainloop()

def czpr():

    czpr = Toplevel(main_window)
    czpr.title("President")
    image = ImageTk.PhotoImage(Image.open("czpr.png"))
    label = tk.Label(czpr, image=image)
    label.pack(expand = "yes")
    czpr.mainloop()

def czlang():

    czlang = Toplevel(main_window)
    czlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("czlang.png"))
    label = tk.Label(czlang, image=image)
    label.pack(expand = "yes")
    czlang.mainloop()

def czcode():

    czcode = Toplevel(main_window)
    czcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("czcode.png"))
    label = tk.Label(czcode, image=image)
    label.pack(expand = "yes")
    czcode.mainloop()

def czcr():

    czcr = Toplevel(main_window)
    czcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("czcr.png"))
    label = tk.Label(czcr, image=image)
    label.pack(expand = "yes")
    czcr.mainloop()


def czinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=czmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = czpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = czlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= czcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = czcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Denmark  Code


def denmap():

    denmap = Toplevel(main_window)
    denmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("denmap.png"))
    label = tk.Label(denmap, image=image)
    label.pack(expand = "yes")
    denmap.mainloop()

def denpr():

    denpr = Toplevel(main_window)
    denpr.title("President")
    image = ImageTk.PhotoImage(Image.open("denpr.png"))
    label = tk.Label(denpr, image=image)
    label.pack(expand = "yes")
    denpr.mainloop()

def denlang():

    denlang = Toplevel(main_window)
    denlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("denlang.png"))
    label = tk.Label(denlang, image=image)
    label.pack(expand = "yes")
    denlang.mainloop()

def dencode():

    dencode = Toplevel(main_window)
    dencode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("dencode.png"))
    label = tk.Label(dencode, image=image)
    label.pack(expand = "yes")
    dencode.mainloop()

def dencr():

    dencr = Toplevel(main_window)
    dencr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("dencr.png"))
    label = tk.Label(dencr, image=image)
    label.pack(expand = "yes")
    dencr.mainloop()


def deninfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=denmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = denpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = denlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= dencode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = dencr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()





#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Estonia  Code


def estmap():

    estmap = Toplevel(main_window)
    estmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("estmap.png"))
    label = tk.Label(estmap, image=image)
    label.pack(expand = "yes")
    estmap.mainloop()

def estpr():

    estpr = Toplevel(main_window)
    estpr.title("President")
    image = ImageTk.PhotoImage(Image.open("estpr.png"))
    label = tk.Label(estpr, image=image)
    label.pack(expand = "yes")
    estpr.mainloop()

def estlang():

    estlang = Toplevel(main_window)
    estlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("estlang.png"))
    label = tk.Label(estlang, image=image)
    label.pack(expand = "yes")
    estlang.mainloop()

def estcode():

    estcode = Toplevel(main_window)
    estcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("estcode.png"))
    label = tk.Label(estcode, image=image)
    label.pack(expand = "yes")
    estcode.mainloop()

def estcr():

    estcr = Toplevel(main_window)
    estcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("estcr.png"))
    label = tk.Label(estcr, image=image)
    label.pack(expand = "yes")
    estcr.mainloop()


def estinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=estmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = estpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = estlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= estcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = estcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Finland Code


def finmap():

    finmap = Toplevel(main_window)
    finmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("finmap.png"))
    label = tk.Label(finmap, image=image)
    label.pack(expand = "yes")
    finmap.mainloop()

def finpr():

    finpr = Toplevel(main_window)
    finpr.title("President")
    image = ImageTk.PhotoImage(Image.open("finpr.png"))
    label = tk.Label(finpr, image=image)
    label.pack(expand = "yes")
    finpr.mainloop()

def finlang():

    finlang = Toplevel(main_window)
    finlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("finlang.png"))
    label = tk.Label(finlang, image=image)
    label.pack(expand = "yes")
    finlang.mainloop()

def fincode():

    fincode = Toplevel(main_window)
    fincode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("fincode.png"))
    label = tk.Label(fincode, image=image)
    label.pack(expand = "yes")
    fincode.mainloop()

def fincr():

    fincr = Toplevel(main_window)
    fincr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("fincr.png"))
    label = tk.Label(fincr, image=image)
    label.pack(expand = "yes")
    fincr.mainloop()


def fininfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=finmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = finpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = finlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= fincode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = fincr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#France Code


def frmap():

    frmap = Toplevel(main_window)
    frmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("frmap.png"))
    label = tk.Label(frmap, image=image)
    label.pack(expand = "yes")
    frmap.mainloop()

def frpr():

    frpr = Toplevel(main_window)
    frpr.title("President")
    image = ImageTk.PhotoImage(Image.open("frpr.png"))
    label = tk.Label(frpr, image=image)
    label.pack(expand = "yes")
    frpr.mainloop()

def frlang():

    frlang = Toplevel(main_window)
    frlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("frlang.png"))
    label = tk.Label(frlang, image=image)
    label.pack(expand = "yes")
    frlang.mainloop()

def frcode():

    frcode = Toplevel(main_window)
    frcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("frcode.png"))
    label = tk.Label(frcode, image=image)
    label.pack(expand = "yes")
    frcode.mainloop()

def frcr():

    frcr = Toplevel(main_window)
    frcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("frcr.png"))
    label = tk.Label(frcr, image=image)
    label.pack(expand = "yes")
    frcr.mainloop()


def frinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=frmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = frpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = frlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= frcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = frcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________




#Germany Code


def grmap():

    grmap = Toplevel(main_window)
    grmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("grmap.png"))
    label = tk.Label(grmap, image=image)
    label.pack(expand = "yes")
    grmap.mainloop()

def grpr():

    grpr = Toplevel(main_window)
    grpr.title("President")
    image = ImageTk.PhotoImage(Image.open("grpr.png"))
    label = tk.Label(grpr, image=image)
    label.pack(expand = "yes")
    grpr.mainloop()

def grlang():

    grlang = Toplevel(main_window)
    grlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("grlang.png"))
    label = tk.Label(grlang, image=image)
    label.pack(expand = "yes")
    grlang.mainloop()

def grcode():

    grcode = Toplevel(main_window)
    grcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("grcode.png"))
    label = tk.Label(grcode, image=image)
    label.pack(expand = "yes")
    grcode.mainloop()

def grcr():

    grcr = Toplevel(main_window)
    grcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("grcr.png"))
    label = tk.Label(grcr, image=image)
    label.pack(expand = "yes")
    grcr.mainloop()


def grinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=grmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = grpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = grlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= grcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = grcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Greece Code


def gremap():

    gremap = Toplevel(main_window)
    gremap.title("Map")
    image = ImageTk.PhotoImage(Image.open("gremap.png"))
    label = tk.Label(gremap, image=image)
    label.pack(expand = "yes")
    gremap.mainloop()

def grepr():

    grepr = Toplevel(main_window)
    grepr.title("President")
    image = ImageTk.PhotoImage(Image.open("grepr.png"))
    label = tk.Label(grepr, image=image)
    label.pack(expand = "yes")
    grepr.mainloop()

def grelang():

    grelang = Toplevel(main_window)
    grelang.title("Language")
    image = ImageTk.PhotoImage(Image.open("grelang.png"))
    label = tk.Label(grelang, image=image)
    label.pack(expand = "yes")
    grelang.mainloop()

def grecode():

    grecode = Toplevel(main_window)
    grecode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("grecode.png"))
    label = tk.Label(grecode, image=image)
    label.pack(expand = "yes")
    grecode.mainloop()

def grecr():

    grecr = Toplevel(main_window)
    grecr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("grecr.png"))
    label = tk.Label(grecr, image=image)
    label.pack(expand = "yes")
    grecr.mainloop()


def greinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=gremap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = grepr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = grelang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= grecode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = grecr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Hungary Code


def humap():

    humap = Toplevel(main_window)
    humap.title("Map")
    image = ImageTk.PhotoImage(Image.open("humap.png"))
    label = tk.Label(humap, image=image)
    label.pack(expand = "yes")
    humap.mainloop()

def hupr():

    hupr = Toplevel(main_window)
    hupr.title("President")
    image = ImageTk.PhotoImage(Image.open("hupr.png"))
    label = tk.Label(hupr, image=image)
    label.pack(expand = "yes")
    hupr.mainloop()

def hulang():

    hulang = Toplevel(main_window)
    hulang.title("Language")
    image = ImageTk.PhotoImage(Image.open("hulang.png"))
    label = tk.Label(hulang, image=image)
    label.pack(expand = "yes")
    hulang.mainloop()

def hucode():

    hucode = Toplevel(main_window)
    hucode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("hucode.png"))
    label = tk.Label(hucode, image=image)
    label.pack(expand = "yes")
    hucode.mainloop()

def hucr():

    hucr = Toplevel(main_window)
    hucr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("hucr.png"))
    label = tk.Label(hucr, image=image)
    label.pack(expand = "yes")
    hucr.mainloop()


def huinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=humap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = hupr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = hulang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= hucode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = hucr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Iceland Code


def icemap():

    icemap = Toplevel(main_window)
    icemap.title("Map")
    image = ImageTk.PhotoImage(Image.open("icemap.png"))
    label = tk.Label(icemap, image=image)
    label.pack(expand = "yes")
    icemap.mainloop()

def icpr():

    icpr = Toplevel(main_window)
    icpr.title("President")
    image = ImageTk.PhotoImage(Image.open("icpr.png"))
    label = tk.Label(icpr, image=image)
    label.pack(expand = "yes")
    icpr.mainloop()

def iclang():

    iclang = Toplevel(main_window)
    iclang.title("Language")
    image = ImageTk.PhotoImage(Image.open("iclang.png"))
    label = tk.Label(iclang, image=image)
    label.pack(expand = "yes")
    iclang.mainloop()

def iccode():

    iccode = Toplevel(main_window)
    iccode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("iccode.png"))
    label = tk.Label(iccode, image=image)
    label.pack(expand = "yes")
    iccode.mainloop()

def iccr():

    iccr = Toplevel(main_window)
    iccr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("iccr.png"))
    label = tk.Label(iccr, image=image)
    label.pack(expand = "yes")
    iccr.mainloop()


def icinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=icemap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = icpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = iclang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= iccode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = iccr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Ireland Code


def irlmap():

    irlmap = Toplevel(main_window)
    irlmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("irlmap.png"))
    label = tk.Label(irlmap, image=image)
    label.pack(expand = "yes")
    irlmap.mainloop()

def irlpr():

    irlpr = Toplevel(main_window)
    irlpr.title("President")
    image = ImageTk.PhotoImage(Image.open("irlpr.png"))
    label = tk.Label(irlpr, image=image)
    label.pack(expand = "yes")
    irlpr.mainloop()

def irllang():

    irllang = Toplevel(main_window)
    irllang.title("Language")
    image = ImageTk.PhotoImage(Image.open("irllang.png"))
    label = tk.Label(irllang, image=image)
    label.pack(expand = "yes")
    irllang.mainloop()

def irlcode():

    irlcode = Toplevel(main_window)
    irlcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("irlcode.png"))
    label = tk.Label(irlcode, image=image)
    label.pack(expand = "yes")
    irlcode.mainloop()

def irlcr():

    irlcr = Toplevel(main_window)
    irlcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("irlcr.png"))
    label = tk.Label(irlcr, image=image)
    label.pack(expand = "yes")
    irlcr.mainloop()


def irlinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=irlmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = irlpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = irllang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= irlcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = irlcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Italy Code


def itmap():

    itmap = Toplevel(main_window)
    itmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("itmap.png"))
    label = tk.Label(itmap, image=image)
    label.pack(expand = "yes")
    itmap.mainloop()

def itpr():

    itpr = Toplevel(main_window)
    itpr.title("President")
    image = ImageTk.PhotoImage(Image.open("itpr.png"))
    label = tk.Label(itpr, image=image)
    label.pack(expand = "yes")
    itpr.mainloop()

def itlang():

    itlang = Toplevel(main_window)
    itlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("itlang.png"))
    label = tk.Label(itlang, image=image)
    label.pack(expand = "yes")
    itlang.mainloop()

def itcode():

    itcode = Toplevel(main_window)
    itcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("itcode.png"))
    label = tk.Label(itcode, image=image)
    label.pack(expand = "yes")
    itcode.mainloop()

def itcr():

    itcr = Toplevel(main_window)
    itcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("itcr.png"))
    label = tk.Label(itcr, image=image)
    label.pack(expand = "yes")
    itcr.mainloop()


def itinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=itmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = itpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = itlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= itcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = itcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Lithuania Code


def litmap():

    litmap = Toplevel(main_window)
    litmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("litmap.png"))
    label = tk.Label(litmap, image=image)
    label.pack(expand = "yes")
    litmap.mainloop()

def litpr():

    litpr = Toplevel(main_window)
    litpr.title("President")
    image = ImageTk.PhotoImage(Image.open("litpr.png"))
    label = tk.Label(litpr, image=image)
    label.pack(expand = "yes")
    litpr.mainloop()

def litlang():

    litlang = Toplevel(main_window)
    litlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("litlang.png"))
    label = tk.Label(litlang, image=image)
    label.pack(expand = "yes")
    litlang.mainloop()

def litcode():

    litcode = Toplevel(main_window)
    litcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("litcode.png"))
    label = tk.Label(litcode, image=image)
    label.pack(expand = "yes")
    litcode.mainloop()

def litcr():

    litcr = Toplevel(main_window)
    litcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("litcr.png"))
    label = tk.Label(litcr, image=image)
    label.pack(expand = "yes")
    litcr.mainloop()


def litinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=irlmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = irlpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = irllang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= irlcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = irlcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Luxembourg Code


def luxmap():

    luxmap = Toplevel(main_window)
    luxmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("luxmap.png"))
    label = tk.Label(luxmap, image=image)
    label.pack(expand = "yes")
    luxmap.mainloop()

def luxpr():

    luxpr = Toplevel(main_window)
    luxpr.title("President")
    image = ImageTk.PhotoImage(Image.open("luxpr.png"))
    label = tk.Label(luxpr, image=image)
    label.pack(expand = "yes")
    luxpr.mainloop()

def luxlang():

    luxlang = Toplevel(main_window)
    luxlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("luxlang.png"))
    label = tk.Label(luxlang, image=image)
    label.pack(expand = "yes")
    luxlang.mainloop()

def luxcode():

    luxcode = Toplevel(main_window)
    luxcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("luxcode.png"))
    label = tk.Label(luxcode, image=image)
    label.pack(expand = "yes")
    luxcode.mainloop()

def luxcr():

    luxcr = Toplevel(main_window)
    luxcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("luxcr.png"))
    label = tk.Label(luxcr, image=image)
    label.pack(expand = "yes")
    luxcr.mainloop()


def luxinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=luxmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = luxpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = luxlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= luxcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = luxcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________
#Monaco Code


def momap():

    momap = Toplevel(main_window)
    momap.title("Map")
    image = ImageTk.PhotoImage(Image.open("momap.png"))
    label = tk.Label(momap, image=image)
    label.pack(expand = "yes")
    momap.mainloop()

def mopr():

    mopr = Toplevel(main_window)
    mopr.title("President")
    image = ImageTk.PhotoImage(Image.open("mopr.png"))
    label = tk.Label(mopr, image=image)
    label.pack(expand = "yes")
    mopr.mainloop()

def molang():

    molang = Toplevel(main_window)
    molang.title("Language")
    image = ImageTk.PhotoImage(Image.open("molang.png"))
    label = tk.Label(molang, image=image)
    label.pack(expand = "yes")
    molang.mainloop()

def mocode():

    mocode = Toplevel(main_window)
    mocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("mocode.png"))
    label = tk.Label(mocode, image=image)
    label.pack(expand = "yes")
    mocode.mainloop()

def mocr():

    mocr = Toplevel(main_window)
    mocr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("mocr.png"))
    label = tk.Label(mocr, image=image)
    label.pack(expand = "yes")
    mocr.mainloop()


def moinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=momap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = mopr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = molang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= mocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = mocr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________
#Netherlands Code


def netmap():

    netmap = Toplevel(main_window)
    netmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("netmap.png"))
    label = tk.Label(netmap, image=image)
    label.pack(expand = "yes")
    netmap.mainloop()

def netpr():

    netpr = Toplevel(main_window)
    netpr.title("President")
    image = ImageTk.PhotoImage(Image.open("netpr.png"))
    label = tk.Label(netpr, image=image)
    label.pack(expand = "yes")
    netpr.mainloop()

def netlang():

    netlang = Toplevel(main_window)
    netlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("netlang.png"))
    label = tk.Label(netlang, image=image)
    label.pack(expand = "yes")
    netlang.mainloop()

def netcode():

    netcode = Toplevel(main_window)
    netcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("netcode.png"))
    label = tk.Label(netcode, image=image)
    label.pack(expand = "yes")
    netcode.mainloop()

def netcr():

    netcr = Toplevel(main_window)
    netcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("netcr.png"))
    label = tk.Label(netcr, image=image)
    label.pack(expand = "yes")
    netcr.mainloop()


def netinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=netmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = netpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = netlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= netcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = netcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Norway Code


def normap():

    normap = Toplevel(main_window)
    normap.title("Map")
    image = ImageTk.PhotoImage(Image.open("normap.png"))
    label = tk.Label(normap, image=image)
    label.pack(expand = "yes")
    normap.mainloop()

def norpr():

    norpr = Toplevel(main_window)
    norpr.title("President")
    image = ImageTk.PhotoImage(Image.open("norpr.png"))
    label = tk.Label(norpr, image=image)
    label.pack(expand = "yes")
    norpr.mainloop()

def norlang():

    norlang = Toplevel(main_window)
    norlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("norlang.png"))
    label = tk.Label(norlang, image=image)
    label.pack(expand = "yes")
    norlang.mainloop()

def norcode():

    norcode = Toplevel(main_window)
    norcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("norcode.png"))
    label = tk.Label(norcode, image=image)
    label.pack(expand = "yes")
    norcode.mainloop()

def norcr():

    norcr = Toplevel(main_window)
    norcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("norcr.png"))
    label = tk.Label(norcr, image=image)
    label.pack(expand = "yes")
    norcr.mainloop()


def norinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=normap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = norpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = norlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= norcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = norcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Poland Code


def polmap():

    polmap = Toplevel(main_window)
    polmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("polmap.png"))
    label = tk.Label(polmap, image=image)
    label.pack(expand = "yes")
    polmap.mainloop()

def polpr():

    polpr = Toplevel(main_window)
    polpr.title("President")
    image = ImageTk.PhotoImage(Image.open("polpr.png"))
    label = tk.Label(polpr, image=image)
    label.pack(expand = "yes")
    polpr.mainloop()

def pollang():

    pollang = Toplevel(main_window)
    pollang.title("Language")
    image = ImageTk.PhotoImage(Image.open("pollang.png"))
    label = tk.Label(pollang, image=image)
    label.pack(expand = "yes")
    pollang.mainloop()

def polcode():

    polcode = Toplevel(main_window)
    polcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("polcode.png"))
    label = tk.Label(polcode, image=image)
    label.pack(expand = "yes")
    polcode.mainloop()

def polcr():

    polcr = Toplevel(main_window)
    polcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("polcr.png"))
    label = tk.Label(polcr, image=image)
    label.pack(expand = "yes")
    polcr.mainloop()


def polinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=polmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = polpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = pollang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= polcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = polcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Portugal Code


def portmap():

    portmap = Toplevel(main_window)
    portmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("portmap.png"))
    label = tk.Label(portmap, image=image)
    label.pack(expand = "yes")
    portmap.mainloop()

def portpr():

    portpr = Toplevel(main_window)
    portpr.title("President")
    image = ImageTk.PhotoImage(Image.open("portpr.png"))
    label = tk.Label(portpr, image=image)
    label.pack(expand = "yes")
    portpr.mainloop()

def portlang():

    portlang = Toplevel(main_window)
    portlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("portlang.png"))
    label = tk.Label(portlang, image=image)
    label.pack(expand = "yes")
    portlang.mainloop()

def portcode():

    portcode = Toplevel(main_window)
    portcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("portcode.png"))
    label = tk.Label(portcode, image=image)
    label.pack(expand = "yes")
    portcode.mainloop()

def portcr():

    portcr = Toplevel(main_window)
    portcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("portcr.png"))
    label = tk.Label(portcr, image=image)
    label.pack(expand = "yes")
    portcr.mainloop()


def portinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=portmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = portpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = portlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= portcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = portcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Romania Code


def romap():

    romap = Toplevel(main_window)
    romap.title("Map")
    image = ImageTk.PhotoImage(Image.open("romap.png"))
    label = tk.Label(romap, image=image)
    label.pack(expand = "yes")
    romap.mainloop()

def ropr():

    ropr = Toplevel(main_window)
    ropr.title("President")
    image = ImageTk.PhotoImage(Image.open("ropr.png"))
    label = tk.Label(ropr, image=image)
    label.pack(expand = "yes")
    ropr.mainloop()

def rolang():

    rolang = Toplevel(main_window)
    rolang.title("Language")
    image = ImageTk.PhotoImage(Image.open("rolang.png"))
    label = tk.Label(rolang, image=image)
    label.pack(expand = "yes")
    rolang.mainloop()

def rocode():

    rocode = Toplevel(main_window)
    rocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("rocode.png"))
    label = tk.Label(rocode, image=image)
    label.pack(expand = "yes")
    rocode.mainloop()

def rocr():

    rocr = Toplevel(main_window)
    rocr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("rocr.png"))
    label = tk.Label(rocr, image=image)
    label.pack(expand = "yes")
    rocr.mainloop()


def roinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=romap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = ropr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = rolang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= rocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = rocr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

#Slovakia Code


def slomap():

    slomap = Toplevel(main_window)
    slomap.title("Map")
    image = ImageTk.PhotoImage(Image.open("slomap.png"))
    label = tk.Label(slomap, image=image)
    label.pack(expand = "yes")
    slomap.mainloop()

def slopr():

    slopr = Toplevel(main_window)
    slopr.title("President")
    image = ImageTk.PhotoImage(Image.open("slopr.png"))
    label = tk.Label(slopr, image=image)
    label.pack(expand = "yes")
    slopr.mainloop()

def slolang():

    slolang = Toplevel(main_window)
    slolang.title("Language")
    image = ImageTk.PhotoImage(Image.open("slolang.png"))
    label = tk.Label(slolang, image=image)
    label.pack(expand = "yes")
    slolang.mainloop()

def slocode():

    slocode = Toplevel(main_window)
    slocode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("slocode.png"))
    label = tk.Label(slocode, image=image)
    label.pack(expand = "yes")
    slocode.mainloop()

def slocr():

    slocr = Toplevel(main_window)
    slocr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("slocr.png"))
    label = tk.Label(slocr, image=image)
    label.pack(expand = "yes")
    slocr.mainloop()


def sloinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=slomap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = slopr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = slolang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= slocode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = slocr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Spain Code


def spmap():

    spmap = Toplevel(main_window)
    spmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("spmap.png"))
    label = tk.Label(spmap, image=image)
    label.pack(expand = "yes")
    spmap.mainloop()

def sppr():

    sppr = Toplevel(main_window)
    sppr.title("President")
    image = ImageTk.PhotoImage(Image.open("sppr.png"))
    label = tk.Label(sppr, image=image)
    label.pack(expand = "yes")
    sppr.mainloop()

def splang():

    splang = Toplevel(main_window)
    splang.title("Language")
    image = ImageTk.PhotoImage(Image.open("splang.png"))
    label = tk.Label(splang, image=image)
    label.pack(expand = "yes")
    splang.mainloop()

def spcode():

    spcode = Toplevel(main_window)
    spcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("spcode.png"))
    label = tk.Label(spcode, image=image)
    label.pack(expand = "yes")
    spcode.mainloop()

def spcr():

    spcr = Toplevel(main_window)
    spcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("spcr.png"))
    label = tk.Label(spcr, image=image)
    label.pack(expand = "yes")
    spcr.mainloop()


def spinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=spmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = sppr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = splang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= spcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = spcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________


#Sweden Code


def swmap():

    swmap = Toplevel(main_window)
    swmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("swmap.png"))
    label = tk.Label(swmap, image=image)
    label.pack(expand = "yes")
    swmap.mainloop()

def swpr():

    swpr = Toplevel(main_window)
    swpr.title("President")
    image = ImageTk.PhotoImage(Image.open("swpr.png"))
    label = tk.Label(swpr, image=image)
    label.pack(expand = "yes")
    swpr.mainloop()

def swlang():

    swlang = Toplevel(main_window)
    swlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("swlang.png"))
    label = tk.Label(swlang, image=image)
    label.pack(expand = "yes")
    swlang.mainloop()

def swcode():

    swcode = Toplevel(main_window)
    swcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("swcode.png"))
    label = tk.Label(swcode, image=image)
    label.pack(expand = "yes")
    swcode.mainloop()

def swcr():

    swcr = Toplevel(main_window)
    swcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("swcr.png"))
    label = tk.Label(swcr, image=image)
    label.pack(expand = "yes")
    swcr.mainloop()


def swinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=swmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = swpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = swlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= swcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = swcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Switzerlang Code


def switmap():

    switmap = Toplevel(main_window)
    switmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("switmap.png"))
    label = tk.Label(switmap, image=image)
    label.pack(expand = "yes")
    switmap.mainloop()

def switpr():

    switpr = Toplevel(main_window)
    switpr.title("President")
    image = ImageTk.PhotoImage(Image.open("switpr.png"))
    label = tk.Label(switpr, image=image)
    label.pack(expand = "yes")
    switpr.mainloop()

def switlang():

    switlang = Toplevel(main_window)
    switlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("switlang.png"))
    label = tk.Label(switlang, image=image)
    label.pack(expand = "yes")
    switlang.mainloop()

def switcode():

    switcode = Toplevel(main_window)
    switcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("switcode.png"))
    label = tk.Label(switcode, image=image)
    label.pack(expand = "yes")
    switcode.mainloop()

def switcr():

    switcr = Toplevel(main_window)
    switcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("switcr.png"))
    label = tk.Label(switcr, image=image)
    label.pack(expand = "yes")
    switcr.mainloop()


def switinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=switmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = switpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = switlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= switcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = switcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



#Ukraine Code


def ukrmap():

    ukrmap = Toplevel(main_window)
    ukrmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("ukrmap.png"))
    label = tk.Label(ukrmap, image=image)
    label.pack(expand = "yes")
    ukrmap.mainloop()

def ukrpr():

    ukrpr = Toplevel(main_window)
    ukrpr.title("President")
    image = ImageTk.PhotoImage(Image.open("ukrpr.png"))
    label = tk.Label(ukrpr, image=image)
    label.pack(expand = "yes")
    ukrpr.mainloop()

def ukrlang():

    ukrlang = Toplevel(main_window)
    ukrlang.title("Language")
    image = ImageTk.PhotoImage(Image.open("ukrlang.png"))
    label = tk.Label(ukrlang, image=image)
    label.pack(expand = "yes")
    ukrlang.mainloop()

def ukrcode():

    ukrcode = Toplevel(main_window)
    ukrcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("ukrcode.png"))
    label = tk.Label(ukrcode, image=image)
    label.pack(expand = "yes")
    ukrcode.mainloop()

def ukrcr():

    ukrcr = Toplevel(main_window)
    ukrcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("ukrcr.png"))
    label = tk.Label(ukrcr, image=image)
    label.pack(expand = "yes")
    ukrcr.mainloop()


def ukrinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=netmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = netpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = netlang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= netcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = netcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________





#United Kingdom Code


def ukmap():

    ukmap = Toplevel(main_window)
    ukmap.title("Map")
    image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\ukmap.png"))
    label = tk.Label(ukmap, image=image)
    label.pack(expand = "yes")
    ukmap.mainloop()

def ukpr():

    ukpr = Toplevel(main_window)
    ukpr.title("President")
    image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\ukpr.png"))
    label = tk.Label(ukpr, image=image)
    label.pack(expand = "yes")
    ukpr.mainloop()

def uklang():

    uklang = Toplevel(main_window)
    uklang.title("Language")
    image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\uklang.png"))
    label = tk.Label(uklang, image=image)
    label.pack(expand = "yes")
    uklang.mainloop()

def ukcode():

    ukcode = Toplevel(main_window)
    ukcode.title("Country Code ")
    image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\ukcode.png"))
    label = tk.Label(ukcode, image=image)
    label.pack(expand = "yes")
    ukcode.mainloop()

def ukcr():

    ukcr = Toplevel(main_window)
    ukcr.title("Currency")
    image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\ukcr.png"))
    label = tk.Label(ukcr, image=image)
    label.pack(expand = "yes")
    ukcr.mainloop()


def ukinfo():
    win = Toplevel(main_window)
    win.title("Select Information")
    win.geometry('290x660')

    bg_image = ImageTk.PhotoImage(Image.open("D:\\ProjectData\\chwin.png"))
    bg_label = tk.Label(win, image=bg_image)
    bg_label.place(x=0, y= 0, relwidth=1,relheight=1)


    win.resizable(False,False)
    

    mapb = PhotoImage(file = r"D:\\ProjectData\\mapb.png")
    mapb = mapb.subsample(2, 2)

    prb = PhotoImage(file = r"D:\\ProjectData\\prb.png")
    prb = prb.subsample(2, 2)

    offlb = PhotoImage(file = r"D:\\ProjectData\\offlb.png")
    offlb = offlb.subsample(2, 2)

    ccodeb = PhotoImage(file = r"D:\\ProjectData\\ccodeb.png")
    ccodeb = ccodeb.subsample(2, 2)

    curb = PhotoImage(file = r"D:\\ProjectData\\curb.png")
    curb = curb.subsample(2, 2)


    Map = tk.Button(win, image= mapb, width = w, command=ukmap)
    Map.place(relx=0.030, rely=0.02, relheight = 0.06, relwidth = 0.95)
    
    pr = tk.Button(win, image= prb, width = w, command = ukpr)
    pr.place(relx=0.030, rely=0.09, relheight = 0.06, relwidth = 0.95)
    
    officialLang = tk.Button(win, image= offlb, width = w, command = uklang )
    officialLang.place(relx=0.030, rely=0.16, relheight = 0.06, relwidth = 0.95)
    
    country_code = tk.Button(win, image= ccodeb, width = w, command= ukcode)
    country_code.place(relx=0.030, rely=0.23, relheight = 0.06, relwidth = 0.95)
    
    Currency = tk.Button(win, image= curb, width = w, command = ukcr)
    Currency.place(relx=0.030, rely=0.30, relheight = 0.06, relwidth = 0.95)
 
    win.mainloop()



new = 1
url = "https://www.facebook.com/mohammadzafar.hayatzada"

def contact():
	webbrowser.open(url,new=new)


    #______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________



 #My Main/Start/Root Menu
from tkinter import *
import PIL
import tkinter as tk
import PIL.Image
from PIL import Image
from tkinter import ttk
from tkinter import Tk
from tkinter import PhotoImage
from tkinter import font
from tkinter import Tk, Label ; from tkinter.font import families
from tkinter.font import families
from PIL import ImageTk
import os
import webbrowser


main_window = tk.Tk()
main_window.title("Program")
main_window.geometry("605x660")


canvas = tk.Canvas(main_window)
scroll_y = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg = 'sky blue')


main_window.resizable(False,True)


main_window.title("CountryGuide")

#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________
 #Menu folded
#Main Menu Buttons Images 
afg = PhotoImage(file = r"af2.png")
# Resizing image to fit on button 
afg1 = afg.subsample(2, 2) 

azer = PhotoImage(file = r"azer.png")
azer1 = azer.subsample(2, 2) 

bang = PhotoImage(file = r"bang.png")
bang1 = bang.subsample(2, 2) 

bah = PhotoImage(file = r"bah.png")
bah1 = bah.subsample(2, 2)

china = PhotoImage(file = r"china.png")
china1 = china.subsample(2, 2)

cyprus = PhotoImage(file = r"cy.png")
cyprus1 = cyprus.subsample(2,2)

geo = PhotoImage(file = r"geo.png")
geo1 = geo.subsample(2,2)


india = PhotoImage(file = r"india.png")
india1 = india.subsample(2,2)

indo = PhotoImage(file = r"indo.png")
indo1 = indo.subsample(2,2)

indo = PhotoImage(file = r"indo.png")
indo1 = indo.subsample(2,2)


iran = PhotoImage(file = r"iran.png")
iran1 = iran.subsample(2,2)


iraq = PhotoImage(file = r"iraq.png")
iraq1 = iraq.subsample(2,2)


israel = PhotoImage(file = r"israel.png")
israel1 = israel.subsample(2,2)

Japan = PhotoImage(file = r"Japan.png")
Japan1 = Japan.subsample(2,2)


kaz = PhotoImage(file = r"kaz.png")
kaz1 = kaz.subsample(2,2)


kw = PhotoImage(file = r"kw.png")
kw1 = kw.subsample(2,2)


ky = PhotoImage(file = r"ky.png")
ky1 = ky.subsample(2,2)


Leb = PhotoImage(file = r"Leb.png")
Leb1 = Leb.subsample(2,2)


mal = PhotoImage(file = r"mal.png")
mal1 = mal.subsample(2,2)


mald = PhotoImage(file = r"mald.png")
mald1 = mald.subsample(2,2)


myn = PhotoImage(file = r"myn.png")
myn1 = myn.subsample(2,2)


ne = PhotoImage(file = r"ne.png")
ne1 = ne.subsample(2,2)

nk = PhotoImage(file = r"nk.png")
nk1 = nk.subsample(2,2)

om = PhotoImage(file = r"om.png")
om1 = om.subsample(2,2)

ph = PhotoImage(file = r"ph.png")
ph1 = ph.subsample(2,2)

pk = PhotoImage(file = r"pk.png")
pk1 = pk.subsample(2,2)

pl = PhotoImage(file = r"pl.png")
pl1 = pl.subsample(2,2)

qa = PhotoImage(file = r"qa.png")
qa1 = qa.subsample(2,2)

ru = PhotoImage(file = r"ru1.png")
ru1 = ru.subsample(2,2)

sa = PhotoImage(file = r"sa.png")
sa1 = sa.subsample(2,2)

sg = PhotoImage(file = r"sg.png")
sg1 = sg.subsample(2,2)

sk = PhotoImage(file = r"sk.png")
sk1 = sk.subsample(2,2)

sr = PhotoImage(file = r"sr.png")
sr1 = sr.subsample(2,2)

sy = PhotoImage(file = r"sy.png")
sy1 = sy.subsample(2,2)

th = PhotoImage(file = r"th.png")
th1 = th.subsample(2,2)

tj = PhotoImage(file = r"tj.png")
tj1 = tj.subsample(2,2)

tr = PhotoImage(file = r"tr.png")
tr1 = tr.subsample(2,2)

turk = PhotoImage(file = r"turk.png")
turk1 = turk.subsample(2,2)

tw = PhotoImage(file = r"tw.png")
tw1 = tw.subsample(2,2)

uae = PhotoImage(file = r"uae.png")
uae1 = uae.subsample(2,2)

uz = PhotoImage(file = r"uz.png")
uz1 = uz.subsample(2,2)
#Europe
al = PhotoImage(file = r"al.png")
al1 = al.subsample(2,2)

aus = PhotoImage(file = r"aus.png")
aus1 = aus.subsample(2,2)

bl = PhotoImage(file = r"bl.png")
bl1 = bl.subsample(2,2)

bgh = PhotoImage(file = r"bgh.png")
bgh1 = bgh.subsample(2,2)

cr = PhotoImage(file = r"cr.png")
cr1 = cr.subsample(2,2)

cz = PhotoImage(file = r"cz.png")
cz1 = cz.subsample(2,2)

cz = PhotoImage(file = r"cz.png")
cz1 = cz.subsample(2,2)

dn = PhotoImage(file = r"dn.png")
dn1 = dn.subsample(2,2)

es = PhotoImage(file = r"es.png")
es1 = es.subsample(2,2)

fl = PhotoImage(file = r"fl.png")
fl1 = fl.subsample(2,2)

fr = PhotoImage(file = r"fr.png")
fr1 = fr.subsample(2,2)

gr = PhotoImage(file = r"gr.png")
gr1 = gr.subsample(2,2)

gre = PhotoImage(file = r"gre.png")
gre1 = gre.subsample(2,2)

hu = PhotoImage(file = r"hu.png")
hu1 = hu.subsample(2,2)

ic = PhotoImage(file = r"ic.png")
ic1 = ic.subsample(2,2)

irland = PhotoImage(file = r"irland.png")
irland1 = irland.subsample(2,2)

it = PhotoImage(file = r"it.png")
it1 = it.subsample(2,2)

lt = PhotoImage(file = r"lt.png")
lt1 = lt.subsample(2,2)

lit = PhotoImage(file = r"lit.png")
lit1 = lit.subsample(2,2)

lx = PhotoImage(file = r"lx.png")
lx1 = lx.subsample(2,2)

mn = PhotoImage(file = r"mn.png")
mn1 = mn.subsample(2,2)

nth = PhotoImage(file = r"nth.png")
nth1 = nth.subsample(2,2)

nr = PhotoImage(file = r"nr.png")
nr1 = nr.subsample(2,2)

pld = PhotoImage(file = r"pld.png")
pld1 = pld.subsample(2,2)

prl = PhotoImage(file = r"prl.png")
prl1 = prl.subsample(2,2)

rom = PhotoImage(file = r"rom.png")
rom1 = rom.subsample(2,2)

sl = PhotoImage(file = r"sl.png")
sl1 = sl.subsample(2,2)

sp = PhotoImage(file = r"sp.png")
sp1 = sp.subsample(2,2)

swe = PhotoImage(file = r"swe.png")
swe1 = swe.subsample(2,2)

swis = PhotoImage(file = r"swis.png")
swis1 = swis.subsample(2,2)

ukr = PhotoImage(file = r"ukr.png")
ukr1 = ukr.subsample(2,2)

uk = PhotoImage(file = r"uk.png")
uk1 = uk.subsample(2,2)

ctact = PhotoImage(file = r"ctact.png")
ctact1 = ctact.subsample(2,2)


#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________

bg = "SteelBlue1"
re = "flat"
#My Buttons
tk.Label(frame, text = "Country Guide",bg='Sky blue',fg='white' ,font=('Times', '28', 'italic', 'bold')).grid(row=0)
tk.Label(frame, text = "Asian Countries ",bg='Sky blue',fg='white', font=('gill sans mt', '15')).grid(row=1,column=0, sticky = "W")
tk.Button(frame, image = afg1, command = afginfo,relief=str(re), bg= str(bg)).grid(row=2 , pady = 5)
tk.Button(frame, image = azer1, command = azinfo,relief=str(re), bg= str(bg) ).grid(row = 3 , pady = 5)
tk.Button(frame, image = bang1 , command=bginfo,relief=str(re), bg= str(bg)).grid(row = 4, pady = 5)
tk.Button(frame, image = bah1, command =bhinfo ,relief=str(re), bg= str(bg)).grid(row = 5, pady = 5)
tk.Button(frame, image = china1, command = chinfo,relief=str(re), bg= str(bg)).grid(row = 6, pady= 5)
tk.Button(frame, image = cyprus1, command = cypinfo,relief=str(re), bg= str(bg)).grid(row = 7, pady= 5)
tk.Button(frame, image = india1,relief=str(re), bg= str(bg), command = indinfo).grid(row = 8, pady= 5)
tk.Button(frame, image = indo1,relief=str(re), bg= str(bg), command=indoinfo).grid(row = 9, pady= 5)
tk.Button(frame, image = iran1,relief=str(re), bg= str(bg),command= irinfo).grid(row = 10, pady= 5)
tk.Button(frame, image = iraq1,relief=str(re), bg= str(bg),command=iqinfo).grid(row = 11, pady= 5)
tk.Button(frame, image = israel1,relief=str(re), bg= str(bg),command= isinfo).grid(row = 12, pady= 5)
tk.Button(frame, image = Japan1,relief=str(re), bg= str(bg),command=jinfo ).grid(row = 13, pady= 5)
tk.Button(frame, image = kaz1,relief=str(re), bg= str(bg),command=kzinfo ).grid(row = 14, pady= 5)
tk.Button(frame, image = kw1,relief=str(re), bg= str(bg),command=kuinfo ).grid(row = 16, pady= 5)
tk.Button(frame, image = ky1,relief=str(re), bg= str(bg),command= kyinfo).grid(row = 17, pady= 5)
tk.Button(frame, image = Leb1,relief=str(re), bg= str(bg),command= linfo).grid(row = 18, pady= 5)
tk.Button(frame, image = mal1,relief=str(re), bg= str(bg),command=mlinfo).grid(row = 19, pady= 5)
tk.Button(frame, image = mald1,relief=str(re),bg= str(bg), command=mdinfo).grid(row = 20, pady= 5)
tk.Button(frame, image = myn1,relief=str(re), bg= str(bg),command= myinfo).grid(row = 21, pady= 5)
tk.Button(frame, image = ne1,relief=str(re), bg= str(bg), command= ninfo ).grid(row = 22, pady= 5)
tk.Button(frame, image = nk1,relief=str(re), bg= str(bg), command=nkinfo).grid(row = 23, pady= 5)
tk.Button(frame, image = om1,relief=str(re), bg= str(bg), command=oinfo).grid(row = 24, pady= 5)
tk.Button(frame, image = ph1,relief=str(re), bg= str(bg), command= phinfo ).grid(row = 25, pady= 5)
tk.Button(frame, image = pk1,relief=str(re), bg= str(bg), command = pkinfo).grid(row = 26, pady= 5)
tk.Button(frame, image = pl1,relief=str(re), bg= str(bg), command=plinfo).grid(row = 27, pady= 5)
tk.Button(frame, image = qa1,relief=str(re), bg= str(bg), command= qinfo).grid(row = 28, pady= 5)
tk.Button(frame, image = ru1,relief=str(re), bg= str(bg), command= rinfo).grid(row = 29, pady= 5)
tk.Button(frame, image = sa1,relief=str(re), bg= str(bg), command = sainfo).grid(row = 30, pady= 5)
tk.Button(frame, image = sg1,relief=str(re), bg= str(bg), command = siinfo).grid(row = 31, pady= 5)
tk.Button(frame, image = sr1,relief=str(re), bg= str(bg), command = srinfo).grid(row = 32, pady= 5)
tk.Button(frame, image = sy1,relief=str(re), bg= str(bg), command =syinfo).grid(row = 33, pady= 5)
tk.Button(frame, image = sk1,relief=str(re), bg= str(bg), command =syinfo).grid(row = 34, pady= 5)
tk.Button(frame, image = th1,relief=str(re), bg= str(bg), command= thinfo).grid(row = 35, pady= 5)
tk.Button(frame, image = tj1,relief=str(re), bg= str(bg), command = tajinfo).grid(row = 36, pady= 5)
tk.Button(frame, image = tr1,relief=str(re), bg= str(bg), command = turkinfo).grid(row = 37, pady= 5)
tk.Button(frame, image = turk1,relief=str(re),bg= str(bg),command = turkinfo).grid(row = 38, pady= 5)
tk.Button(frame, image = tw1,relief=str(re), bg= str(bg), command= taiinfo).grid(row = 39, pady= 5)
tk.Button(frame, image = uae1,relief=str(re), bg= str(bg),command = uinfo).grid(row = 40, pady= 5)
tk.Button(frame, image = uz1,relief=str(re), bg= str(bg) ,command = uzinfo).grid(row = 41, pady= 5)
#European Countries
tk.Label(frame, text = "European Countries ",bg='Sky blue',fg='white',font=('gill sans mt', '15')).grid(row=42,column=0, sticky = "W")
tk.Button(frame, image = al1,relief=str(re), bg= str(bg),command=albinfo).grid(row = 43, pady= 5)
tk.Button(frame, image = aus1,relief=str(re), bg= str(bg),command=ausinfo ).grid(row = 44, pady= 5)
tk.Button(frame, image = bl1,relief=str(re), bg= str(bg) , command=belinfo).grid(row = 45, pady= 5)
tk.Button(frame, image = bgh1,relief=str(re), bg= str(bg),command=bulinfo ).grid(row = 46, pady= 5)
tk.Button(frame, image = cr1,relief=str(re), bg= str(bg),command=croinfo ).grid(row = 47, pady= 5)
tk.Button(frame, image = cz1,relief=str(re), bg= str(bg), command=czinfo ).grid(row = 48, pady= 5)
tk.Button(frame, image = dn1,relief=str(re), bg= str(bg) , command= deninfo).grid(row = 49, pady= 5)
tk.Button(frame, image = es1,relief=str(re), bg= str(bg), command=estinfo ).grid(row = 50, pady= 5)
tk.Button(frame, image = fl1,relief=str(re), bg= str(bg),command=fininfo ).grid(row = 51, pady= 5)
tk.Button(frame, image = fr1,relief=str(re), bg= str(bg),command=frinfo ).grid(row = 52, pady= 5)
tk.Button(frame, image = gr1,relief=str(re), bg= str(bg),command=grinfo ).grid(row = 53, pady= 5)
tk.Button(frame, image = gre1,relief=str(re), bg= str(bg),command=greinfo ).grid(row = 54, pady= 5)
tk.Button(frame, image = hu1,relief=str(re), bg= str(bg),command=huinfo ).grid(row = 55, pady= 5)
tk.Button(frame, image = ic1,relief=str(re), bg= str(bg),command=icinfo ).grid(row = 56, pady= 5)
tk.Button(frame, image = irland1,relief=str(re), bg= str(bg),command=irlinfo ).grid(row = 57, pady= 5)
tk.Button(frame, image = it1,relief=str(re), bg= str(bg),command=itinfo ).grid(row = 58, pady= 5)
tk.Button(frame, image = lit1,relief=str(re), bg= str(bg),command=litinfo ).grid(row = 59, pady= 5)
tk.Button(frame, image = lx1,relief=str(re), bg= str(bg),command=luxinfo ).grid(row = 60, pady= 5)
tk.Button(frame, image = mn1,relief=str(re), bg= str(bg) , command=moinfo).grid(row = 61, pady= 5)
tk.Button(frame, image = nth1,relief=str(re), bg= str(bg),command=netinfo ).grid(row = 62, pady= 5)
tk.Button(frame, image = nr1,relief=str(re), bg= str(bg),command=norinfo ).grid(row = 63, pady= 5)
tk.Button(frame, image = pld1,relief=str(re), bg= str(bg),command=polinfo ).grid(row = 64, pady= 5)
tk.Button(frame, image = prl1,relief=str(re), bg= str(bg),command=portinfo ).grid(row = 65, pady= 5)
tk.Button(frame, image = rom1,relief=str(re), bg= str(bg),command=roinfo ).grid(row = 66, pady= 5)
tk.Button(frame, image = sl1,relief=str(re), bg= str(bg),command=sloinfo ).grid(row = 67, pady= 5)
tk.Button(frame, image = sp1,relief=str(re), bg= str(bg),command=spinfo ).grid(row = 68, pady= 5)
tk.Button(frame, image = swe1,relief=str(re), bg= str(bg),command=swinfo ).grid(row = 69, pady= 5)
tk.Button(frame, image = swis1,relief=str(re), bg= str(bg),command=switinfo ).grid(row = 70, pady= 5)
tk.Button(frame, image = ukr1,relief=str(re), bg= str(bg),command=ukrinfo ).grid(row = 71, pady= 5)
tk.Button(frame, image = uk1,relief=str(re), bg= str(bg),command=ukinfo ).grid(row = 72, pady= 5)
tk.Button(frame, image = ctact1,relief=str(re), bg= str(bg),command=contact ).grid(row = 73, pady= 5)









canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')



#______________________________________________________________________________________________________________________

#----------------------------------------------------------------------------------------------------------------------
#______________________________________________________________________________________________________________________





main_window.mainloop()
