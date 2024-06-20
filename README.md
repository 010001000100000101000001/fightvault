# FightVault

FightVault is your destination for the latest news, updates, and information on mixed martial arts and combat sports. The platform aims to keep fans and enthusiasts informed and connected with the combat sports community. It promotes communication and interaction between users by allowing people to sign up with an email address and creating a password. Site users who are logged in, can comment, rate and vote on the predicted outcome of a bout on relevant posts that include the polling feature. It is a blog where site users can share their opinions and excitement on all things related to combat sports.


## Table of Contents



## Project Overview

FightVault is a blog designed for mixed martial arts and combat sports enthusiasts. It aims to bring together a community of passionate people who share a love for martial arts and combat sports. The platform is dedicated to providing a space where fans can write, read, and learn about their favorite sports and fighters. FightVault strives to offer an engaging experience, from in-depth articles, to the latest news and event coverage. Over time we hope it can grow to a place where we interview fighters and expand a section where users can watch and share media content.


## User Stories

### View a Page of Posts

**As a Site User, I can view a list of recent posts on the home page so that I can quickly find new content.**

- **Acceptance criteria 1:** The home page displays a list of recent posts, including the title, author, date, and a brief summary of the post.
- **Acceptance criteria 2:** Users can click on the title or the image of each post to be re-directed to a page to read the full post with an image related to that post.
- **Acceptance criteria 3:** Pagination is implemented to navigate through multiple pages of posts so a user can navigate to older posts.

### Open a Post

**As a Site User, I can click on a post so that I can read the full text and see a larger version of the image related to the post.**

- **Acceptance criteria 1:** When a blog post title or image is clicked, a user is re-directed to a page that displays the full image and the full written post.

### View Comments

**As a Site User / Admin, I can view comments on an individual post so that I can read the conversation.**

- **Acceptance criteria 1:** Given one or more user comments, the admin can view them.
- **Acceptance criteria 2:** A site user can view all approved comments under the posts.

### Account Registration

**As a Site User, I can register an account so that I can comment on a post.**

- **Acceptance criteria 1:** A user can register an account with an email.
- **Acceptance criteria 2:** Then the user can log in and they will see 
- **Acceptance criteria 3:** When the user is logged in, they can comment, rate posts and vote in the poll on relevant posts that include the polling feature.

### Additional User Stories

**As a Site User, I can register for an account so that I can access additional features and interact with the community.**

- **Acceptance criteria 1:** A registration form is available with fields for username, email, and password.
- **Acceptance criteria 2:** Users receive a welcome message upon successful registration and are able to view thir username, email and time they logged in.

**As a Site User, I can log in to my account so that I can access personalized features.**

- **Acceptance criteria 1:** A login form is available with fields for username and password.
- **Acceptance criteria 2:** Users are redirected to the home page upon successful login.
- **Acceptance criteria 3:** Users see a personalised Welcome back message, their email and the time they logged in.

**As a Site User, I can log out of my account so that I can securely end my session.**

- **Acceptance criteria 1:** A logout button is available in the same location (top right hand corner) on all pages when the user is logged in.
- **Acceptance criteria 2:** Users are redirected to the home page upon successful logout and an alert message displays "You have sucessfully logged out".

**As a Site User, I can post comments on blog posts so that I can engage in discussions.**

- **Acceptance criteria 1:** A comment form is available on each post detail page.
- **Acceptance criteria 2:** Comments are displayed below the post in a threaded format.

**As an Admin, I can manage user comments so that I can moderate content on the site.**

- **Acceptance criteria 1:** Admins can view, approve, or delete all comments from the django admin dashboard.
- **Acceptance criteria 2:** Only approved comments are displayed to other site users.

**As an Admin, I can create, edit, and delete blog posts so that I can manage site content.**

- **Acceptance criteria 1:** Admins have access to the django content management interface.
- **Acceptance criteria 2:** Changes to posts are immediately reflected on the site.

**As a Site User, I can rate blog posts so that I can provide feedback on the content.**

- **Acceptance criteria 1:** A rating system (star ratings customised to gloves) is available on each post detail page.
- **Acceptance criteria 2:** Users can submit a rating out of 5, with 5 being the highest rating.

**As a Site User, I can view the overall rating of a blog post so that I can gauge its quality.**

- **Acceptance criteria 1:** The average rating is displayed on each post detail page.
- **Acceptance criteria 2:** The score the ratings are displayed with the username of the user who rated the post and the time and date it was rated.



## Features

### Existing Features

- **Navigation Bar**
  - A fully responsive navigation bar with links to the Home, About, Contact, Register, Login and Logout.
  - It is consistent across all pages for easy navigation.
  - The Register, Login and Logout is seperated to the right side of the page in large screens.
  - In mobile and smaller screens there is a hamburger menu when clicked on opens a side menu which displays the navigational bar and lists of page. It includes an x to remove the menu 
    from visibility.

- **Home Page**
  - Displays the latest blog posts with titles, authors, times and dates, featured images, and excerpts.
  - When the title is hovered over the colour changes from black to red and when a post has been viewed, the colour of the title changes to blue to show what posts have already been 
    viewed by the site user.
  - It has NEXT and PREVIOUS buttons included to navigate through older posts and navigate back to more recent posts.


- **About Page**
  - Provides information about FightVault’s mission, values, and goals.
  - This can be updated as FightVault evolves and be edited by a site admin in the django admin panel.
  - Two images are displayed on the left hand side, the first is the Fightvault image with a logo and the second is gloves, pads and a black belt.
  - The second image is not displayed on smaller mobile screens for a better UI.
    

- **Contact Page**
  - Allows users to get in touch with the FightVault team for inquiries or feedback.
  - It has the FightVault logo image in the background.


- **User Authentication**
  - User registration form.
  - User login form.
  - A button to logout displayed on every page where the user will be redirected back to the home page a message is displayed confirming they have been logged out.
  - Authentication powered by Django Allauth.
  

- **Blog Post Detail Page**
  - Detailed view of each blog post, including the full post content.
  - Full featured image, relevant to the post.
  - Time and date the post was created.
  - Post Author.
    
- **Comments**
  - A comment section for users to comment on the post.
  - A full view of all approved comments along with the username of the commenter and the time and date of the comment.
  - Feedback to the user to let them know that there comment is awaiting admin approval.
  - An arrow pointing to the comment awaiting to be approved.
  - Comment displayed in bold for easy viewing.
  - Username and time and date slighty greyed out to not be too distracting from the main comments.

 - **Ratings section**
   - A rating system for the post.
   - Average ratings displayed in bold red.
   - Username of the person who rated.
   - Time and date of the rating
   - Boxing gloves graphic for users to interact and choose the rating in a fun an engaging way.
   - Colour change of the gloves from red to black when hovered on and clicked.
   - Easily see visually the rating choice out of 5.
     
- **Polling Section**
    - A polling system to vote on the predicted outcome of a bout, only included on relevant posts.
    - Two options are displayed with both fighters names with an option to select one.
    - A submit vote button to submit the vote.
    - Current poll is displayed in green and red for contrast along with percentage bars included with the fighers names and the persentage of the current votes.
   
### Features Left to Implement





## Design

### Wireframes



### Color Scheme

- The color scheme is designed to be bold and vibrant, reflecting the dynamic nature of combat sports.
  - Primary colors: 
  - Secondary colors: 

### Typography

- The typography is chosen to be modern and easy to read.
  - Primary font: Montserrat
  - Secondary font: Oswald

## Technologies Used

- **Django**
  - The web framework used for developing the FightVault platform.
  
- **Cloudinary**
  - Used for storing and serving media files.
  
- **Django Allauth**
  - Provides comprehensive user authentication and registration functionalities.
  
- **Bootstrap**
  - Utilized for responsive and mobile-first front-end design.
  
- **ElephantSQL**
  - 
  
- **GitHub and Heroku**
 

## Testing



### Automated Tests



### Manual Tests



### Validator Testing 

- **HTML**
 - W3C HTML validator was used for html testing.
 - Link for validator: https://validator.w3.org/.
 
  
- **CSS**
 - W3C CSS validator was used for CSS testing.
 - Link for CSS validator: https://jigsaw.w3.org/css-validator/.


- **JavaScript**
  - JS Hint was used for JavaScript testing.
  - Link for JS Hint: https://jshint.com/.


- **Python**
  - CI Python Linter was used to test python for PEP8 adherence.
  - Link for CI Python Linter: https://pep8ci.herokuapp.com/.
  



## Deployment

This project has been successfully deployed through the Heroku platform, utilizing the Code Institute's Heroku mock terminal. To achieve this, the following deployment procedure was undertaken:

**Repository Cloning**: Initiated the process by cloning the project's repository to ensure a local copy for preparing deployment.

**Procfile Creation**:  A procfile was created and web: gunicorn fightvault.wsgi was added.

**Updated Requirements.txt**: Requirements.txt was updated with the necessary changes using pip3 freeze --local > requirements.txt command in the terminal.

**Settings** DEBUG: Set to False for production.

**Heroku Application**: Proceeded by establishing a new application within the Heroku environment, dedicated specifically to this project.

**Buildpack Configuration**: Configured the necessary Python buildpack.

**Environment Variables**: Set up SECRET_KEY in Config Vars, also CLOUDINARY_URL and DATABASE_URL were set up at appropriate stages.

**Repository Integration**: Linked the Heroku application to this corresponding GitHub repository to enable direct deployments from the source code.

**Application Deployment**: Completed the deployment process by utilizing Heroku's 'Deploy' feature, which facilitated the transition of the project from development to a live environment.

The live link can be found here: https://fightvault-d3f5315751bb.herokuapp.com/

## Credits 

<a href="https://www.freepik.com/free-photo/boxing-glove-hanging-wire-mesh-fence_8403137.htm#fromView=search&page=1&position=13&uuid=6a20f894-e0d5-4319-9924-9afc5383a952">Image by wavebreakmedia_micro on Freepik</a>

https://www.flickr.com/photos/184367221@N07/48711412483/in/photolist-2hdsHRn-Pj4SCJ-MGVwLp-LNU1Pj-2hdsHDD-MJKKCz-VaGuyX-2i5tJbP-ahsvM5-23T37QM-8HsSxH-2o8TiTk-2of4EW3-2ok32PJ-9ed3Fj-D3XoaY-jrUdJJ-SbjLaa-2c3onSK-9ed3Tf-axjffz-2aqvLbw-8HsT4V-aSiTkH-KyuF3Q-aEiZUz-uCabRg-cPw2JE-7ZPJtx-DyYK4c-ckpQN9-2jLwenk-6yZJxW-xsJgov-2mHYQu1-dPUyXf-cEz5q5-5tLc3W-2o4hs6c-ZWEyzs-2iGAyjQ-dh9j6K-7VxbT5-2p4HBAi-94DMLS-21w5mRJ-9xcT5U-PW8Frj-2qq1W-2p4PEyG


https://www.flickr.com/photos/thedailysportsherald/10132617584 TheDailySportsHerald's photo, licensed as Attribution-NonCommercial-NoDerivs.


https://www.flickr.com/photos/jblmpao/31070937830 Demetrious Johnson   Joint Base Lewis McChord's photo, licensed as Attribution-NonCommercial-ShareAlike. 


https://www.flickr.com/photos/122735657@N06/13995369395/in/photolist-njHVJk-nhFug3-njLpTG-rNbgJW-NcyNAj-c4oqhU-njryTS-rNekkh-njrqFQ-rviGuj-rLqp5k-rMTFfB-qQzwsk-rzdqh2-ryYyaW-c8rkBw-rKYNhm-rvA9TN-rvpGWQ-c8rfsQ-NcyNmS-NcyP3w-c4ouff-rB9KRF-NcyNyL-c9VDyU-c4ovV9-bkaVzC-tjJmTF-s6hpAV-c9VNoC-nmuwtz-HDHcLu-4HpKrV-QPFxib-c9Wb2o-c8rhWd-c9WrU5-c4o5wQ-c4ot55-c9W8Ab-c4od75-c4oaH5-c4nXQd-njrHka-c4o15J-c4ooqb-c8rw3W-njrGSh-c8rWWL/   Adam Crowther's photo, licensed as Attribution-NonCommercial-NoDerivs


contact image 2: 
https://www.flickr.com/photos/thejointstaff/34082947345/in/photolist-zxmx9E-zxmxhW-zAxD3t-Nxxbp4-zAxCCF-qvDmkw-zzEMBP-AKm2bC-zzEMsk-oYeYHd-zyzuZy-ATdAeV-AfgdFP-BfoYCT-yrgmhm-26nrCoq-rxPyzN-rN9WCa-rvpGWQ-TJjrZk-TVN1Pc-TJjsiX-jHodhe-2hSrqgq-ruyDWj-HDHcLu-7Z5MpN-7G8biq-5oXVcR-NsHbnC-NsHbDQ-BBHTrg-BzqGLW-BbuNT2-AMumjy-AUVooQ-2payJR4


https://commons.wikimedia.org/wiki/File:Usyk_-_Knyazev_-_0412.jpg


https://www.flickr.com/photos/kevinpoh/4730344693  Kevin Poh's photo


https://www.flickr.com/photos/websummit/52473040640 https://www.flickr.com/photos/websummit/52473040640


https://commons.wikimedia.org/wiki/File:Max_Holloway_180428-D-SW162-1532_%2827918239868%29.jpg  Creator: Sgt. James K. McCann 


https://commons.wikimedia.org/wiki/File:Michael_Chandler_at_MTV_Movie_Awards_2012.jpg American mixed martial artist Michael Chandler interviewed at the MTV Movie Awards 2012


https://www.flickr.com/photos/kenlund/7237766724 Prudential Center, Newark, New Jersey 


https://commons.wikimedia.org/wiki/File:Islam_Makhachev_2022_UFC_belt.png

### Content 


### Media

- 

## Acknowledgements


