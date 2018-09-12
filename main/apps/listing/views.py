from django.shortcuts import render, redirect
from apps.listing.models import *

def newListing(request):    
    if request.method == 'POST':
        errors = {}
        fields = ['name', 'city', 'state', 'maxguests', 'beds', 'bedrooms', 'bathrooms',
            'description', 'price']
        for field in fields:
            if field in request.POST:
                if request.POST[field]=='':
                    errors[field]="Cannot be blank"
                else:
                    pass
            else:
                errors[field]="Need to be filled"

        if len(errors)>0:
            print(errors)
            context = {
                "errors": errors
            }
            print("\n\n-------------------")
            print(context)
            return redirect("hub:becomeHost")

        print("\n\n-------------------")
        print(request.POST)

    this_listing = Listing.objects.add_listing(request.POST)
    for i in range(1, 12):
        name = "amenities"
        name = name + str(i)
        if name in request.POST:
            print(name)
            this_amenity = Amenity.objects.get(id=i) 
            this_listing.amenities.add(this_amenity)

    return redirect("hub:profile")

def home(request):
    return render(request, "hub/dashboard.html")

def newAmenity(request):
    array = ["Kitchen", "Patio or Balcony", "Free Parking", "Washer/Dryer", "Wifi", "TV", "Private Entrance", "Air Conditioning", "Outdorr Grill", "Coffee Maker", "Fireplace"]
    for item in array:
        Amenity.objects.create(name=item)
    return redirect("hub:profile")

def update(request, listing_id):
    handle_uploaded_file(request.FILES['newimg'], str(request.FILES['newimg']))
    listing = Listing.objects.get(id=listing_id)
    listing.photos = str(request.FILES['newimg'])
    listing.save()
    return redirect("hub:profile")

def review(request, listing_id):
    data = request.POST
    listing = Listing.objects.get(id=listing_id)
    user = User.objects.get(id=request.session['data']['id'])
    this_review = Reviews.objects.create(title=data['title'], content=data['content'], listing=listing, user=user, rating=int(data['rating']))
    this_review.save()

  
    total, count = 0, 0
    for review in listing.reviews.all():
        total += review.rating
        count += 1
    
    listing.rating = total / count
    listing.save()

    return redirect("/{}/listingdetails/".format(listing_id))