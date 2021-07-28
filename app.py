from tkinter import * 
import instaloader
from tkinter.messagebox import showinfo

win = Tk()
win.config(bg="#FDEDEC")
win.iconbitmap('pink.ico')
win.geometry('520x240')
win.title('Ig-Info') 


          
def followers():
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, 'Put your Ig-Username here!') #Put your ig-username here!
    Lbl0= Label(win, text=type(profile),bg="black",fg="white")
    Lbl0.place(x=220,y=40)

    Lbl1 = Label(win,text=("Number of Posts: ", profile.mediacount),bg="black",fg="white")
    Lbl1.place(x=220,y=60)

    Lbl2 =Label(win,text=("Followers: ", profile.followers),bg="black",fg="white")
    Lbl2.place(x=220,y=80)
            
    Lbl3 = Label(win,text=("Followees: ", profile.followees),bg="black",fg="white")
    Lbl3.place(x=220,y=100)

    Lbl4 = Label(win,text=("Bio: ", profile.biography,profile.external_url),bg="black",fg="white")           
    Lbl4.place(x=220,y=120)
    

def posts():
    L = instaloader.Instaloader()


    for post in instaloader.Hashtag.from_name(L.context, 'Put your Ig-Username here!').get_posts(): #put your ig-username here
        show = Label(win,text=L.download_post(post, target='Put your Ig-Username here!')) #add hastag to create a folder of your ig-username
        show.pack()

        showinfo("Done!!")


def pic():
    ob=instaloader.Instaloader()
    user=input("Enter Username:")
    ob.download_profile(user,profile_pic_only=True)
    showinfo("Done!")

 
 
lbl = Label(win,text="Ig-profile-Info",font=('Verdana 15'),bg="black",fg="white")
lbl.place(x=50,y=40)

btn = Button(win,text="Scrape",font=('roboto 10 bold'),bg="#0B5345",fg="white",command=posts)
btn.place(x=50,y=80)


btn = Button(win,text="Pull",font=('roboto 10 bold'),bg="#0B5345",fg="white",command=followers)
btn.place(x=50,y=120)

btn = Button(win,text="Profile",font=('roboto 10 bold'),bg="#0B5345",fg="white",command=pic)
btn.place(x=50,y=160)


btn = Button(win,text="Exit",font=('roboto 10 bold'),bg="#0B5345",fg="white",command=win.destroy)
btn.place(x=50,y=200)

win.mainloop()
