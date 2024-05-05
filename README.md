# URBAN GLAM WEAR

![URBAN-GLAM-WEAR mock up images](documentation_assets/mock-up.png)

## Introduction
[Link to deployed site](https://book-heaven-e537b3f88787.herokuapp.com/)
Urban Glam Wear is an online clothes shopping site designed for urban fashionist and created using Django, Python, HTML, CSS JavaScript, Amazon Web Services and Stripe.

## Table of Contents

- [URBAN GLAM WEAR](#urban-glam-wear)
    - [Introduction](#introduction)
    - [Table of Contents](#table-of-contents)
    - [User Experience (UX)](#user-experience-ux)
        - [Project Goals](#project-goals)
        - [User Stories](#user-stories)
        - [Strategy Table](#strategy-table)
    - [Scope](#scope)
        - [Phase 1](#phase-1)
        - [Phase 2](#phase-2)
        - [Phase 3](#phase-3)
        - [Phase 4](#phase-4)
    - [Structure](#structure)
        - [Database Model](#database-model)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Wireframes](#wireframes)
    - [Features](#features)
        - [General](#general)
        - [Home Page](#home-page)
        - [Register Page](#register-page)
        - [My Profile Page](#my-profile-page)
        - [Login & Logout Pages](#login--logout-pages)
        - [Wishlist Page](#wishlist-page)
        - [Product Management](#product-management)
        - [Products Page](#products-page)
        - [Product Detail Page](#product-detail-page)
        - [Bag Page](#bag-page)
        - [Checkout Page](#checkout-page)
        - [Checkout Success Page](#checkout-success-page)
        - [Contact Us Page](#contact-us-page)
        - [About Us Page](#about-us-page)
        - [Privacy Policy Page](#privacy-policy-page)
        - [404 Page](#404-page)
    - [Technologies Used](#technologies-used)
        - [Languages Used](#languages-used)
        - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
        - [Packages / Dependencies Installed](#packages--dependencies-installed)
    - [Testing](#testing)
        - [Code Validation](#code-validation)
            - [HTML](#html)
            - [CSS](#css)
            - [Python](#python)
        - [Accesibility](#accesibility)
        - [Tools Testing](#tools-testing)
        - [Manual Testing](#manual-testing)
            - [Browser Compatibility](#browser-compatibility)
            - [Device Compatibility](#device-compatibility)
            - [Navbar Testing](#navbar-testing)
            - [Footer Testing](#footer-testing)
            - [Search Bar Testing](#search-bar-testing)
            - [Product Page Testing](#product-page-testing)
            - [Product Detail Page Testing](#product-detail-page-testing)
            - [Bag Testing](#bag-testing)
            - [Checkout Page Testing](#checkout-page-testing)
            - [Contact Us Page Testing](#contact-us-page-testing)
            - [Privacy Policy Page Testing](#privacy-policy-page-testing)
            - [404 Page Testing](#404-page-testing)
            - [Register Page Testing](#register-page-testing)
            - [Login Page Testing](#login-page-testing)
            - [Logout Page Testing](#logout-page-testing)
            - [Product Management Page Testing](#product-management-page-testing)
            - [Wishlist Page Testing](#wishlist-page-testing)
    - [Deployment](#deployment)
        - [Deploying on Heroku](#deploying-on-heroku)
    - [Credits](#credits)
        - [Content](#content)
        - [Media](#media)
        - [Code](#code)
    - [Known Bugs](#known-bugs)
    - [Acknowledgements](#acknowledgements)


## User Experience (UX)

Not all Customers enjoy a day of shopping in a crowded mall. Other customers do not have the time or means to go shopping in a physical store. Many customers enjoy searching for their favorite clothes online without having to leave their home. This Website is for all of them.

### Project Goals

- Responsive design to make the website accessible on different screen sizes.
- Well-structured website and easy to navigate.
- Provide security in access to user data and their bookings.
- Provide a search bar and a navbar to allow the users to look for products by categories.
- Allows CRUD functionality in bag page and product management page.
- Provide users with a secure checkout system.

### User Stories

- USER STORIE 1: As a shopper, I can browse a list of available products so that I can explore the offerings and find items of interest.
- USER STORIE 2: As a shopper, I can apply filters to products by category, price, and features so that I can narrow down my search and find products that meet my preferences.
- USER STORIE 3: As a shopper, I can view detailed product information, including images and descriptions, so that I can make informed decisions about my purchases.
- USER STORIE 4: As a shopper, I can add products to my shopping cart so that I can keep track of items I intend to purchase.
- USER STORIE 5: As a shopper, I can view and edit the contents of my shopping cart so that I can make adjustments before finalizing my purchase.
- USER STORIE 6: As a shopper, I want to receive a confirmation email after making a purchase so that I have a record of my transaction.
- USER STORIE 7: As a registered user, I can create an account so that I can track my order history.
- USER STORIE 8: As a registered user I can edit my shipping/billing information and my contact information so that update my information in my profile.
- USER STORIE 9: As a shopper, I can review my order summary during the checkout process so that I can confirm the accuracy of my selected items and their quantities.
- USER STORIE 10: As an administrator, I can manage the product catalog by adding, editing, or removing products so that the website reflects the current inventory.
- USER STORIE 11: As an administrator, I can receive email notifications about new orders so that I can stay informed about incoming business.
- USER STORIE 12: As a User I can Enter my payment information so that Check out easily and with no problems.
- USER STORIE 13: As a User I can add products to my wish list so that I can save my favorite items for a future purchase.
- USER STORIE 14: As a User I can receive a newsletter so that I can be updated about all the discounts and arrivals.
- USER STORIE 15: As a User I can use a contact form so that I can make questions about products, discounts and other topics of my interest.

### Strategy Table

Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Responsive design | 5 | 5
Display Products in a list | 5 | 5
Account registration | 5 | 5
User profile | 5 | 5
Admin Product Management | 5 | 5
Add products to bag | 5 | 5
Remove products from bag | 5 | 5
Update products in the bag | 5 | 5
Provides a checkout page | 5 | 5 
Contact form | 3 | 4
wishlist | 3 | 4 
Newsletter Subscription | 3 | 3
Avoid double checkout | 5 | 4
checkout email | 3 | 3
Total | 62 | 63

## Scope

### Phase 1
- Responsive design
- Display products in a list
- Add products to bag
- Remove products from bag
- Update products in bag
### Phase 2
- Account registration
- User profile
- Admin product management
- Provides a checkout page
### Phase 3
- Avoid double checkout
- Checkout email
### Phase 4
- Wishlist
- Newsletter subscription
- Contact form
## Structure
### Database Model
![Db-model](documentation_assets/ugw_diagram.png)
### Colour Scheme
![Palette](documentation_assets/palette.png)
### Typography
The Website has been created with 2 fonts. The main one is Playfair display.
For Titles and Branding the choosen font is Sedgwick Ave Display.
![Playfair-Display](documentation_assets/playfair_display.png)
![Sedgwick-Ave-Display](documentation_assets/sedgwick_ave_display.png)
### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to create all the wireframes for desktop and mobile views for this project.

Page | Wireframe
--- | ---
home | ![homepage-wireframe](documentation_assets/home%20_page%20_wf.png)
My profile |  ![my-profile-wireframe](documentation_assets/my_profile_page_wf.png)
Sign Up |  ![sign-up-wireframe](documentation_assets/sign_up_page_wf.png)
Sign In |  ![sign-in-wireframe](documentation_assets/sign_in_page_wf.png)
Sign Out |  ![sign-out-wireframe](documentation_assets/sign_out_page_wf.png)
Wishlist |  ![wishlist-wireframe](documentation_assets/wishlist_page_wf.png)
Products page |  ![products-page-wireframe](documentation_assets/product_page_wf.png)
Product Detail |  ![product-detail-wireframe](documentation_assets/product_details_page_wf.png)
Product management | ![product-management-wireframe](documentation_assets/product_management_page_wf.png)
Shopping bag |  ![shopping-bag-wireframe](documentation_assets/shopping_bag_page_wf.png)
Checkout |  ![checkout-wf-wireframe](documentation_assets/checkout_page-wf.png)
Checkout success | ![checkout-success-wf-wireframe](documentation_assets/checkout_success_wf.png)
About us |  ![about-us-wf-wireframe](documentation_assets/about_us_page_wf.png)
Contact us |  ![contact-us-wf-wireframe](documentation_assets/contact_us_page_wf.png)
Privacy Policy |  ![privacy-policy-wf-wireframe](documentation_assets/privacy_policy_page_wf.png)

## Features

### General

This web application has been designed with bootstrap5 to be responsive across all devices.

- Navigation bar:
![navigation-bar-img](documentation_assets/navigation-bar.png)
    - The navigation bar contain links with dropdown menus to navigate through all products and categories in the store.
    - It also contains 2 icons, my account icon with a dropdown menu with all the options for account management. When no user is logged in the dropdown menu shows a link for registration and a link to log in.
    When the user is logged in the dropdown menu shows a link to My profile page, a link to the Wishlist page and the log out link.
    If the user is an admin it also provide a link to Product management page.
    The shopping bag icon is linked to the shopping bag page and shows the grand total under the icon.
    - The Urban Glam Wear banner is linked to home page.
    - There is a search bar that helps users to find products easily.
    - At the very bottom of the navigation bar there is a banner that shows the minimum order cost for free delivery.

- The footer:
![footer-img](documentation_assets/footer.png)
    - The footer contains links to 4 social media, Facebook, Twitter(X), Instagram and LinkedIn.
    - The user can navigate to Contact us page using a button.
    - There are two links that provide access to About us page and Privacy policy page.
    - The footer also shows an Urban Glam Wear banner and the stripe banner. At the very bottom ther is a copyright banner.

### Home Page

![home-page-img](documentation_assets/homepage-img.png)

    -The home page contains the navigation bar, the footer and a section with some usefull information and the Newsletter subscription section.
    -Under the navigation bar there is a button, to access the products page, over a graffiti background image.

### Register Page

![register-page-img](documentation_assets/register-page-img.png)

- The email is the primary key for the registration process
- Password1 and Password2 must match.
- The password needs to contain both letters and numbers and cannot be a commonly used password.
- All error messages will be displayed in the form to provide correct feedback to the user in case something went wrong during the registration process.
- When the process is finished, the user will receive a successful message.

![register-page-error-img](documentation_assets/register-page-error-img.png)

### My Profile Page

![my-profile-page-img](documentation_assets/my-profile-page-img.png)

    - This profile page is divided in tu columns:
        - The first column contains all the delivery information and the user can update this information using the update button below the form.
        - The second column contains all the order history providing some usefull information about the orders and also a button to visit the order summary itself.

### Login and Logout Pages

![login-page-img](documentation_assets/login-page-img.png)

    -This page contains the Django form for sign in where the user can login using the email address provided or the Username
    - There is a checking box if the user wants the page to remember the login information.
    - There are two buttons, one that redirect the user to the home page and the other to Sign in with the credential provided.
    - At the very bottom of the form there is a link to reset the password.

![logout-page-img](documentation_assets/logout-page-img.png)

![password-reset-img](documentation_assets/password-reset-img.png)

![password-reset-confirmation-img](documentation_assets/password-reset-confirmation-img.png)

### Wishlist Page

![wishlist-page-img](documentation_assets/wishlist-page-img.png)

    - The wishlist is a simple template that use a carousel to show all the users wishlist products.
    - The cards shows all details and image of the product and a button to navigate to the products page.

### Product Management

![product-management-page-img](documentation_assets/product-management-page-img.png)

    - The product management page contains a form that allows the admin user to Add new products to the database filling all the necesary inputs.
    -There is an Add product button to add the product to the database and a cancel button that redirect the user to the products page.

### Products Page

![Products-page-img](documentation_assets/products-page-img.png)

    - The Products Page is a list of all products displayed in horizontal cards that contains all the product data divided in 2 columns:
        - The first column contains the picture of the product, the name, rate, carbon footprint, category and description.
        - The second column contains the price, if the product has free shipping itself, a button to the product details page and the Add to wish list button. When the product is already in the wishlist, the button text change to Remove from wishlist, giving the user the posibility to remove the product from the user wishlist.
        - At the upper-right corner of the product list the user can use a dropdown menu to sort the list with different filter.

### Product Detail Page

![product-details-page-img](documentation_assets/product-details-page-img.png)

    - The product detail page shows all product details in a card where th user can have a clear view of the product with an image, a description, price, rate, carbon footprint and category.
    - The user can also pick the product size and quantity to put it inside the bag by using the "Add to bag" button.
    - The user can also Add the product to the wishlist or come back to the products page by using the "Keep shopping" button.
    - If the user is an admin the product page also shows an "Edit" button to change the details of this product or delete the product from the database by using the "Delete" button.

### Bag Page

![bag-page-img](documentation_assets/bag-page-img.png)

    - The bag page contains a list of products inside a table displaying the product image, the name and size, the price, the quantity and the subtotal for each product.
    - The quantity of the listed product can be change by using the input text box and the button "Update". It can be removed from the bag by using the "Remove" button.
    - At the end of the list the page shows the bag total, the delivery total and the grand total.
    - The users can leave the bag using the "Keep Shopping" button or go to the checkout page by clicking on the "Secure Checkout" button.

### Checkout Page

![checkout-page-img](documentation_assets/checkout-page-img.png)

    -The Checkout page is divided in 2 columns:
        - The first column shows a form where the user can change the delivery information. At the button of this form the user can pay by using a credit or debit card. 
        -The second column shows the order summary with the items details, images and the order total, delivery total and grand total.
    - Under the first colum the user can find two button, "adjust bag" to go back to bag page and "Complete Order" to pay for the order shown in the order summary column.

### Checkout Success Page

![checkout-succces-page-img](documentation_assets/checkout-success-page-img.png)

    - The Checkout Success page shows a summary of the order.
    - The user will recieve an email with all the details of the order shown in the page.
    - There is a button below the summary that redirects the user to the products page, filtered for new arrivals.

### Contact Us Page

![contact-us-page-img](documentation_assets/contact-us-page-img.png)

   - The Contact Us page is a custom form where the user can send a message to the web page admin.
   - The form only needs a name, an email address to contact back the user and the message body.
   - Under the form the user can find a "Submit" button that send all data to the database. 

### About Us Page

![about-us-page-img](documentation_assets/about-us-page-img.png)

    -The About Us page shows a short description of the UWG physical shop with a picture and under this text the user can find the contact details for the physical shop including address, phone and email address.

### Privacy Policy Page

![privacy-policy-page-img](documentation_assets/privacy-policy-page-img.png)

    - This page shows a legal text with all the privacy policy for this web page.

