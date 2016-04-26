# DoorHub
Repo for the Lean &amp; Agile Product Development course at Boston University

Team currently made up of:
- Drew kierke@bu.edu
- Jenny jennychu@bu.edu
- Tang ngtang@bu.edu
- Shidong lsd@bu.edu
- Tianchen tangtc@bu.edu


# DoorHub (working title) Project

The project is focused on learning Lean and Agile methodoligies employing them effectively to add someTHING to the IoT.  We will be pursuing a modular, portable, connected keyless entry system.

## Video Demos:

To start we have videos for each of our features here:

#### DoorHub Lean & Agile Dev - Demo Links:
Main/General Demo (w/security log & motion detector working) - 
`https://youtu.be/l8X3Ur0scr8`

Temporary Key Link Demo - 
`https://youtu.be/w86ZMifzLhI`

Texting Alarm Demo - 
`https://youtu.be/dWvJ4kmH5zE (main demo)`
`https://youtu.be/AH7fdJLDGuI (bonus Demo)`

Reliability Demo - 
`https://youtu.be/ZXOci0WjoVM`

### First Meeting Backlog:
- [x] Setup Slack channel for continuous agile and adaptable corespondence 
- [x] Setup github
- [x] Setup Trello and Sprint board
- [x] First Sprint update
- [x] Setup daily meeting times
- Continued on our Trello board..

Project features will be listed on the project backlogs on the Trello account.

### Relevant Links (updated with resources as we come across them):

#### Security research:
Hey everyone!  If anyone is interested in security of IoT I figured I would share what resources I have come across recently - I am working on mass dynamic analysis tool for detecting IoT vulnerabilities at scale in embedded firmware right now for the 700 level cybersec course this semester and so I have been reading a lot in this area.

Please post any additional resources you guys have used or know of!

#### Why should you care?
It is mostly out of scope of the class but whenever you are doing product development in the IoT space it is becoming increasingly important to keep security at least at the back of your mind.  

Some additional motivation might come from the newest unclassified (2016) U.S. intelligence cybersecurity threat landscape from the U.S. Director of National Intelligence:
Note on page 1 (fifth page of the pdf) the first global cyber threat lists IoT:
http://www.dni.gov/files/documents/SASC_Unclassified_2016_ATA_SFR_FINAL.pdf

#### $$$
And if that wasn't enough there is always the motivation that if you learn about this IoT security there are jobs and bug bounties galore waiting for you: 
https://www.iotvillage.org/#contest https://bugcrowd.com/programs 

#### Where to start - OWASP:
OWASP is a well regarded organization for in web security research, known for their great top 10 vulnerabilities lists spanning various attack spaces.  They recently started a dedicated IoT security project that has a lot of great starter information.

> Slides from a recent talk from RSA conf. about OWASP to give you a basic idea: 
> https://www.owasp.org/images/5/51/RSAC2015-OWASP-IoT-Miessler.pdf (RSA 2015)

> infographic .jpg version: https://www.owasp.org/images/8/8e/Infographic-v1.jpg
> full slides: https://www.owasp.org/images/7/71/Internet_of_Things_Top_Ten_2014-OWASP.pdf (2014)

> The main page for the project with a lot of great resources: 
> https://www.owasp.org/index.php/OWASP_Internet_of_Things_Project 

#### Testing your device:
Checklist based on the OWASP resources above: https://www.owasp.org/index.php/IoT_Testing_Guides
Avatar - Dynamic analysis tool information for anyone doing dedicated one off embedded testing:
Paper from NDSS conference: http://www.s3.eurecom.fr/docs/ndss14_zaddach.pdf 
Slides summarizing paper from the talk: http://www.internetsociety.org/sites/default/files/02_3_slides.pdf 

#### Good Security Conference Videos/talks:
"Internet of Fails" talk from defcon22 (defcon is a hacker culture con in Vegas every year that is much less formal than others, but often also more entertaining, this is just an interesting talk in general, probably not the best resource in this list if you're looking to get your hands dirty):
https://www.youtube.com/watch?v=WHdU4LutBGU 

####Random Resources:
Great article by arstechnica about shodan (the google of vulnerable IoT devices) and how Minimum viable product and waterfall prod development in the IoT realm are such huge problems: http://arstechnica.com/security/2016/01/how-to-search-the-internet-of-things-for-photos-of-sleeping-babies/ 
Mass analysis tool developed by a professor at BU in ece for mass dynamic analysis and automatic emulation of IoT firmware images via modified qemu (open source project not applicable for one off IoT device testing, but cool stuff nontheless): 
open source proj: https://github.com/firmadyne/firmadyne 
paper just published at NDSS last week: https://www.internetsociety.org/sites/default/files/blogs-media/towards-automated-dynamic-analysis-linux-based-embedded-firmware.pdf 
Here is a bunch of stuff from a  post in an old thread I made that was a bit buried but I am not reediting it so take it as is:

#### Less organized old post:
"
Also if anyone is interested in embedded and Internet of things security/wants to keep security in mind when designing their devices - despite the NSFW name this is actually a really good source for sec write ups on internet of things projects gone wrong:
https://www.reddit.com/r/theinternetofshit/top/?sort=top&t=year
 

"The reason my lamp is insecure" - One more technical article about a specific application, namely raspberry pi and a more technical write up on security measures:
https://www.praetorian.com/blog/reason-why-my-internet-of-things-iot-lamp-is-insecure
 
A discussion between professional Internet of Things hackers and end users on state of IoT sec:
https://www.reddit.com/r/IAmA/comments/3ka38q/we_are_professional_iot_hackers_and_researchers/
"

Conclusion:

In June I will be working at a company/dept focused on cybersec research in their "Agile & Adaptive" department that is composed of 7 FFRDCs.  There is definitely a place for security in the agile development process and I encourage you all to consider it in the future.  

Please post anything you find interesting in the space over the course of the semester - enjoy break!

