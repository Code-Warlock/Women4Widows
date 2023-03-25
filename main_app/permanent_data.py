data = {
    "name_main": "Conversation in Action",
    "name_secondary": "Women4Widows Initiative",
    "goals" : [
        {"text": "Supporting local widows to become productive in the community through economic empowerment", "image" : "widows.jpg"},
        {"text" : "Reimaging the role of widows in the local communities", "image" : "widow5_with_fam.jpg"}, 
        {"text" : "helping widows to be self-sufficient", "image":"bags.jpg" }
               ]
}
vision = """
    Widows in Nigeria live on the absolute fringe of society. They are often denied inheritance rights and have their property taken after the death of a partner.  With most having no education, they labor for a couple of dollars per day, not near enough to feed their children.  Since they are widowed, they are often abused socially, and many physically, by members of their community.  Sunrise for Rural Dwellers, a 501c3, organized by Fr. Tony Okolo, has embarked on a path to empower widows, and give these women a path towards dignity and a better life. 
 
Sunrise for Rural Dwellers is working towards empowering these women by funding a farm.  Our goal is two-fold:  provide sustenance for the widows and their families and provide a revenue source for them through the agricultural surplus from the farm. Therefore, this investment in the widows, lifts their families, Nigeria, and all of society.
 
Our organization has designated a plot of land for the farm and funded the initial clearing of the land and the seeds and roots needed to begin planting.  We are seeking ongoing support for the farm.  This includes annual seeds, farming tools, and expansion opportunities.
"""
widows_url = []
for num in range(1,17):
    if num == 5:
        continue
    widows_url.append("widow"+str(num))