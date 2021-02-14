from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movies, Tvshows, Comingsoon, Episodes
from django.core.mail import send_mail, send_mass_mail
import random
# Create your views here.


allgenres = [
    "Comedy",
    "Action",
    "Drama",
    "Sci-fi",
    "Fantasy",
    "Crime",
    "Netflix",
    "Adventure",
    "Romance",
    "Anime",
    "Horror",
    "Teen",
    "Thriller",
    "Mystery",
    "Superhero",
    "Family",
    
]
alltvgenres = [
    "Action",
    "Adventure",
    "Anime",
    "Comedy",
    "Crime",
    "Drama",
    "Fantasy",
    "Horror",
    "Netflix",
    "Mystery",
    "Romance",
    "Sitcom",
    "Superhero",
    "Sci-fi",
    "Thriller",
    "Teen"
]

def handler404(request, exception):
    # Search bar POST method
    if request.method == "POST":
        search_var = request.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)
    return render(request, 'main/404.html', {"genres":allgenres})

def home(response):
    m = Movies.objects.all()
    t = Tvshows.objects.all()

    randomnumber = random.randrange(0, 14)
    randommoviegenre = allgenres[randomnumber]
    randomtvgenre = alltvgenres[randomnumber]

    latest_movies = Movies.objects.filter(category="Movie").order_by('-id')[:18]

    latest_tvshows = Tvshows.objects.filter(category="Tv Serie").order_by('-id')[:18]

    auto_movies = Movies.objects.filter(category="Movie").order_by('-id')[18:36]

    auto_tvshows = Tvshows.objects.filter(category="Tv Serie").order_by('-id')[18:36]

    #topmovies
    def last(n): 
        return n[num]   
   
 
    def sort(tuples):  
        return sorted(tuples, key = last) 
    viewslist = []
    num = 1
    for item in Movies.objects.all():
        viewslist.append((item.name, item.views))

    sortlist = sort(viewslist)
    sortlist.reverse()
    nonamelist = []
    for sortlist_item in sortlist:
        nonamelist.append(sortlist_item[0])

    # Search bar POST method
    if response.method == "POST":
        if response.POST.get("search"):
            search_var = response.POST.get("search")
            return HttpResponseRedirect("/%s" %search_var)


    return render(response, "main/index.html", 
    {"m":m,"t":t, "latest_movies":latest_movies, "latest_tvshows":latest_tvshows, "auto_movies":auto_movies,
    "auto_tvshows":auto_tvshows, "genres":allgenres, "movie_genres":m, "random_movie_genre":randommoviegenre,
    "random_tv_genre":randomtvgenre, "top_rated_movies":m, "top_rated_tvshows":t,
    "comingsoon":Comingsoon.objects.all().order_by('-id'), "sortlist":nonamelist[:10], "series_episodes":Episodes.objects.all(),
    "moviepopup":Movies.objects.all(), "tvseriepopup":Tvshows.objects.all(),})



def search(response, search):
    moviesearchresults = []
    testresults = []
    testresults1 = []
    recommendedresults = []
    watchsplit = search.split(" ")
    
    values = Movies.objects.all()
    values4 = Episodes.objects.all()
    values1 = Tvshows.objects.all()
    movie_startwith=Movies.objects.filter(name__startswith=search)
    tvshows=Tvshows.objects.filter(name__startswith=search)
    
    for i_movie_startwith in movie_startwith:
        moviesearchresults.append(i_movie_startwith.name)

    for tvshows_startwith in tvshows:
        moviesearchresults.append(tvshows_startwith.name)
                
    for i in values:
        namesplit = i.name.split(" ")
        for k in namesplit:
            for j in watchsplit:
                if j != "the" and j != "and":
                    if k.lower() == j.lower():
                        moviesearchresults.append(i.name)



    
    for it in values1:
        namesplittv = it.name.split(" ")
        for kt in namesplittv:
            for jt in watchsplit:
                if jt != "the" and jt != "and":
                    if kt.lower() == jt.lower():
                        moviesearchresults.append(it.name)

    

    for item_tv in list(dict.fromkeys(moviesearchresults)):
        for tv in values1:
            if item_tv == tv.name:
                genresplit = tv.genres.split(" ")
                for tv_genre in genresplit:
                    for tv1 in values1:
                        genresplit2 = tv1.genres.split(" ")
                        for tv_genre1 in genresplit2:
                            if tv_genre == tv_genre1:
                                if tv1.name not in moviesearchresults:
                                    recommendedresults.append(tv1.name)



    for item_movie in list(dict.fromkeys(moviesearchresults)):
        for movie in values:
            if item_movie == movie.name:
                genre_moviesplit = movie.genres.split(" ")
                for movie_genre in genre_moviesplit:
                    for movie1 in values:
                        genre_moviesplit2 = movie1.genres.split(" ")
                        for movie_genre1 in genre_moviesplit2:
                            if movie_genre == movie_genre1:
                                if movie1.name not in moviesearchresults:
                                    recommendedresults.append(movie1.name)                                    
    
    


    # Search bar POST method
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)

    return render(response, "main/search.html",
    {"values2":Episodes.objects.all(), "values":Movies.objects.all(), "values1":Tvshows.objects.all(), "genres":allgenres,
    "search":search, "moviesearchresults":list(dict.fromkeys(moviesearchresults)), "recommendedresults":list(dict.fromkeys(recommendedresults)),
    "tvseriepopup":Tvshows.objects.all(), "series_episodes":Episodes.objects.all(), "moviepopup":Movies.objects.all(),})



def watching(response, watching):
    values2 = Episodes.objects.all()
    stopsnextepisode = 0
    stopsnextseason = 0
    presentseason = 0
    presentseason1 = 0
    presentseason2 = 0
    values6 = 0
    for item in values2:
        theone = (
            item.name
            + " season "
            + item.seasons.__str__()
            + " episode "
            + item.episodes.__str__()
        )
        if watching == theone:
            presentseason = int(item.seasons)
            values4 = Episodes.objects.filter(name=item.name, seasons=item.seasons).reverse()
            values5 = Episodes.objects.filter(name=item.name).reverse()
            for values4_item in values4:
                stopsnextepisode = values4_item.episodes
            
            for values5_item in values5:
                stopsnextseason = values5_item.seasons

            if int(item.seasons) > 1:
                presentseason1 = presentseason - 1
                values6 = Episodes.objects.filter(
                    name=item.name, seasons=presentseason1
                ).reverse()
                for values6_item in values6:
                    presentseason2 = values6_item.episodes
    
    for most_watched in Movies.objects.all():
        if most_watched.name == watching:
            most_watched.views = most_watched.views + 1
        most_watched.save()
    
    # Search bar POST method
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)
    return render(response, "main/watching.html", 
    {"values":Movies.objects.all(), "watch":watching, "values1":Episodes.objects.all(),
    "stopsnextepisode":stopsnextepisode, "stopsnextseason":stopsnextseason, "presentseason":presentseason,
    "presentseason1":presentseason2, "genres":allgenres, "test":values6, "test1":presentseason2})


def movies(response):
    # Search bar POST method
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)
    return render(response, "main/movies.html", 
    {"values":Movies.objects.filter(category="Movie").order_by('-id')[:12], 
    "values1":Movies.objects.filter(category="Movie").order_by('-id')[12:24],
    "values2":Movies.objects.filter(category="Movie").order_by('-id')[24:36],
    "values3":Movies.objects.filter(category="Movie").order_by('-id')[36:48],
    "values4":Movies.objects.filter(category="Movie").order_by('-id')[48:60],
    "values5":Movies.objects.filter(category="Movie").order_by('-id')[60:72],
    "values6":Movies.objects.filter(category="Movie").order_by('-id')[72:84],
    "values7":Movies.objects.filter(category="Movie").order_by('-id')[84:96],
    "values8":Movies.objects.filter(category="Movie").order_by('-id')[96:108],
    "values9":Movies.objects.filter(category="Movie").order_by('-id')[108:120], "genres":allgenres, 
    "all_movies":Movies.objects.all()[:120], "moviepopup":Movies.objects.all()})

def tvseries(response):
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)

    return render(response, "main/tvseries.html", 
    {"genres":allgenres, "series_episodes":Episodes.objects.all(), "latest":Tvshows.objects.filter(category="Tv Serie").order_by('-id')[:24], 
    "tvgenres":alltvgenres, "all_tv":Tvshows.objects.all()})

def mostwatched(response):
    #topmovies
    def last(n): 
        return n[num]   
   
 
    def sort(tuples):  
        return sorted(tuples, key = last) 
    viewslist = []
    num = 1
    for item in Movies.objects.all():
        viewslist.append((item.name, item.views))

    sortlist = sort(viewslist)
    sortlist.reverse()
    nonamelist = []
    for sortlist_item in sortlist:
        nonamelist.append(sortlist_item[0])

    # Search bar POST method
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)

    return render(response, "main/mostwatched.html", {"genres":allgenres, "sortlist":nonamelist[:30], "moviepopup":Movies.objects.all()})

def comingsoon(response):
    # Search bar POST method
    if response.method == "POST":
        search_var = response.POST.get("search")
        return HttpResponseRedirect("/%s" %search_var)
    return render(response, "main/comingsoon.html", {"moviesoonlist":Comingsoon.objects.filter(category="Movie").order_by('-id'), "tvseriesoonlist":Comingsoon.objects.filter(category="Tv Serie").order_by('-id'), "genres":allgenres,
    })




def genres(response):
    return render(response, "main/genres.html", {"genres":allgenres, "moviepopup":Movies.objects.all(), "movies":Movies.objects.all().order_by('-id')[:100]})



def tvname(response, tvname):
    error_verify = "False"
    for item in Episodes.objects.all():
        if item.name == tvname:
            last_season = item.seasons
        else:
            last_season = 0
    
    for i in Tvshows.objects.all():
        if i.name == tvname:
            error_verify = "True"

    # Search bar POST method
    if response.method == "POST":
        if response.POST.get("search"):
            search_var = response.POST.get("search")
            return HttpResponseRedirect("/%s" %search_var)
    return render(response, "main/tvname.html", 
    {"tvname":tvname, "series_episodes":Episodes.objects.all(), "last_season":last_season, "tvseries":Tvshows.objects.all(), "genres":allgenres, "error_verify":error_verify})