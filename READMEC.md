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