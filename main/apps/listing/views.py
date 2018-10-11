from django.shortcuts import render, redirect
from apps.listing.models import *
from random import randint

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

    this_listing = Listing.objects.add_listing(request.POST)
    for i in range(1, 12):
        name = "amenities"
        name = name + str(i)
        if name in request.POST:
            this_amenity = Amenity.objects.get(id=i) 
            this_listing.amenities.add(this_amenity)

    return redirect("hub:profile")

def home(request):
    return render(request, "hub/dashboard.html")

def updatepic(request, listing_id):
    handle_uploaded_file(request.FILES['newimg'], str(request.FILES['newimg']))
    listing = Listing.objects.get(id=listing_id)
    listing.main_photo = str(request.FILES['newimg'])
    listing.save() 
    return redirect("/{}/userListingProfile/".format(listing_id))

def delete(request, listing_id):
    # delete listing 
    # delete amenity connections to listing
    return redirect("hub:profile")


# ----------------------------- dev tools - fill random data --------------------------------#


name_list = [
    "Hip and Cozy In-town King Studio", 
    "Cozy Private Loft Apt with Balcony", 
    "Walk to Restaurants from Your Front Door", 
    "Spend Evenings Barbecuing with a city View", 
    "Peaceful Apartment with a Lush, Zen-Like Garden", 
    "Comfortable spot Near City/Airport", 
    "5 Star Place Right in the Middle of Everything.", 
    "Amazing Spacious Apartment with a View.", 
    "#3 Urban Warehouse Loft in Deep Ellum"]
desc_list = [
    "Escape the bustle of the city and relax in a cozy backyard sanctuary. Sample local craft beer in an Adirondack chair in the garden, and switch on a heat lamp when it gets chilly. Watch a widescreen TV from the bed and make espresso in the morning.", 
    "Escape to where comfort meets convenience. Centrally located near shopping & restaurants. Only 7 miles to downtown. Fresh 1 bdrm / 1 bath condo style flat, with full kitchen, living and bedroom areas, along with a beautiful pool. Access to public transportation. Easy commute to airport.", 
    "An exquisite, handcrafted home, blending Bauhaus contemporary with warm rustic elegance, in a secluded setting with running brook and shimmering light filtered through countless Japanese Maples. Winding gravel foot paths through a forested canopy lead to the foot bridge traversing Ash Creek on to the Treehouse entry. Tucked away in the heart of Little Forest Hills, this timeless, private property is truly extraordinary.",
    "Adorable guest cottage in the heart of town. Near the lake, Arts District, Convention Center & AT&T Center. Serene & safe setting for couples, business travelers, and extended stay. Accommodates a single guest or couple. Private entrance. PLEASE review ALL guest rules. Not suitable for children. NO smoking inside or outside the cottage. Confirmation of reservation conveys acceptance of rules.", 
    "Elegant studio in Uptown's premier historic building – one time home to Judy Garland, Dean Martin and Zsa Zsa Gabor.My place is good for couples, solo adventurers, business travelers, families (with kids), and furry friends (pets).", 
    "Private warehouse loft with stained concrete floors, brick & block walls, custom kitchen & bath, 8.5ft window, 3 skylights & 10' to 15' ceilings. Off-street parking in the heart of the warehouse district - walk to music, art, dining, clubs. No Parties. Management lives on site. Neighbors are watchful.", 
    "My place is close to art and culture, great views, family-friendly activities, and all types of bars and dining. You’ll love my place because of the kitchen, the coziness, the high ceilings, the views, and the location. My place is good for couples, solo adventurers, and business travelers." ]
amenity_list = [
    "Kitchen", "Patio or Balcony", "Free Parking", "Washer/Dryer", "Wifi", "TV", "Private Entrance", "Air Conditioning", "Outdorr Grill", "Coffee Maker", "Fireplace"]
listing_type_list = ["ENITRE PLACE", "PRIVATE ROOM", "SHARED ROOM"] 
city_list = ["Dallas", "Seattle", "New York", "Los Angeles", "Chicago", "Miami", "Denver", "Nashville", "Atlanta", "New Orleans",  "Boston", "San Jose", "Austin", "Houston", "Louisville", "Richmond", "Pittsburg", "St. louis", "St. Paul", "Baltimore", "Hartford", "Portland"]
state_list = ["TX", "WA", "NY", "CA", "IL", "FL", "CO", "TN", "GA", "LA", "MA", "CA", "TX", "TX", "KY", "VA", "PA", "MO", "MN", "MD", "CT", "OR"]
reveiws_list = [
    "This Lodging option was better than I expected. Everything was very easy to understand and my stay was smooth. The location is fantastic and one can walk to places to eat and drink. I will stay there again.", 
    "The place is pleasant place to cool your heels after a busy day in downtown. The neighborhood is quiet and there is enough privacy for you to chill for an evening. I will stay there again if the opportunity arises.", "My host was great and very prompt to reply to any questions that we had.  The cottage is an oasis of relaxation and the next time we return to the area we'll definitely try and stay there again.", 
    "Great location and excellently designed space. Loved how functional and comfortable they had made the small space. We were able to walk to a couple of the host's local recommendations and both were great!", 
    "Great place with great people. Has all the things you need to make it feel like a home away from home", "Super comfortable, great backyard patio, awesome neighborhood!!", 
    "We could not have asked for a better host, and along with the delicious weather, we had the most comfortable, cozy and delightful place to stay. Highly recommend!", 
    "This Air Bnb was the perfect place for me to stay on my solo trip! The town was so beautiful, lots to do around there and walkable! It was also very close to downtown which was great because I used uber while I was visiting. I would definitely recommend this to anyone wanting a homey vibe while on vacation!", 
    "I loved staying at the this place. I was able to walk to the nearby yoga studio, restaurants, shops, etc. The cottage felt very private and had everything I needed to make my stay enjoyable.", 
    "I only stayed for one night on a quick trip but I hope to return again! The cottage had everything I needed, a very comfortable bed, and a great outdoor space. Coffee and restaurants were just around the corner.", 
    "I loved the little place. It was warm and cozy and had everything you would want for an extended stay. I was right in town, where I wanted to be, and it was easy to walk, drive, or Lyft where I needed to go. What a fantastic host! Very quick to respond and checked in with me during my stay. Thanks!",
    "My first venture using Airbnb lead me to an amazing place. I found the owner very accommodating and very quick to respond to our spontaneous request. The location is walking distance to restaurants and shops. The place exceeded our needs. Cute, clean, and perfect location.", 
    "This condo has a great location with ski in ski out access and a close walk to town. The beds were not terribly comfortable for me, my husband slept ok but I need a firm bed and the main bed was very very soft so beware.  There is a nice view of aspen trees but no balcony etc. So if you are looking for an alternative to a hotel then a good find.", 
    "Truly wonderful spot for a couples getaway! Perfect location between town and the outdoors. Ten minute walk to downtown and a hiking trail right out the side door. Very clean and has great hot tubs/ spa on the property. Would certainly stay here again!", 
    "Just as described! Perfect little studio, clean, and great location. Wish the weather would have been a notch cooler for us, as AC’s are not a thing in the mountains :) great place!", 
    "Terrific location. Great hike right outside building. Cozy stay!", 
    "Perfect spot for a quiet getaway. A half mile from downtown. Garage for vehicle. Worth it. We will return.", 
    "The location was amazing! At the steps of everything. The apartment was comfortable for the two of us, we had everything we needed for a great weekend. The bed was super comfortable, and with the bedding it was really warm despite it being 9 degrees outside!", 
    "Jack and Jerrod were very helpful! This studio was perfect for our 2 days of skiing at skiing! Location is excellent, across the street from Peak 9 lift, and within blocks of everything you need to walk to. We did not use our car once after arriving. Very comfy." ]

def fillamenities(request): 
    for item in amenity_list:
        Amenity.objects.create(name=item)
    return redirect("hub:profile")

def filllistings(request):
    user_list = User.objects.all()
    for user in user_list: 
        rand_location = randint(0, 11)
        main_image = "h" + str(randint(1,20)) + ".jpg"
        listing_1 = {
            "name": name_list[randint(0, 8)],
            "homeType": listing_type_list[randint(0,2)],
            "maxguests": randint(2, 9),
            "bedrooms": randint(1, 4),
            "beds": randint(1, 5),
            "bathrooms": randint(1, 4),
            "description": desc_list[randint(0, 6)],
            "city": city_list[rand_location],
            "state": state_list[rand_location],
            "price": randint(45, 150),
            "host": user.id,
            "main_photo": main_image 
        } 
        this_listing = Listing.objects.filling_listings(listing_1)
        rand_amenity = [1, randint(2,4), 5, randint(6,7), randint(8,9), randint(10,11)]
        for i in rand_amenity:
            this_amenity = Amenity.objects.get(id=i) 
            this_listing.amenities.add(this_amenity)              
    return redirect("hub:profile")



    