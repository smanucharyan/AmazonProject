from selenium.webdriver.common.by import By

#Main Page
goToSignInButton = (By.ID, "nav-link-accountList")

#SignIn Page
emailUsername = (By.ID, "ap_email")
continueButton = (By.ID, "continue")
wrongEmail = (By.TAG_NAME, "li")
wrongEmailAnotherSolution = (By.XPATH, "//div[@class='a-alert-content']")

#Password Page
passwordInput = (By.ID, "ap_password")
rememberMeCheckbox = (By.NAME, "rememberMe")
signInButton = (By.ID, "signInSubmit")
wrongPass = (By.TAG_NAME, "li")
wrongPassAnotherSolution = (By.XPATH, "//div[@class='a-alert-content']")

#Home Page
cardButton = (By.ID, "nav-cart-count-container")
searchProduct = (By.ID, "twotabsearchtextbox")
menu = (By.ID, "nav-link-accountList")
logout = (By.ID, "nav-item-signout")

#Cart Page
delete1Product = (By.XPATH, "(//input[@class='a-color-link'])[1]")
productsLoc = (By.XPATH, "//img[@class='sc-product-image']")
cardCount = (By.ID, "nav-cart-count")
cartMessage = (By.XPATH, "//div[@class='a-row sc-cart-header']")

#Product Page
productOpen = (By.XPATH, "(//img[@class='s-image'])[1]")
addCard = (By.ID, "add-to-cart-button")

