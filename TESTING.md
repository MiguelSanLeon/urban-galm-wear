go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
- [Accesibility](#accesibility)
- [Tools Testing](#tools-testing)
- [Manual Testing](#manual-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Navbar Testing](#navbar-testing)
    - [Home Page Testing](#home-page-testing)
    - [Product Page Testing](#product-page-testing)
    - [Product Details Page Testing](#product-details-page-testing)
    - [Bag Testing](#bag-testing)
    - [Checkout Testing](#checkout-testing)
    - [Checkout Success Testing](#checkout-success-testing)
    - [Contact Us Testing](#contact-us-testing)
    - [About Us Testing](#about-us-testing)
    - [Privacy Policy Testing](#privacy-policy-testing)
    - [404 Page Testing](#404-page-testing)
    - [Register Page Testing](#register-page-testing)
    - [Login Page Testing](#login-page-testing)
    - [Logout Page Testing](#logout-page-testing)
    - [Product Management Page Testing](#product-management-page-testing)
    - [Wishlist Page Testing](#wishlist-page-testing)

## Code Validation
### HTML

|Page|Validator|Result|
| --- | --- | --- |
| Home Page | ![home](documentation_assets/testing/home.png) | <mark>Pass<mark> |
| Register Page | ![register](documentation_assets/testing/register.png) | <mark>Pass<mark> |
| My Profile Page | ![my-profile](documentation_assets/testing/my-profile.png) | <mark>Pass<mark> |
| Login Page | ![login](documentation_assets/testing/login.png) | <mark>Pass<mark> |
| Logout Page | ![logout](documentation_assets/testing/logout.png) | <mark>Pass<mark> |
| Wishlist Page | ![wishlist](documentation_assets/testing/wishlist.png) | <mark>Pass<mark> |
| Product Management Page | ![product-management](documentation_assets/testing/product-management.png) | <mark>Pass<mark> |
| Products Page | ![products-page](documentation_assets/testing/products.png) | <mark>Pass<mark> |
| Product Details Page | ![product-details](documentation_assets/testing/product-detail.png) | <mark>Pass<mark> |
| Bag Page | ![bag](documentation_assets/testing/bag.png) | <mark>Pass<mark> |
| Checkout Page | ![checkout](documentation_assets/testing/checkout.png) | <mark>Pass<mark> |
| Checkout Success Page | ![checkout-success](documentation_assets/testing/checkout-success.png) | <mark>Pass<mark> |
| Contact Us Page | ![contact-us](documentation_assets/testing/contact-us.png) | <mark>Pass<mark> |
| About Us Page | ![about-us](documentation_assets/testing/about-us.png) | <mark>Pass<mark> |
| Privacy Policy Page | ![privacy-policy](documentation_assets/testing/privacy-policy.png) | <mark>Pass<mark> |
| 404 Page | ![404](documentation_assets/testing/404.png) | <mark>Pass<mark> |

### CSS

|File|Validator|Result|
| --- | --- | --- |
| base.css | ![base.css](documentation_assets/testing/base.png) | <mark>Pass<mark> |
| checkout.css | ![checkout.css](documentation_assets/testing/checkout-css.png) | <mark>Pass<mark> |
| profile.css | ![profile.css](documentation_assets/testing/profile-css.png) | <mark>Pass<mark> |

### JavaScript

|File|Validator|Result|Comments|
| --- | --- | --- | --- |
| stripe_elements.js | ![stripe-elements](documentation_assets/testing/stripe-elements.png) | <mark>Pass<mark> | Two undefined variables |
| countryfield.js | ![countryfield](documentation_assets/testing/countryfield.png) | <mark>Pass<mark> | One undefined variables |

### Python


|File|App|Validator|Result|Comments|
| --- | --- | --- | --- | --- |
| apps.py | Bag | ![bag-apps](documentation_assets/testing/bag-apps.py.png) | <mark>Pass<mark> | |
| contexts.py | Bag | ![bag-apps](documentation_assets/testing/bag-contexts.png) | <mark>Pass<mark> | |
| urls.py | Bag | ![bag-urls](documentation_assets/testing/bag-urls.png) | <mark>Pass<mark> | |
| views.py | Bag | ![bag-views](documentation_assets/testing/bag-views.png) | <mark>Pass<mark> | |
| admin.py | Checkout | ![checkout-admin](documentation_assets/testing/checkout-admin.png) | <mark>Pass<mark> | |
| apps.py | Checkout |![checkout-apps](documentation_assets/testing/checkout-apps.png) | <mark>Pass<mark> | |
| forms.py | Checkout |![checkout-forms](documentation_assets/testing/checkout-forms.png) | <mark>Pass<mark> | |
| models.py | Checkout |![checkout-models](documentation_assets/testing/checkout-models.png) | <mark>Pass<mark> | |
| signals.py | Checkout |![checkout-signals](documentation_assets/testing/checkout-signals.png) | <mark>Pass<mark> | |
| urls.py | Checkout |![checkout-urls](documentation_assets/testing/checkout-urls.png) | <mark>Pass<mark> | |
| views.py | Checkout |![checkout-views](documentation_assets/testing/checkout-views.png) | <mark>Pass<mark> | File 80 to long: not possible to fix the line |
| admin.py | Home |![home-admin](documentation_assets/testing/home-admin.png) | <mark>Pass<mark> | |
| apps.py | Home |![home-apps](documentation_assets/testing/home-apps.png) | <mark>Pass<mark> | |
| forms.py | Home |![home-forms](documentation_assets/testing/home-forms.png) | <mark>Pass<mark> | |
| models.py | Home |![home-models](documentation_assets/testing/home-models.png) | <mark>Pass<mark> | |
| urls.py | Home |![home-urls](documentation_assets/testing/home-urls.png) | <mark>Pass<mark> | |
| views.py | Home |![home-views](documentation_assets/testing/home-views.png) | <mark>Pass<mark> | |
| admin.py | Newsletter |![newsletter-admin](documentation_assets/testing/newsletter-admin.png) | <mark>Pass<mark> | |
| apps.py | Newsletter |![newsletter-apps](documentation_assets/testing/newsletter-apps.png) | <mark>Pass<mark> | |
| forms.py | Newsletter |![newsletter-forms](documentation_assets/testing/newsletter-forms.png) | <mark>Pass<mark> | |
| models.py | Newsletter |![newsletter-models](documentation_assets/testing/newsletter-models.png) | <mark>Pass<mark> | |
| urls.py | Newsletter |![newsletter-urls](documentation_assets/testing/newsletter-urls.png) | <mark>Pass<mark> | |
| views.py | Newsletter |![newsletter-views](documentation_assets/testing/newsletter-views.png) | <mark>Pass<mark> | |
| admin.py | Products |![products-admin](documentation_assets/testing/products-admin.png) | <mark>Pass<mark> | |
| apps.py | Products |![products-apps](documentation_assets/testing/products-apps.png) | <mark>Pass<mark> | |
| forms.py | Products |![products-forms](documentation_assets/testing/products-forms.png) | <mark>Pass<mark> | |
| models.py | Products |![products-models](documentation_assets/testing/products-models.png) | <mark>Pass<mark> | |
| urls.py | Products |![products-urls](documentation_assets/testing/products-urls.png) | <mark>Pass<mark> | |
| views.py | Products |![products-views](documentation_assets/testing/products-views.png) | <mark>Pass<mark> | |
| widgets.py | Products |![products-widgets](documentation_assets/testing/products-widgets.png) | <mark>Pass<mark> | line 9 too long |
| apps.py | Profiles |![profiles-apps](documentation_assets/testing/profiles-apps.png) | <mark>Pass<mark> | |
| forms.py | Profiles |![profiles-forms](documentation_assets/testing/profiles-forms.png) | <mark>Pass<mark> | |
| models.py | Profiles |![profiles-models](documentation_assets/testing/profiles-models.png) | <mark>Pass<mark> | |
| urls.py | Profiles |![profiles-urls](documentation_assets/testing/profiles-urls.png) | <mark>Pass<mark> | |
| views.py | Profiles |![profiles-views](documentation_assets/testing/profiles-views.png) | <mark>Pass<mark> | |
| settings.py | urban_glam_wear |![urban-glam-wear-settings](documentation_assets/testing/settings.png) | <mark>Pass<mark> | 31, 86, 146, 149, 152, 155 lines too long |
| urls.py | urban_glam_wear |![urban-glam-wear-urls](documentation_assets/testing/ugw-urls.png) | <mark>Pass<mark> | |
| views.py | urban_glam_wear |![urban-glam-wear-views](documentation_assets/testing/ugw-views.png) | <mark>Pass<mark> | |
| apps.py | Wishlist |![wishlist-apps](documentation_assets/testing/wishlist-apps.png) | <mark>Pass<mark> | |
| urls.py | Wishlist |![wishlist-urls](documentation_assets/testing/wishlist-urls.png) | <mark>Pass<mark> | |
| views.py | Wisklist |![wishlist-views](documentation_assets/testing/wishlist-views.png) | <mark>Pass<mark> | 

## Accesibility

|PAge|Lighthouse Report|
| --- | --- |
| Home | ![home-lhr](documentation_assets/lighthouse/home-lhr.png)|
| Registration | ![registration-lhr](documentation_assets/lighthouse/register-lhr.png)|
| My Profile | ![my-profile-lhr](documentation_assets/lighthouse/my-profile-lhr.png)|
| Login | ![login-lhr](documentation_assets/lighthouse/login-lhr.png)|
| Logout | ![logout-lhr](documentation_assets/lighthouse/logout-lhr.png)|
| Wishlist | ![wislist-lhr](documentation_assets/lighthouse/wishlist-lhr.png)|
| Product management | ![product-management-lhr](documentation_assets/lighthouse/product-management-lhr.png)|
| Products | ![products-lhr](documentation_assets/lighthouse/products-lhr.png)|
| Product Details | ![product-details-lhr](documentation_assets/lighthouse/product-details-lhr.png)|
| Bag | ![bag-lhr](documentation_assets/lighthouse/bag-lhr.png)|
| Checkout | ![checkout-lhr](documentation_assets/lighthouse/checkout-lhr.png)|
| Checkout-success | ![checkout-success-lhr](documentation_assets/lighthouse/checkout-success-lhr.png)|
| Contact Us | ![contact-us-lhr](documentation_assets/lighthouse/contact-us-lhr.png)|
| About Us | ![about-us-lhr](documentation_assets/lighthouse/about-us-lhr.png)|
| Privacy Policy | ![privacy-policy-lhr](documentation_assets/lighthouse/privacy-policy-lhr.png)|
| 404 | ![404-lhr](documentation_assets/lighthouse/404-lhr.png)|

## Tools Testing

[Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.

## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail |
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <mark>Pass<mark> 
Safari | No appearance, responsiveness nor functionality issues. | <mark>Pass<mark> 
Mozilla Firefox | No responsiveness nor functionality issues.| <mark>Pass<mark> 
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <mark>Pass<mark> 

### Navbar Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Navbar | Click on the logo | Redirects to Home | Pass | The mobile version has a Home link in the dropdown menu |
|  | Click on the categorires links in navbar | Open the dropdown menus  | Pass |   |
|  | Click the links inside the dropdown menus | Redirects to correct page | Pass |  |
|  | Click on My Account icon | Open the dropdown menu | Pass |  |
|  | Click on the links in My account dropdown menu | Redirect to correct page | Pass |  |
|  | Click on Bag icon | Redirect to Shopping bag page  | Pass |  |
| Search bar | Type keywords | Return correct results | Pass |  |

### Home Page Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Home | Click on Go Shopping button | Redirects to products page | Pass |  |
| Newsletter | Type a valid email and click on subscribe button | Show a succes message  | Pass | when typing a not valid email the user receive feedback messages showing what is wrong with the email entered 
| Footer | Click on Contact Us button | Redirects to correct page | Pass |  |
|  | Click on About Us link | Redirects to correct page | Pass |  |
|  | Click on Privacy Policy link | Redirects to correct page | Pass |  |
|  | Click on Social Media icons | Redirects to the correct page | Pass |  |

### Product Page Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Product page | Use the Sorting menu | Reorder the product list | Pass |  |
| Product card | Clck on Details button | Redirects to Product details page | Pass |  |
|  | Click on Add to wishlist button | Shows a success message | Pass | It also change the Add to wishlist button text to Remove from Wishlist in the product card |
|  | Click on Remove from wishlist button | Shows a success message | Pass | IT also change the Remove from wishlist button text to Add to wishlist button |

### Product Details Page Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Product Details card | use the dropdown menu for size selection | Change the actual selection | Pass |  |
|  | Use the Quantity up/down arrows to add/rest units | Change the quantity number adding/removing one when clicked | Pass |  |
|  | Type a correct number in Quantity input area | Change the quantity number | Pass | When typing something different from a number the user receive feedback messages to enter a correct number. It also has a top quantity of 99 units |
|  | Click on Add to wishlist button | Shows a success message | Pass | It also change the Add to wishlist button text to Remove from Wishlist in the product card |
|  | Click on Remove from wishlist button | Shows a success message | Pass | IT also change the Remove from wishlist button text to Add to wishlist button |
|  | Click on Add to bag button | Shows a Succes message with your bag content and a button to go to Secure Checkout | Pass | The button in the Success message is redirecting correctly to Checkout page |
|  | Click on Keep Shopping button | Redirects to Products page | Pass |  |
| Only for Admin Users | Click on Edit button | Redirects to Product management Edit page with all the product data displayed on the form. | Pass | It also shows an Alert message to the admin that said "You are editing Yoga set |
|  | Click on Delete button | Show a modal Asking the admin for deletion confirmation | Pass | The App shows an abnormal behavior when clicking yes in the modal showing a message with the text undefined. But the product is deleted properly and no other issues are detected |

### Bag Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Product info | Click on Quantity add/remove arrows | Add/remove 1 from acutal number | Pass | input a number works as well and still has a limit of 99 products |
|  | Click on Update after changing the quantity number | Change the quantity number and update the subtotal | Pass |  |
|  | Click on Remove | Remove the product from the bag | Pass |  |
|  | Click on Keep Shopping button | Redirects the user to Products page | Pass |  |
|  | Click on Secure Checkout button | Redirects the user to Checkout page | Pass |  |

### Checkout Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Checkout form | Input incorrect data to form | Shows feedback messages to the user to fix the problem  | Pass |  |
|  | Click on Adjust Bag button | Redirects the user to Checkout page | Pass |  |
|  | Click on complete order button | Redirects the user to Checkout Success page | Pass | It also shows a success message informing the user that the order was processed and an email will be sent to the users email |

### Checkout Success Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|  | Click on Have a look button | Redirects user to Products page filtered by New arrivals category | Pass |  |

### Contact Us Testing
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Contact us form |  Input incorrect data to form | Shows feedback messages to the user to fix the problem | Pass |  |
|  | click on Submit button |  |  |  |
