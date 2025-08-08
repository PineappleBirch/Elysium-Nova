*** Settings ***
Library           SeleniumLibrary
Resource          resources/login_page.robot
Resource          resources/inventory_page.robot

Suite Setup       Run Keyword    login_page.Open And Go To Login Page    ${BROWSER}    ${CHROME_OPTIONS}
Suite Teardown    Close Browser
Test Setup        login_page.Go To Login Page

*** Variables ***
${BROWSER}              Chrome
${CHROME_OPTIONS}       add_argument("--disable-features=PasswordLeakDetection")
${VALID_USER}           standard_user
${LOCKED_OUT_USER}      locked_out_user
${PASSWORD}             secret_sauce
${ERROR_LOCKED_OUT}     Epic sadface: Sorry, this user has been locked out.
${ERROR_NO_MATCH}       Epic sadface: Username and password do not match any user in this service
${ERROR_USER_REQUIRED}  Epic sadface: Username is required
${ERROR_PASS_REQUIRED}  Epic sadface: Password is required

*** Test Cases ***
TC-LOG-001: Successful Login
    [Tags]    Login    Positive
    login_page.Input Username    ${VALID_USER}
    login_page.Input Password    ${PASSWORD}
    login_page.Click Login Button
    inventory_page.Verify User Is On Inventory Page

TC-LOG-002: Failed Login with Locked Out User
    [Tags]    Login    Negative
    login_page.Input Username    ${LOCKED_OUT_USER}
    login_page.Input Password    ${PASSWORD}
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_LOCKED_OUT}

TC-LOG-003: Failed Login with Incorrect Password
    [Tags]    Login    Negative
    login_page.Input Username    ${VALID_USER}
    login_page.Input Password    wrong_password
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_NO_MATCH}

TC-LOG-004: Failed Login with Invalid Username
    [Tags]    Login    Negative
    login_page.Input Username    invalid_user
    login_page.Input Password    ${PASSWORD}
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_NO_MATCH}

TC-LOG-005: Failed Login with Empty Username
    [Tags]    Login    Negative
    login_page.Input Password    ${PASSWORD}
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_USER_REQUIRED}

TC-LOG-006: Failed Login with Empty Password
    [Tags]    Login    Negative
    login_page.Input Username    ${VALID_USER}
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_PASS_REQUIRED}

TC-LOG-007: Failed Login with Empty Credentials
    [Tags]    Login    Negative
    login_page.Click Login Button
    login_page.Verify Error Message Is    ${ERROR_USER_REQUIRED}

TC-INV-002: Verify product sort functionality (Name A to Z)
    [Setup]    Log In With Standard User
    [Tags]    Inventory    Positive
    inventory_page.Sort Items By    az
    inventory_page.Verify First Item Name Is    Sauce Labs Backpack

TC-INV-003: Verify product sort functionality (Name Z to A)
    [Setup]    Log In With Standard User
    [Tags]    Inventory    Positive
    inventory_page.Sort Items By    za
    inventory_page.Verify First Item Name Is    Test.allTheThings() T-Shirt (Red)

TC-INV-006: Verify "Add to Cart" functionality
    [Setup]    Log In With Standard User
    [Tags]    Inventory    Positive
    inventory_page.Add Backpack To Cart
    inventory_page.Verify Cart Badge Count Is    1

*** Keywords ***
Log In With Standard User
    login_page.Go To Login page
    login_page.Input Username    ${VALID_USER}
    login_page.Input Password    ${PASSWORD}
    login_page.Click Login Button
    inventory_page.Verify User Is On Inventory Page