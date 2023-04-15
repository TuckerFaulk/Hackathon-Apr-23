**CHARLIE CHARLIE ONE**

[amiresponsive mockups of project]()

**[Link to the deployed site](https://hackathon-apr-2023.herokuapp.com/)

# Project Overview
Charlie Charlie One is a Peer Support Platform connecting veterans seeking mental health support with other veterans who have experienced similar challenges. To facilitate communication, support and encourage community engagement, Charlie Charlie One includes a matching system, a private messaging functionality, and group discussions (blog) and private and public profile options for those needing anonymity.

This platform was built using Django, Python, JavaScript and Bootstrap 4. The site was deployed on Heroku and uses Cloudinary for cloud storage.

Charlee Charlee One is Team 2's Stamp Out The Stigma project submission for Code Institute and Social Soda Hackathon (April 2023).


**TABLE OF CONTENTS**
* [USER EXPERIENCE](#user-experience)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
        * [Feature Planning](#feature-planning)
        * [User Stories](#user-stories)
    * [Structure Plane](#structure-plane)>
        * [Database Design](#database-design)
            * [Database ERD](#database-erd)
            * [Data Modelling](#data-modelling)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
        * [Colour Palette](#colour-paletteframes)
* [Agile Methodology](#agile-methodology)
    * [GitHub Projects](#github-projects)
* [Features](#features)
* [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks Used](#frameworks-used)
    * [Programmes and Applications](#frameworks-used)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

<hr>
---
# USER EXPERIENCE

## Strategy Plane


## Scope Plane
**Feature Planning**
When planning the Charlie Charlie One's features and scope, we drew up a Desirability, Importance and Viability analysis of all the features to be included in the project, and ranked each of these by order of importance from low (1) to high (5). The features that ranked the highest will be prioritised and delivered as part of the MVP. The target users for each ranked feature were also included.

| # | Feature | Target User | Desirability | Importance | Viability  | Delivered |
| --- | --- | --- | --- | --- | --- | --- |
| USER ACCOUNTS|  |  |  |  |  |  |
| 1 | User Role Permissions | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 2 | Account Registration | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 3 | User Email Confirmation | All Users <sup>1</sup> | 3 | 3 | 4 | ❌ |
| 4 | Password Reset | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 5 | Social Media Registration &amp; Login | All Visitors | 5 | 2 | 2 | ❌
| NAVIGATION |  |  |  |  |  |  |
| 6 | Navigation to include: logo, my account (register, login) | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 7 | Navigation to include: my account (my profile, logout), bookmark | Logged In Users | 5 | 5 | 5 | ✅ |
| 8 | Top Navigation Search Bar | All Users <sup>1</sup> | 2 | 3 | 5 | ❌ |
| 9 | Top Navigation to include: my account (my profile, logout) | Logged In Superadmins | 2 | 2 | 2 | ✅ |
| 10 | Searching | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 11 | Filtering | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| BLOG |  |  |  |  |  |  |
| 12 | List of Posts | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 13 | Create Post | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 14 | Post Detail Page | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 15 | Comment on Post | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 16 | Like Posts | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| PROFILES |  |  |  |  |  |  |
| 17 | User Profile Page | Registered Users | 5 | 5 | 5 | ✅ |
| 18 | User Public Profile Page | Registered Users | 5 | 5 | 5 | ✅ |
| 19 | Set Each User Info field to Private or Public | All Registered Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 20 | Follow Other Users | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 21 | Unfollow Other Users | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 21 | View List of Followed Users | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 22 | Update Personal Information | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 23 | Find a Veteran | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 24 | Filter List of Registered Veterans | All Logged In Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| ONE TO ONE MESSAGING |  |  |  |  |  |  |
| 25 | Send Message to a User + Maintain Anonymity, if Preferred | Logged In Users | 5 | 5 | 5 | ✅ |
| 26 | Read Message from a User | Logged In Users | 5 | 5 | 5 | ✅ |
| 27 | Reply to Message from a User  + Maintain Anonymity, if Preferred | Logged In Users | 5 | 5 | 5 | ✅ |
| 28 | View List of Messages Received | Logged In Users | 5 | 5 | 5 | ✅ |
| RESOURCES |  |  |  |  |  |  |
| 29 | List of Charities and NGOs Supporting Veterans and Military Personnel | All Users | 5 | 5 | 5 | ✅ |
| Email Marketing |  |  |  |  |  |  |
| 30 | Email Subscription, Powered by MailChimp | Registered Subscribers | 3 | 3 | 3 | ❌ |
| Contact Us |  |  |  |  |  |  |
| 31 | Contact Form | All Users <sup>1</sup> | 3 | 3 | 3 | ❌ |
## Structure Plane
### Interaction Design

### Database Design
* Database

**Entity Relationship Diagram**
* ERD ![ERD](./documentation/erd.svg)

This ER diagram captures the relationships between real-world entities. The entities are the data points of objects such as persons, places and things and together with their attributes, compose their domain, ie, their individual table. The cardinality (relationships) between these entities are then mapped and identified.

### User Stories
#### First Time Visitor Goals - As a first time user who has not created an account, I want to be able to:
* Immediately understand the main purpose and use of the platform, **Charlie Charlie One**, and intuitively understand how to use it
* Search for specific Veterans based on certain criteria, filter list of registered Veterans or view all.
* Register/ create a user account

#### Registered User Goals - As a registered user, I want to be able to:
* Learn more about what I can do on the **Charlie Charlie One** Platform
* Create, read, edit, and delete my personal information
* Set which of my information I choose to display publicly
* Upload or not upload my image



* Have access to tools I may need in order to add, update or delete my recipes
* Search and view specific recipes (if already available on the App)
* Be forewarned of the consequences of what I am about to do on the App, such as deleting my recipes
* Have my own member user dashboard (read functionality)

#### Site Admin Goals - As an administrator, I want to be able to:
* Have the ability to maintain the Paleo Recipe App, in particular the categories
* Add, edit and delete my own recipes
* Add, edit, retrieve and delete any recipe by category
* Search and view specific recipes (if already available on the App)

# Features
Charlie Charlie One provides:
* Matching System through ---
* Post Content - contribute to the discussion
* Enables veterans to join the discussion, ask for help and support other users anonymously through:
    * an option to set their profile details to private, where the only publicly available information is a required *preferred display name*
* Veterans to create a profile and choose which of their information they want to share publicly.
, private messaging, and group discussions (blog) to facilitate communication and support.

# Future Development, Iteration and Implementation

# Technologies Used
## Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5) Used for the content and structure of the site.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) Used for the styling of the site.

* [Python](https://www.python.org/) Used for the back end programming of the site.

## Frameworks Used
* [DJANGO - v3.2 ](https://docs.djangoproject.com/en/4.1/releases/3.2/) Django is a free and open-source, Python-based web  framework that follows the model–template–views architectural pattern.

* [Bootstrap4 - v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used as the frontend framework.

## Programmes and Applications

* [Git](https://git-scm.com/) used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.
* [GitHub](https://github.com/) is the project's git repository
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) Terminal used to push changes to the GitHub repository.
* [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) used to track and integrate issues for Agile Development
* [favicon.io](https://favicon.io/) used to create the site's favicon
* [Chrome DevTools](https://www.google.com/intl/en_uk/chrome/) - used for debugging, validation (Lighthouse) and taking fullscreen screenshots of the site
* [Balsamiq](https://balsamiq.com/)  - Used to create wireframes.
* [Heroku](https://devcenter.heroku.com/) Used for hosting and deployment of the live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.
* [VSCode](https://code.visualstudio.com/)  - Used to create and edit the website.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)  - Used to test responsiveness and debug.
* [Cloudinary](https://cloudinary.com/)  - Used to add images in the cloud.

## Testing, Bugs & Solutions

* Known Bugs
    * Validation error on Profile template. - Priority to be fixed in next sprint

### Acknowledgments
    Thank you to the Code Institute Hack Team who organised this Hackathon.
<hr>