**TABLE OF CONTENTS**

* [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
    * [Colour Palette](#colour-paletteframes)
* [Features](#features)
* [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks Used](#frameworks-used)
    * [Programmes and Applications](#frameworks-used)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

<hr>

## Structure Plane
### Interaction Design

* User Flow Diagram ![User Journey Flow](./documentation/rising-women-user-flow-diagram.png)

### Database Design
* Database

**Entity Relationship Diagram**
* [ERD Version 1](./documentation/rising-women-erd-v1.png)
* [ERD Version2](./documentation/rising-women-erd-v2.png)
* ERD Version 3 - FINAL ![ERD Version3](./documentation/rising-women-erd-v3.png)

This ER diagram captures the relationships between real-world entities. The entities are the data points of objects such as persons, places and things and together with their attributes, compose their domain, ie, their individual table. The cardinality (relationships) between these entities are then mapped and identified.

* Data Modelling
    As evidenced by the ERD discussed above, the data model type used for this project is the Relational Model.
    * **User Model**
    - The User model is a component of Django's Authentication system and contains information about the user.
    - The User model contains the following fields: username, email, first_name, last_name, password, is_staff, is_active, is_superuser, date_joined, and last_login.

    * **UserProfile Model**
        - The UserProfile model is an extension of the Django User model and has a one-to-one relationship with it.
        - The UserProfile model contains the following fields: user, is_mentor, is_mentee, default_town_or_city, executive_summary, technical_skills, leadership_skills, my_achievements, my_linkedin, my_website, my_pyblished_articles, my_mentors, my_inspirational_wwomen, my_testimonials_given, my_testimonials_received
        - The UserProfile model is included in the installed profiles application.

    * **Category Model**
        - The Category model contains the following fields: name.
        - It is one of the models included in the installed mentors application.

    * **Subcategory Model**
        - The Subcategory model contains the following fields: name, category.
        - It contains the Category model as a foreignkey.
        - It is one of the models included in the installed mentors application.

    * **Mentor Model**
        - The Mentor model contains the following fields: name, slug, verified, expertise, bio, image, website, linkedin, category, subcategory.
        - It contains the Category model as a foreignkey.
        - It contains the Subcategory model as a foreignkey.
        - It is one of the models included in the installed mentors application.

    * Contact Model
        - The Cintact model contains the following fields: fullname, email, verified, areas_of_expertise, website, linkedin, bio, why_you_want_to_become_a_mentor
        - It is the only model included in the installed contact application.

### User Stories
| #                                | Issue ID | Target User | User Story                                                                                                                                                                                                 |
|----------------------------------| --- |-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VIEWING &amp; NAVIGATION         |  |             |                                                                                                                                                                                                            |
| 1                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | Visitor     | Create a profile                                                                                                                                |
| 2                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | Visitor     | Provide information about service and MH issues                                                                                                           |
| 3                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | Visitor     | Post content (images/stories)                                                                                              |
| 4                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | Visitor     |                                                                                                                    |
| 5                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | Visitor     |
                  |
| 6                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | User        |                                                                                      |
| 7                                | [add-here-issue-number](add-here-issue-closed-resolved-number) | User        |
| REGISTRATION &amp; USER ACCOUNTS |  |             |

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


### Acknowledgments
    Thank you to the Code Institute Hack Team who organised this Hackathon.
<hr>