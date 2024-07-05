# FightVault



## Introduction

This is my fourth project in Code Institute Diploma in Software Development with eCommerce. FightVault is a blog for fans of martial arts and combat sports. It promotes communication and interaction between users by allowing people to sign up with an email address and creating a password. Users are authenticated use django-allauth. Site users who are logged-in, can create comments, read other user's approved comments, update and delete their own comments. Logged-in users can rate a blog post and vote on the predicted outcome of a bout or match on relevant posts that include the polling feature. The website is a full stack django project written in HTML, CSS, Javascript and Python.


![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/8a5f23ca-56c5-40b7-b946-98f2475b346c)


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
  - [Lighthouse Tests](#lighthouse-tests)
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

Must have, Should have, Could have or Won't have labels have been assigned to my User Stories based on level of importance for a MVP (Minimum Viable Product) and for future iterations. They are available to view in my Projects section here on Github. Each user story is assigned points based on estimated time taken to develop each user story.

The goal of MVP development is to test the product viability, gather user feedback, and validate the idea before investing more time and resources into developing the product further.

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
- **Acceptance criteria 3** Given more than one comment, there is a conversation thread.
- **Acceptance criteria 4** Comments need to be approved by an admin before they are visible to other users.
- **Acceptance criteria 5** A success message is generated to let the user know their comment was submitted for approval.

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

**As a logged in Site User, I can modify my comment on a post so that I can update or correct what I have previously written.**

-  **Acceptance criteria 1:** Given a logged-in user, they can modify their comment.
-  **Acceptance criteria 2:** The user must be able to click this option to access a form to edit their comment.
-  **Acceptance criteria 3:** After modifying their comment, the user can save changes.
-  **Acceptance criteria 4:** The site should provide feedback indicating the comment has been successfully updated.

**As a logged in site user I can I can delete my comment on a post so that I can remove my participation from the conversation if I choose.**

- **Acceptance criteria 1:** Given a logged-in user, they can see a "Delete" option next to their comment so that they can click on it to initiate the deletion of their own comment.
- **Acceptance criteria 2:** When the "Delete" option is clicked, a pop-up confirmation box appears asking the user, "Are you sure you want to delete this comment?" The user must confirm to delete or click the x or anywhere on the page to cancel.
- **Acceptance criteria 3:** Upon confirming the deletion, the comment is removed from the post. The site should provide the user feedback indicating the comment has been successfully deleted.

**As a site user I can vote on who I think will win a fight and see the percentage of votes for each fighter so that I can participate in predicting the outcomes for a fun element, see the community's opinions and engage, more with the content.**

- **Acceptance criteria 1:** The user can see a vote form at the bottom of each fight-related post allowing them to choose between two fighters.
- **Acceptance criteria 2:** After submitting a vote, the user receives a confirmation message, and their vote is recorded in the database.
- **Acceptance criteria 3:** The user receives a confirmation message after submitting their vote, and their vote is recorded in the database.
- **Acceptance criteria 4:** The user can see visual percentage bars showing the distribution of votes for each fighter, updated in real-time based on all submitted votes.




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



### Contact

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

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/424cd5aa-dd5a-4e07-b662-58e1b3b9a3cf)




- **About Page**
  - Provides information about FightVault’s mission, values, and goals.
  - This can be updated as FightVault evolves and be edited by a site admin in the django admin panel.
  - Two images are displayed on the left hand side, the first is the Fightvault image with a logo and the second is gloves, pads and a black belt.
  - The second image is not displayed on smaller mobile screens for a better UI.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/d2b121d2-7d8d-407e-9957-fc6d340cbfd2)



- **Contact Page**
  - Allows users to get in touch with the FightVault team for inquiries or feedback.
  - It has the FightVault logo image in the background.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/160e97d9-68b6-4286-864e-7a0df4b60370)




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
  - Full CRUD functionality, a logged in user has the ability to edit and delete their own comments

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/c4112aa7-2344-4d14-9a31-7d54986056a9)

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/45bf223c-2b97-4ddf-9ccf-09d640852462)

A modal pops up asking the user if they want to delete their comment:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/3acc40da-26c8-4d5f-8f36-9e8855b8fcb9)


 - **Ratings section**
   - A rating system for the post.
   - Average ratings displayed in bold red.
   - Username of the person who rated.
   - Time and date of the rating
   - Boxing gloves graphic for users to interact and choose the rating in a fun an engaging way.
   - Colour change of the gloves from red to black when hovered on and clicked.
   - Easily see visually the rating choice out of 5.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/1ada1f10-b08e-4906-9761-a582352a5198)


     
- **Polling Section**
    - A polling system to vote on the predicted outcome of a bout, only included on relevant posts.
    - Two options are displayed with both fighters names with an option to select one.
    - A submit vote button to submit the vote.
    - Current poll is displayed in green and red for contrast along with percentage bars included with the fighers names and the persentage of the current votes.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/4827bbeb-dabe-4ce4-9660-8f3bcb1c1496)



- **Custom 404 Not Found error page**

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/278b6c22-287e-44eb-b610-8da25f5e9650)


- **Custom 500 internal server error page**

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/424d7144-0013-4a57-bdeb-c2c0b399814c)



### Features Left to Implement

In future iterations of the website, with more time, I will create the ability for users to also create and edit blog posts but at this time this is reserved for staff and admin level users who have credentials to access the admin panel. I will create a section of the website where media files can be viewed and users can comment and rate the video clips.


## Design

### Wireframes

Desktop:
![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/b6409f45-46ca-4b7a-a561-1972bf7cf6e4)

Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/c2752568-0b1d-4949-9d63-cd053c6b4841)




### Color Scheme

- The color scheme is designed to be bold and vibrant, reflecting the dynamic nature of combat sports.
- https://contrast-grid.eightshapes.com/ was utilised to ensure good scores on contrast ratio for improved accessibility.

### Typography

Google fonts was utilised for a modern look and fall back fonts were set in case of any issues that may arise.

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



### Lighthouse Tests

#### Home

 Desktop:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/b3d94f6f-0758-4420-bf34-107d8fb1772e)


Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/02deeeb6-eb32-4170-a532-8f19632a5f74)


#### About

Desktop:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/97c0e5c1-bec3-43a0-ae43-e763bbc50ded)


Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/36793230-e4aa-4a90-84f3-31a973183ac2)


#### Contact

Desktop:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/8f3ebe95-d6d4-4058-9b41-9c40a2a7b36c)


Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/63ce8445-153c-4e05-be10-679bd67b99c5)


#### Register

Desktop:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/86c87fa6-4c2e-4edf-957a-d215a76f6f06)


Mobile: 

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/1bc2ed53-987f-4526-be95-4c32436d3d3b)



#### Login

Desktop: 

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/e3045b3d-34c8-4524-adb2-d9df3dc24cd8)


Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/7755234d-175b-4c08-acfb-31f4c19c7935)


#### Post Detail Page


Desktop:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/a7f40a3b-f92f-426d-947b-a3055dee5c79)


Mobile:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/fbac2e6b-679f-4666-91b7-8ee875bb1d69)






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


### Contact Form

| Feature Tested                | Expected Outcome                                                 | Testing Performed        | Actual Outcome                                | Result   |
|-------------------------------|------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Email input requires email    | The email input is required, warning "@" must be included        | incorrect email format   | message will not post, warning appears        | Pass     |
| Send button                   | redirects to thank_you page with a success response message      | Click send               | Correct page and message is displayed         | Pass     |


### Post Detail Page

| Feature Tested                | Expected Outcome                                                 | Testing Performed        | Actual Outcome                                | Result   |
|-------------------------------|------------------------------------------------------------------|--------------------------|-----------------------------------------------|----------|
| Vote System working correctly | Vote system displays the correct message, and updates Poll result| Submit Vote, check       | Feedback given and Poll updates in real time  | Pass     |
| Vote Progress Bars            | Progress bars updates as new votes are submitted                 | Test with several voters | Progress bars are correctly updated and diplay| Pass     |
| Ratings system                | The correct feedback messages are displayed                      | Submit Rating, check     | Correct user feedback based on conditions     | Pass     |
| Average Rating is updated     | Average Ratings updates when ratings are submitted successfully  | Test with several raters | Average Ratings are updated successfully      | Pass     |
| Posting a comment             | A comment is posted when submitted successfully (admin approved) | Test with several users  | A comment posts successfuly, (admin approved) | Pass     |
| Update a comment              | A comment is updated when a logged in user updates               | Test with several users  | A comment updates successfully                | Pass     |
| Delete a comment              | A comment is deleted when a logged in user deletes               | Test with several users  | A comment is removed from the public page     | Pass     |
| Warning modal                 | A warning modal asks user if they want to confirm or cancel      | Test with several users  | A Warning Modal is displayed for the user     | Pass     |

### Validator Testing 

**HTML**
  W3C HTML validator was used for html testing.
 - Link for validator: https://validator.w3.org/.

#### Home
link: https://fightvault-d3f5315751bb.herokuapp.com/

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/11d4fe04-9a19-45fb-b040-9e262223d71f)


#### About
link: https://fightvault-d3f5315751bb.herokuapp.com/about/

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/eb4f2354-ba9c-414f-b29c-ad52ec5b0dc5)

#### Contact
link: https://fightvault-d3f5315751bb.herokuapp.com/contact/

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/2b61b3d8-22e5-46ae-aa30-42828a010dee)


#### Register / signup
link: https://fightvault-d3f5315751bb.herokuapp.com/accounts/signup/

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/98afcaa5-5398-4ef2-add2-f661d0583581)


#### Login
link: https://fightvault-d3f5315751bb.herokuapp.com/accounts/login/
![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/25e8bed5-d471-494e-ba87-1e00430edfab)



**CSS**
 - W3C CSS validator was used for CSS testing.
 - Link for CSS validator: https://jigsaw.w3.org/css-validator/.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/e2d27275-6c40-4e06-b1d9-7e3821ed31a9)

By Direct input:

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/6eaff242-4a30-4fd4-89d2-6fc0b9777d21)



**JavaScript**
  - JS Hint was used for JavaScript testing.
  - Link for JS Hint: https://jshint.com/.

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/e5464c2e-b349-41e3-808d-32c42046ff9b)


**Python**
  - CI Python Linter was used to test python for PEP8 adherence.
  - Link for CI Python Linter: https://pep8ci.herokuapp.com/.

All python code was tested and no errors present apart from in the settings file which has pre-existing code that was not added by me.

Example:
blog/views.py

![image](https://github.com/010001000100000101000001/fightvault/assets/147556282/393c1187-65b7-4c6d-a2c8-2f1eeed36bdc)


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

I chose the subjects and and fights and used ChatGPT to generate an article which I edited and corrected some information for the examples of the blog posts that would be made by real admins that are part of the FightVault team. Some posts are dated and this site would always have fresh posts added as new events and news unfolds in real time. I created fake accounts and usernames to add comments, votes and ratings on the posts to test the functionality of featuures and give an example of how the site would be used by people who signed up and created an account. The codestar walk-through project was used as a base to start this project and implement a lot of ideas and technologies which I have added some and taken some away to make this project my own.

#### Links and sources

- https://ausi.github.io/respimagelint/docs.html#images.missingFittingSrc
- https://www.w3schools.com/
- https://www.codecademy.com/
- https://claude.ai/
- https://dequeuniversity.com/rules/axe/4.9/link-name
- https://stackoverflow.com/questions/51884586/force-cloudinary-urls-to-use-https
- https://www.freshtechtips.com/2014/01/rwd-testing-in-google-chrome.html
- https://cloudconvert.com/jpg-to-webp
- https://tinypng.com/
- https://ezgif.com/resize
- https://medium.com/nyc-design/7-rules-for-creating-visually-aesthetic-ui-6ac0fe8856f
- https://mailtrap.io/blog/gmail-smtp/
- https://www.learnpython.org/
- https://fonts.google.com/
- https://docs.google.com/document/d/1VSJtnhh_8djRyncotRzMJG9g_ATfiBHasUVZ1xTwybE/edit#heading=h.hvy9tw74f1o0
- https://cloudinary.com/
- https://web.dev/articles/csp#eval_too



### Media

- https://www.flickr.com/

- https://pixabay.com/

- Google search using the Free license filter.

- https://www.flickr.com/photos/kevinpoh/4730344693  Kevin Poh's photo

- https://www.flickr.com/photos/websummit/52473040640 https://www.flickr.com/photos/websummit/52473040640

- https://commons.wikimedia.org/wiki/File:Max_Holloway_180428-D-SW162-1532_%2827918239868%29.jpg  Creator: Sgt. James K. McCann 

- https://commons.wikimedia.org/wiki/File:Michael_Chandler_at_MTV_Movie_Awards_2012.jpg American mixed martial artist Michael Chandler interviewed at the MTV Movie Awards 2012

- https://www.flickr.com/photos/kenlund/7237766724 Prudential Center, Newark, New Jersey 

- https://commons.wikimedia.org/wiki/File:Islam_Makhachev_2022_UFC_belt.png

- ChatGPT was used to generate the images on the About page. I shared some similar images and gave prompts to change the colour scheme until I selected the images to be used.


### Favicons

Font awesome icons are used througout the site. Link: https://fontawesome.com/.
The glove icons from the Ratings system are from Freefavicon. Link: https://www.freefavicon.com/freefavicons/sports/iconinfo/boxing-glove-152-171268.html.
The favicon generator that was used for the browser tab thumbnail is Real Favicon Generator. Link: https://realfavicongenerator.net/.


## Acknowledgements

A big Thank you to everyone at Code Institute, Laura our Cohort facilitator and everyone for the support. A special thanks to my mentor  Matt Bodden for keeping me on track on always pointing me in the right direction.
