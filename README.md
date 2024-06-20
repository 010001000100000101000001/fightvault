# FightVault

FightVault is your destination for the latest news, updates, and information on MMA and combat sports. The platform aims to keep fans and enthusiasts informed and connected with the combat sports community. It promotes communication and interaction between users by allowing people to sign up with an email address and creating a password. Site users who are logged in, can comment, rate and vote on the predicted outcome of a bout on relevant posts that include the polling feature. It is a blog where site users can share their opinions and excitement on all things related to combat sports.


## Table of Contents



## Project Overview

FightVault is a blog designed for MMA and combat sports enthusiasts. It aims to bring together a community of passionate individuals who share a love for all things martial arts. The platform is dedicated to providing a space where fans can write, read, and learn about their favorite sports and fighters. FightVault strives to offer an engaging experience, from in-depth articles, to the latest news and event coverage. Over time we hope it can grow to a place where we interview fighters and expand a section where users can watch and share media content.


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
  - Includes user registration, login, and logout functionalities powered by Django Allauth.
  

- **Blog Post Detail Page**
  - Detailed view of each blog post, including the full content, author details, and the ability to leave comments and ratings.
  -

- **Comments and Ratings**
  - Users can leave comments and rate blog posts to provide feedback and engage with the content.
 

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
 
  
- **CSS**


### Unfixed Bugs


## Deployment



The live link can be found here: 

## Credits 


### Content 


### Media

- 

## Acknowledgements


