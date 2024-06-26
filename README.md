# FightVault



## Introduction

This is my fourth project in Code Institute Diploma in Software Development with eCommerce. FightVault is a blog for fans of martial arts and combat sports. It promotes communication and interaction between users by allowing people to sign up with an email address and creating a password. Users are authenticated use django-allauth. Site users who are logged-in, can create comments, read other user's approved comments, update and delete their own comments. Logged-in users can rate a blog post and vote on the predicted outcome of a bout or match on relevant posts that include the polling feature. The website is a full stack django project written in HTML, CSS, Javascript and Python.


![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/80d903a9-2720-43ee-9569-268649d03556)

[Click Here to View Live Website on Heroku](https://fightvault-d3f5315751bb.herokuapp.com/)



## Table of Contents
- [FightVault](#fightvault)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
- [User Stories](#user-stories)
  - [View a Page of Posts](#view-a-page-of-posts)
  - [Open a Post](#open-a-post)
  - [View Comments](#view-comments)
  - [Account Registration](#account-registration)
  - [Additional User Stories](#additional-user-stories)
- [Entity Relationship Diagram - ERD](#entity-relationship-diagram---erd)
  - [Entities and Attributes](#entities-and-attributes)
    - [Post](#post)
    - [Comment](#comment)
    - [Rating](#rating)
    - [Vote](#vote)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Navigation Bar](#navigation-bar)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Contact Page](#contact-page)
    - [User Authentication](#user-authentication)
    - [Blog Post Detail Page](#blog-post-detail-page)
    - [Comments](#comments)
    - [Ratings Section](#ratings-section)
    - [Polling Section](#polling-section)
  - [Features Left to Implement](#features-left-to-implement)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Automated Tests](#automated-tests)
  - [Manual Tests](#manual-tests)
  - [Validator Testing](#validator-testing)
    - [HTML](#validator-testing)
    - [CSS](#validator-testing)
    - [JavaScript](#validator-testing)
    - [Python](#validator-testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Favicons](#favicons)
- [Acknowledgements](#acknowledgements)

## Project Overview

The aim is to provide a space for people who share a love for martial arts and combat sports. The site gives a space  for  users to read, write, and learn about their favourite sports and fighters. Over time we hope it can grow to a place where we interview fighters and expand a section where users can watch and share media content.


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


## Entity Relationship Diagram - ERD


| Attribute         | Data Type       | Notes                                    |
|-------------------|-----------------|------------------------------------------|
| **title**         | `CharField`     | `max_length=100`, `default='About FightVault'` |
| **profile_image** | `CloudinaryField` | `default='placeholder'`                 |
| **mission**       | `TextField`     | `blank=True`                             |
| **values**        | `TextField`     | `blank=True`                             |
| **goals**         | `TextField`     | `blank=True`                             |
| **updated_on**    | `DateTimeField` | `auto_now=True`                          |


## Entities and Attributes

### Post


| Attribute         | Data Type                | Notes                                |
|-------------------|--------------------------|--------------------------------------|
| **title**         | `CharField`              | max_length=200, unique=True          |
| **slug**          | `SlugField`              | max_length=200, unique=True          |
| **author**        | `ForeignKey`             | to `User`, related_name="blog_posts" |
| **featured_image**| `CloudinaryField`        | default='placeholder'                |
| **content**       | `TextField`              |                                      |
| **created_on**    | `DateTimeField`          | auto_now_add=True                    |
| **updated_on**    | `DateTimeField`          | auto_now=True                        |
| **status**        | `IntegerField`           | choices=STATUS_CHOICES, default=0    |
| **excerpt**       | `TextField`              | blank=True                           |
| **fighter1_name** | `CharField`              | max_length=35, default='Fighter 1'   |
| **fighter2_name** | `CharField`              | max_length=35, default='Fighter 2'   |
| **display_voting**| `BooleanField`           | default=False                        |

**Relationships:**
- One-to-Many with `User` (author)
- One-to-Many with `Comment`
- One-to-Many with `Rating`
- One-to-Many with `Vote`

### Comment

| Attribute         | Data Type                | Notes                                |
|-------------------|--------------------------|--------------------------------------|
| **post**          | `ForeignKey`             | to `Post`, related_name="comments"   |
| **author**        | `ForeignKey`             | to `User`, related_name="comments_author" |
| **body**          | `TextField`              |                                      |
| **approved**      | `BooleanField`           | default=False                        |
| **created_on**    | `DateTimeField`          | auto_now_add=True                    |

**Relationships:**
- Many-to-One with `Post`
- Many-to-One with `User`

### Rating

| Attribute         | Data Type                | Notes                                |
|-------------------|--------------------------|--------------------------------------|
| **post**          | `ForeignKey`             | to `Post`, related_name="ratings"    |
| **user**          | `ForeignKey`             | to `User`                            |
| **score**         | `IntegerField`           | choices=1-5                          |
| **comment**       | `TextField`              | blank=True, null=True                |
| **created_on**    | `DateTimeField`          | auto_now_add=True                    |

**Relationships:**
- Many-to-One with `Post`
- Many-to-One with `User`

### Vote

| Attribute         | Data Type                | Notes                                |
|-------------------|--------------------------|--------------------------------------|
| **post**          | `ForeignKey`             | to `Post`, related_name="votes"      |
| **user**          | `ForeignKey`             | to `User`                            |
| **choice**        | `CharField`              | max_length=10                        |
| **created_at**    | `DateTimeField`          | auto_now_add=True                    |

**Relationships:**
- Many-to-One with `Post`
- Many-to-One with `User`



### Attributes

| Attribute     | Data Type      | Notes                                |
|---------------|----------------|--------------------------------------|
| **name**      | `CharField`    | max_length=100                       |
| **email**     | `EmailField`   |                                      |
| **message**   | `TextField`    |                                      |
| **created_at**| `DateTimeField`| auto_now_add=True                    |





## Features

### Existing Features

- **Navigation Bar**
  - A fully responsive navigation bar with links to the Home, About, Contact, Register, Login and Logout.
  - It is consistent across all pages for easy navigation.
  - The Register, Login and Logout is seperated to the right side of the page in large screens.
  - In mobile and smaller screens there is a hamburger menu when clicked on opens a side menu which displays the navigational bar and lists of page. It includes an x to remove the menu 
    from visibility.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/9266a9e6-d992-4430-b856-7df2d0ac03aa)

- **Home Page**
  - Displays the latest blog posts with titles, authors, times and dates, featured images, and excerpts.
  - When the title is hovered over the colour changes from black to red and when a post has been viewed, the colour of the title changes to blue to show what posts have already been 
    viewed by the site user.
  - It has NEXT and PREVIOUS buttons included to navigate through older posts and navigate back to more recent posts.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/210229b3-fb66-415f-b2d5-a73739bc9c7d)



- **About Page**
  - Provides information about FightVault’s mission, values, and goals.
  - This can be updated as FightVault evolves and be edited by a site admin in the django admin panel.
  - Two images are displayed on the left hand side, the first is the Fightvault image with a logo and the second is gloves, pads and a black belt.
  - The second image is not displayed on smaller mobile screens for a better UI.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/2c7b045e-0b90-4475-8fad-f3e59c1de530)


- **Contact Page**
  - Allows users to get in touch with the FightVault team for inquiries or feedback.
  - It has the FightVault logo image in the background.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/6e09a232-0253-4f7d-9d68-82a2d0daca09)



- **User Authentication**
  - User registration form.
  - User login form.
  - A button to logout displayed on every page once the user has logged in where the user will be redirected back to the home page a message is displayed confirming they have been logged out.
  - Authentication powered by Django-Allauth.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/7f429300-a8c5-4984-b122-70ed59ccb596)

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/4b6a1567-12ee-4160-bcfc-598b76d3bff1)

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/09a0368a-1360-4760-a449-7dc18481c4e1)




- **Blog Post Detail Page**
  - Detailed view of each blog post, including the full post content.
  - Full featured image, relevant to the post.
  - Time and date the post was created.
  - Post Author.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/23ec8f8d-2038-408b-b651-44997a3c118e)
Page scroll continued below .. 
![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/7481613b-888e-4291-a303-7f6cf7cf8cb3)


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

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/3883e5b1-0d51-48c9-8689-59fd5ae763ef)

     
- **Polling Section**
    - A polling system to vote on the predicted outcome of a bout, only included on relevant posts.
    - Two options are displayed with both fighters names with an option to select one.
    - A submit vote button to submit the vote.
    - Current poll is displayed in green and red for contrast along with percentage bars included with the fighers names and the persentage of the current votes.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/cddf69de-d34d-4764-8cb4-1183802aa5c3)


- **Custom 404 error page**

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/278b6c22-287e-44eb-b610-8da25f5e9650)



### Features Left to Implement

Another section of the website where media files can be viewed and users can comment and rate the video clips.




## Design

### Wireframes



### Color Scheme

- The color scheme is designed to be bold and vibrant, reflecting the dynamic nature of combat sports.

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
  - Used as the database to store information.
  
- **GitHub and Heroku**
 

## Testing



### Automated Tests



### Manual Tests

### Navigation Bar

| Feature Tested                | Expected Outcome                                                 | Testing Performed        | Actual Outcome                                | Result   |
|-------------------------------|------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| FightVault logo link          | Directs user to the home page                                    | Click "FightVault"       | Directed to home page                         | Pass     |
| Home link                     | Directs user to the home page                                    | Click "Home"             | Directed to home page                         | Pass     |
| About link                    | Directs user to the about page                                   | Click "About"            | Directed to about page                        | Pass     |
| Contact link                  | Directs user to the booking page                                 | Click "Contact"          | Directed to contact page                      | Pass     |
| Register link                 | Directs user to the sign up page                                 | Click "Register"         | Directed to sign up page                      | Pass     |
| Login in link                 | Directs user to the sign in page                                 | Click "Login"            | Directed to sign in page                      | Pass     |
| register link in alert bar    | Directs user to the sign up page                                 | Click "register"         | Directed to sign up page                      | Pass     |
| login in link in alert bar    | Directs user to the sign in page                                 | Click "login"            | Directed to sign in page                      | Pass     |
| Logout link (signed in)       | Directs user to the home page / Displays feedback message        | Click "Logout"           | Directed to home page (alerts user)           | Pass     |
| Personalised welcome message  | Personalised welcome message for logged in user displayed        | Signed in                | Personalised message displayed                | Pass     |
| Personal email displayed      | Displays users email                                             | Signed in                | Users email is displayed                      | Pass     |
| Last login displayed          | Displays date and time user logged in                            | Signed in                | Displays date and time user logged in         | Pass     |

### Home page

| Feature Tested                | Expected Outcome                                                 | Testing Performed        | Actual Outcome                                | Result   |
|-------------------------------|------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Responsive design             | The page changes so the content fits at all screen sizes         | Change sizes (DevTools)  | The page is responsive amd content fits       | Pass     |
| Text readability              | Text is readable at all screen sizes                             | Read all text blocks     | The text is readable at all breakpoints       | Pass     |
| Pagination buttons            | NEXT and PREVIOUS buttons redirects to see older and newer posts | Click NEXT and PREVIOUS  | Posts are displayed correctly and scrollable  | Pass     |
| Image click redirects         | Clicking all the post image redirects to post_detail             | Click all images         | User is redirected to post_detail page        | Pass     |
| Post title click redirects    | Clicking all post titles redirects user to post_detail           | Click all post titles    | User is redirected to post_detail page        | Pass     |
| Social media links wired-up   | Clicking social media links opens new tab to social media page   | Click social media icons | New tab is opened to social media page        | Pass     |




### Validator Testing 

**HTML**
  W3C HTML validator was used for html testing.
 - Link for validator: https://validator.w3.org/.
 
  
**CSS**
 - W3C CSS validator was used for CSS testing.
 - Link for CSS validator: https://jigsaw.w3.org/css-validator/.


**JavaScript**
  - JS Hint was used for JavaScript testing.
  - Link for JS Hint: https://jshint.com/.


**Python**
  - CI Python Linter was used to test python for PEP8 adherence.
  - Link for CI Python Linter: https://pep8ci.herokuapp.com/.
  



## Deployment

### Fork the Repository
1. Click the "Fork" button at the top right corner of the page.
2. This action creates a copy of the repository under your own GitHub account.

### Clone the Repository Locally
- **Open Your Forked Repository:**
  - Go to your GitHub account and open the forked FightVault repository.
- **Clone the Repository:**
  - Click the "Code" button.
  - Copy the URL provided.
- **Open Your Command Line Interface (CLI):**
  - Navigate to the directory where you want to clone the repository.
  - Run the Clone Command: "git clone <copied-URL>"
    - Replace `<copied-URL>` with the URL you copied from GitHub.
- **Move Into the Cloned Directory:**"cd fightvault"

### Set Up the Application Locally
- **Install Dependencies:**
  - Ensure you have Python and pip installed.
  - Run the following command to install the required packages: `pip install -r requirements.txt`
- **Run the Application:**
  - Start the development server: `python manage.py runserver`

### Deploy to Heroku

This project has been successfully deployed through the Heroku platform, utilizing the Code Institute's Heroku mock terminal. To achieve this, the following deployment procedure was undertaken:

- **Open Heroku:**
  - Go to Heroku and log in to your account.
- **Create a New Application:**
  - Click on "New" in the top right corner and select "Create new app".
  - Choose a unique app name and select your region.
  - Press "Create app".
- **Configure the Application Settings:**
  - **Config Vars:**
    - Navigate to the "Settings" tab.
    - Under "Config Vars", click "Reveal Config Vars".
    - Add the following environment variables:
      ```
      DATABASE_URL: Your database URL.
      CLOUDINARY_URL: Your Cloudinary URL for managing media files.
      SECRET_KEY: A secret key for Django security (generate a random one).
      ```
  - **Buildpacks:**
    - Scroll to the "Buildpacks" section and click "Add buildpack".
    - Select "Python" and press "Save changes".
- **Deploy the Application:**
  - **Connect to GitHub:**
    - Go to the "Deploy" tab.
    - In the "Deployment method" section, select "GitHub".
    - Search for your forked FightVault repository and press "Connect".
  - **Manual Deploy:**
    - Scroll down to the "Manual deploy" section.
    - Select the branch you want to deploy and click "Deploy Branch".
  - Heroku will now build and deploy application.
  

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

### Content

I chose the subjects and and fights and used ChatGPT to generate an article which I edited and corrected some information for the examples of the blog posts that would be made by real admins that are part of the FightVault team. Some posts are dated and this site would always have fresh posts added as new events and news unfolds in real time. I created fake accounts and usernames to add comments, votes and ratings on the posts to test the functionality of featuures and give an example of how the site would be used by people who signed up and created an account.


### Media


https://commons.wikimedia.org/wiki/File:Usyk_-_Knyazev_-_0412.jpg


https://www.flickr.com/photos/kevinpoh/4730344693  Kevin Poh's photo


https://www.flickr.com/photos/websummit/52473040640 https://www.flickr.com/photos/websummit/52473040640


https://commons.wikimedia.org/wiki/File:Max_Holloway_180428-D-SW162-1532_%2827918239868%29.jpg  Creator: Sgt. James K. McCann 


https://commons.wikimedia.org/wiki/File:Michael_Chandler_at_MTV_Movie_Awards_2012.jpg American mixed martial artist Michael Chandler interviewed at the MTV Movie Awards 2012


https://www.flickr.com/photos/kenlund/7237766724 Prudential Center, Newark, New Jersey 


https://commons.wikimedia.org/wiki/File:Islam_Makhachev_2022_UFC_belt.png

ChatGPT was used to generate the images on the About page. I shared some similar images and gave prompts to change the colour scheme until I selected the images to be used.


### Favicons

Font awesome icons are used througout the site. Link: https://fontawesome.com/.
The glove icons from the Ratings system are from Freefavicon. Link: https://www.freefavicon.com/freefavicons/sports/iconinfo/boxing-glove-152-171268.html.
The favicon generator that was used for the browser tab thumbnail is Real Favicon Generator. Link: https://realfavicongenerator.net/.


## Acknowledgements


