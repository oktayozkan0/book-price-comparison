from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SearchForm
from .utils import sort_by_value, async_request
import asyncio

class SearchView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        context = {
            "form":form
        }
        return render(request, "main.html", context)

    def post(self, request, *args, **kwargs):
        print("post data")
        form = SearchForm(request.POST)
        websites = request.POST.getlist("websites")
        q = request.POST.get("query")
        if len(websites) < 1:
            return redirect("/")
        if form.is_valid():
            raw_data =  asyncio.run(async_request(websites=websites, q=q))
            print("hello im rawdata")
            print(raw_data)
            data = [data["items"] for data in raw_data]
            print(data)
        else:
            form = SearchForm()
        print(data)
        data = sort_by_value(data)
        
        context = {"context":data[1:], "cheapest":data[0], "query":q}

        return render(request, "books.html", context)
