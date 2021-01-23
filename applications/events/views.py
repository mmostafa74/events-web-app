from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

from applications.events.models import Event
from applications.events.forms import SearchForm, EventForm


@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.slug = slugify(event.title)
            event.author = request.user
            form.save()
            return redirect("events:event_list")
    else:
        form = EventForm()
    return render(request, "events/add_event.html", {"form": form})


@login_required
def edit_event(request, event):
    event_details = get_object_or_404(Event, slug=event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event_details)
        if form.is_valid():
            event_details = form.save(commit=False)
            event_details.author = request.user
            form.save()
            return redirect("events:event_list")
    else:
        form = EventForm(instance=event_details)
    return render(request, "events/edit_event.html", {"form": form})


@login_required
def delete_event(request, event):
    event_details = get_object_or_404(Event, slug=event)
    event_details.delete()
    return render("events:event_list")


def event_list(request):
    objects = Event.objects.all()
    paginator = Paginator(objects, 5)
    page = request.GET.get("page")
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, "events/list.html", {"page": page, "events": events})


def event_detail(request, event):
    event = get_object_or_404(Event, slug=event)

    return render(request, "events/detail.html", {"event": event})


def event_search(request):
    form = SearchForm()
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Event.objects.annotate(
                search=SearchVector("title", "description")
            ).filter(search=query)
    return render(
        request,
        "events/search.html",
        {"form": form, "query": query, "results": results},
    )
