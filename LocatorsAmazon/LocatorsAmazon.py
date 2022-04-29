from selenium.webdriver.common.by import By

#Main Page
goToSignInButton = (By.ID, "nav-link-accountList")

#SignIn Page
emailUsername = (By.ID, "ap_email")
continueButton = (By.ID, "continue")

#Password Page
passwordInput = (By.ID, "ap_password")
rememberMe = (By.NAME, "rememberMe")
signInButton = (By.ID, "signInSubmit")

#Home Page
cardButton = (By.ID, "nav-cart-count-container")

#Card Page
delete1Product = (By.XPATH, "(//input[@class='a-color-link'])[1]")
products_loc = (By.XPATH, "//img[@class='sc-product-image']")
deleteAllProducts = (By.XPATH, "//input[@class='a-color-link']")
card_count = (By.ID, "nav-cart-count")
#randomProduct = ()

#a-fixed-left-grid-col a-float-left sc-product-image-desktop a-col-left
#a-fixed-left-grid-inner