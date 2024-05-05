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
