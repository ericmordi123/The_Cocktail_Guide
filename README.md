# The Cocktail Guide

Link to final version []

## Data Centric Development Project - Milestone Project 3
The aim of this project was to utilise the skills and frameworks leanred to create and online cocktail app that will allow users to veiw, Edit and create there own cocktails.

## User Journey And Testing 
| User Journey  | User Flow | Manual Testing |
| ------------- | ------------- | -------------------- |
| - As a User I want the ability to add cocktail reicpe.  | From homepage click on get started > From Recipe page click Addrecipe in navbar > fill in form click add recipe > you are forwarded back to recipes pages where you can see added recipe | Pass |
| - As a User I want the ability to edit recipe  | From homepage click on get started > From Recipe page click on edit recipe on any recipe card > fill in form click add recipe > you are forwarded back to recipes pages where you can see updated recipe | Pass |
| - As a User I want the ability to sign/register my own account where I can see recipes I have made  | From homepage click on get started > From Recipe page click MyHome in navbar > from sign in page either fill in details and click login or click  Sign up here. > if logged in you are forwarded to ypur own homepage where you can see your cocktail recipes or you are forwared to register page to register details and redirected back to sign in | Pass |
| - As a User I want the ability to delete a recipe  | From homepage click on get started > From Recipe page click on edit recipe on any recipe card > click delete recipe > you are forwarded back to recipes pages where you can see recipe has been deleted | Pass |
| - As a User I want the ability to sign/register my own account where I can see recipes I have made  | From homepage click on get started > From Recipe page click MyHome in navbar > from sign in page either fill in details and click login or click  Sign up here. > if logged in you are forwarded to ypur own homepage where you can see your cocktail recipes or you are forwared to register page to register details and redirected back to sign in | Pass |
| - As a User I want the ability to find a cocktail recipe based on the alcohol used  | From homepage click on get started > From Recipe page click Alcohols in navbar > click on alcohol card to see discription or click view to see cocktails | Pass | 
| - As a User I want to see a step by step guide on how to make a cocktail. | From homepage click on get started > From Recipe page click on veiw recipe on any recipe card > redirected to selected cocktail recipe page | Pass |
| - As a User I want to see the difficulty in making and how strong a cocktail is. | From homepage click on get started > From Recipe page click on veiw recipe on any recipe card > redirected to selected cocktail recipe page |
| - As a User I want to be able to see everything needed in order to make a cocktail correctly such as time length and ingredients. | From homepage click on get started > From Recipe page click on veiw recipe on any recipe card > redirected to selected cocktail recipe page |

The user joureny highlights all of the apps main feaures. Manual testing was done by following the user flow with mouse and keybord. In addition to this I also tested the app on all main browsers and devices to make sure the app is working corrctly 
and the user a great experience no matter what devise is being used to access the app. Browsers include: Firefox, Chrome, Internet explorer, yandex browser and Safari. Devices include: Iphone,Samsung phones an ipad and my laptop.

## Technologies used 
* I used [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) to create the base of my project.
* I used [CSS3](http://www.css3.info/) in order to implement custom styling in my project.
* I used [Python3](https://www.python.org/) 3 for the backend of my project along with the Flask Framework.
* I used [jQuery](https://jquery.com/) to simplify my JavaScript.
* I used [MongoDB](https://www.mongodb.com/) for my database to store all my data.
* I used [Materialize](https://materializecss.com/) for it's frontend frameworks for the style and layout of my project.
* I used [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) templating language to keep code clean.
* I used [Cloudinary](https://cloudinary.com/) to store high resolution images 
* I used [Heroku](https://en.wikipedia.org/wiki/Heroku) to deploy my application.
* I used [MoqUps](https://app.moqups.com/sign-up) to create the mockup version of my website, that can be found Here.
* I used [bcrypt](http://zetcode.com/python/bcrypt/) (a password-hashing function) to further protect private user information

### Validator used to check my code:

- [W3C HTML](https://validator.w3.org/)
- [W3C CSS3](https://jigsaw.w3.org/css-validator/)

### Issues found and fixed
- The alignment of the images on the cocktail recipe page was off due to images varying in sizes. I fixed this by reseaching a solution and finding it is a common fault that can be fixed by setting a fixed height.
- The index page content was not fixing onto the page and was carouselling along with the slides. This was fixed by digging deep into [stackoverflow](https://stackoverflow.com/) and finding a solution. 
- The Headings for all main pages where getting lost in the background image so I initailly used the brightness filter in css to dim the background image but from looking through templates and UX design pages i thought
adding a border in css for all headers would be a unique way to make the page pop aswell and for the userto have a better experience. This was confirmed by friends and family who tested the app.

### Things to improve in the Future
- The user will be able to access there own personal homepage that shows them the cocktails they created
- Give the user the abilty to share recipes on other platforms like twitter

## DEPLOYMENT
All code throughtout the build process, every bug fix, all corrections and ammendments have been commited to GitHub using [Version Control]().

All my commits and the full code for my project can be found on my GitHub Repository [found here]()

All work has been commited and deployed to Heroku [found here]()

### content
The content for the app was precured from [unsplash](https://unsplash.com/) a great platform for good quality images and a number of recipe websites and textbook guides 
- (https://www.thespruceeats.com/quick-guide-to-distilled-spirits-760713)
- (https://uk.thebar.com/cocktail-recipes/classic-cocktails)
-(https://www.socialandcocktail.co.uk/top-100-cocktails/)