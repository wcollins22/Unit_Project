from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from app.models import Student
from app.forms import ProfileForm


<<<<<<< Updated upstream
def profile_function(request):
    form = ProfileForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        
=======
def page_view(request):
    context = {
        "students" : {
            "Ethan Ward" : Student("Ethan Ward", "I'm 18 years old. I'm Taken. Favorite Color is Purple", "Dishwasher at Corner Store", "Bruce, MS"),

            "Rylee Chisholm" : Student("Rylee Chisholm", "5'5 and clingy, but thats okay.", "To be 6ft tall.  I did dream once about this really weird fun house with a serial killer dressed as a neon pumpkin.", "Mom"),

            "Asian Markiplier" : Student("Asian Markiplier", "Am Wasian. Am Weeb. Am Saucy Housewife.", "To become best Wasian.", "Pizza Boi", "Hidden Leaf Village"),

            "Daelan" : Student("Daelan", "I have always liked to play video games and I was in band.", "I deliver at Domino's.", "Pontotoc, MS"),

            "RJay Pickering" : Student("RJay Pickering", "I like to play video games and fix broken vehicles.  i use to go to the gym alot and i love working around a farm", "videogame designer", "student/farmer", "Pontotoc, MS"),

            "Randy Trullet" : Student("Randy Trullet", "Oh my days, British Wannabe, Future Application Developer", "I want a house and a dog, that's about it. Also want a computer, that's a priority", "Student", "Corinth, MS"),

            "Sean Ennis": Student("Sean Ennis", "Flying on airplanes makes me nervous.", "Professional Football Player", "Director", "Philadelphia, PA"),

            "Mariann" : Student("Mariann", "I am 18 years old and I enjoy listening to music in my free time along with reading, watching TV, and sleeping. ", "R&B/ Lofi HipHop", "I hope to be a Software engineer with at least a Master's degree in the future and possibly try my in music production. I also want to travel the world in the meantime.", "I am from the small town of Charleston, Mississippi."),

            "Dylan Goad" : Student("Dylan Goad", "Nah", "Minecraft Parodies", "Be a Billionaire", "Unemployed", "Logan Coley's Basement"),

            "Isaac" : Student("Isaac", "I like to make things. I have a lot of creative hobbies. Drawing, Jewelry making, sewing, and playing instruments.", "Rock, Electronic", "I want to be pursue a career in art", "Server at Newk's Eatery", "Oxford"), 

            "Quinton Summerford" : Student("Quinton Summerford", "Blue Pill or Red Pill? |Blue: Blueberry flavor | Red: Infinite Money", "Nightcore", "To defeat the sussy little dragon of Cthulhu", "Discord Admin", "White Plains, NY"),

            "Jacen Barefoot" : Student("Jacen Barefoot", "Skateboarder, RubiksQbSolver, and Aspiring Software Developer", "Anime", "House, Skatepark backyard, wife and kids, and a good job.", "North Carolina"),

            "Ryan Bennett" : Student("Ryan Bennett", "I'm a boring guy who plays video games.", "Classic Country", "Become a video game developer", "Server/Delivery Driver", "Saltillo, Mississippi"),

            "LOGAN T WILKINS" : Student("LOGAN T WILKINS", "I love video games and play a large variety of them my favorites being soul calibur, halo, for honor, skyrim and fallout 4. I enjoy various forms of art as any form of expressing creativity brings me joy, I like to draw, create ships in space engineers, build models in blender, paint, write, make characters in video games, build maps in halo, etc. I also love to spar, as in sword fighting or other weapons fighting and i have practiced many martial arts to improve my sword fighting capability. Some of the martial arts i have studied involve ", "Alternative rock is my top favorite, then there's instrumental, and dubstep... I also like christian rock", "All my life i've wanted a role in creating video game, and it aligns with many of my favorite things to do, how ever I have to one day open a HEMA academy to teach sword play and martial arts", "I currently work at Larsons Cashsaver Water Valley MS", "Memphis")
        }
    }
    return render(request, "page.html", context)
>>>>>>> Stashed changes

        return render(request, "profiles.html", {"form":form, "name":name})
    else:
        return render(request, "profiles.html",)
