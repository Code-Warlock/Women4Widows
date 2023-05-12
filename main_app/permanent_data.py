
data = {
    "name_main": "Conversation in Action",
    "name_secondary": "Women4Widows Initiative",
    "goals": [
        {"text": "Supporting local widows to become productive in the community through economic empowerment",
            "image": "widows.jpg"},
        {"text": "Reimaging the role of widows in the local communities",
            "image": "widow5_with_fam.jpg"},
        {"text": "helping widows to be self-sufficient", "image": "bags.jpg"}
    ]
}
vision = """
    Widows in Nigeria live on the absolute fringe of society. They are often denied inheritance rights and have their property taken after the death of a partner.  With most having no education, they labor for a couple of dollars per day, not near enough to feed their children.  Since they are widowed, they are often abused socially, and many physically, by members of their community.  Sunrise for Rural Dwellers, a 501c3, organized by Fr. Tony Okolo, has embarked on a path to empower widows, and give these women a path towards dignity and a better life. 
 
Sunrise for Rural Dwellers is working towards empowering these women by funding a farm.  Our goal is two-fold:  provide sustenance for the widows and their families and provide a revenue source for them through the agricultural surplus from the farm. Therefore, this investment in the widows, lifts their families, Nigeria, and all of society.
 
Our organization has designated a plot of land for the farm and funded the initial clearing of the land and the seeds and roots needed to begin planting.  We are seeking ongoing support for the farm.  This includes annual seeds, farming tools, and expansion opportunities.
"""
widows_url = []
for num in range(1, 17):
    if num == 5:
        continue
    widows_url.append("widow"+str(num))


_projects = [
    {
        "slug" : "uvuru-widows-empowerment",
        "title": "Uvuru Women Empowerment",
        "imageurl" : "main_app/images/smiling_widows.jpg",
        "imageurl2" : "main_app/images/women_sharing.jpg",
        "description": "Widows are most times the breadwinners of their families and therefore require assistance in reducing the heavy financial burdens they carry. They need skill acquisition, long term support and income generating activities",
        "excerpts": "Supporting local widows to become productive in the community through economic empowerment.",
        "date": "23 Jun",
        "start" : "9am",
        "end" : "2pm",
        "venue" : "Uvuru",
        "organiser" : "Fr Tony Okolo",
        "location": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63397.113100071125!2d7.154418241776304!3d6.730809716802797!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1044f379dc323ae7%3A0xbacf2d2d05a07129!2sUVURU!5e0!3m2!1sen!2sng!4v1682089230421!5m2!1sen!2sng",
        "activities": {
            "desc": "There a great need to empower these rural widows to become self-sufficient to work in the agricultural sector with access to finance, knowledge and trainings which will enable them have sustainable livelihoods through farming, guarantying food security for their children.",
            "list": ["Assisting widow consultants in farming", "Share best practices and knowledge.", "Assisting widow consultants in farming", "Collaborate with technology, informations security, and business partners", "Find and address performance issues."]
            },
        "vision" : "Our vision is to assist widows by providing them with trainings and the follow-ups required for them to succeed in their chosen trade or profession medical outreach designed to enable widows to know their health status and at the same time issue medical advice that will support their well-being",
        "mission" : "Our mission is to empower widows in Africa by providing them with the resources, education, and support they need to achieve financial stability and independence. We believe that widows are one of the most vulnerable and marginalized groups in Africa, facing discrimination and hardship due to social and cultural norms"
    },
    {
        "slug" : "sunrise-medical-outreach",
        "title": "Free medical outreach",
        "imageurl" : "main_app/images/gathering.jpg",
        "imageurl2" : "main_app/images/outreach/queueing.jpg",
        "moreimages" : ["main_app/images/outreach/equipment.jpg","main_app/images/outreach/equipments.jpg"],
        "description": "Free medical outreach in Uvuru Community, Uzo Uwani LGA, Enugu state, Nigeria was successfully hosted by Sunrise for Rural Dwellers.  This event took place on the 18th of August 2019 from 9 am – 7 pm at the Community Primary School, Uvuru. Over 500 people with different ailments benefited from the free medical and welfare. Children were also not left out.",
        "excerpts": "Supporting local widows to become productive in the communityy through economic empowerment.",
        "date": "23 Jun",
        "start" : "9am",
        "end" : "7pm",
        "organiser" : "Phillip Tirone",
        "venue":"Uvuru Community, Uzo Uwani LGA, Enugu state, Nigeria",
        "location": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d253610.20103115754!2d6.966492868216118!3d6.689044044039436!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x104487e41ea22ee5%3A0x9f9bc38433307d39!2sUzo-Uwani%20LGA%20Headquarters%2C%20Umulokpa!5e0!3m2!1sen!2sng!4v1683882290046!5m2!1sen!2sng",
        "activities": {
            "desc": "It was a memorable event seeing the joy put on the faces of the community residents being provided with free medical services. More than 20 medical professionals voluntarily participated in this event. ",
            "list": ["Medications were prescribed for all the conditions diagnosed where necessary", "Share best practices and knowledge.", " Medical referrals were made for conditions that couldn’t be properly attended to immediately", "Medications were dispensed by Pharmacists", "Patients were counseled on the use of these medications"]
            },
        "vision" : "The vision of this outreach is to make sure that we give appropriate and quality health care treatment and medications to those in the rural dwelling of the African society and to make illness and death rates caused by poor health care condition and facilities reduced to the barest minimum",
        "mission" : "The Sunrise Free Medical Outreach was organized to make health care and medicine very accessible, reduce the amount of health complications in the community and also enlighten the masses on the need for proper medical care"
    }
]