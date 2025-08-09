*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${URL}                  https://www.saucedemo.com/
${BROWSER}              Chrome
${VALID_USER}           standard_user
${LOCKED_OUT_USER}      locked_out_user
${PASSWORD}             secret_sauce
${ERROR_CONTAINER}      css:h3[data-test="error"]
${ERROR_LOCKED_OUT}     Epic sadface: Sorry, this user has been locked out.
${ERROR_NO_MATCH}       Epic sadface: Username and password do not match any user in this service
${ERROR_USER_REQUIRED}  Epic sadface: Username is required
${ERROR_PASS_REQUIRED}  Epic sadface: Password is required

*** Test Cases ***
TC-LOG-002: Failed Login with Locked Out User
    [Tags]    Login    Negative
    Input Username    ${LOCKED_OUT_USER}
    Input Password    ${PASSWORD}
    Click Login Button
    Verify Error Message    ${ERROR_LOCKED_OUT}
    [Teardown]    Go To    ${URL}

TC-LOG-003: Failed Login with Incorrect Password
    [Tags]    Login    Negative
    Input Username    ${VALID_USER}
    Input Password    wrong_password
    Click Login Button
    Verify Error Message    ${ERROR_NO_MATCH}
    [Teardown]    Go To    ${URL}

TC-LOG-004: Failed Login with Invalid Username
    [Tags]    Login    Negative
    Input Username    invalid_user
    Input Password    ${PASSWORD}
    Click Login Button
    Verify Error Message    ${ERROR_NO_MATCH}
    [Teardown]    Go To    ${URL}

TC-LOG-005: Failed Login with Empty Username
    [Tags]    Login    Negative
    Input Password    ${PASSWORD}
    Click Login Button
    Verify Error Message    ${ERROR_USER_REQUIRED}
    [Teardown]    Go To    ${URL}

TC-LOG-006: Failed Login with Empty Password
    [Tags]    Login    Negative
    Input Username    ${VALID_USER}
    Click Login Button
    Verify Error Message    ${ERROR_PASS_REQUIRED}
    [Teardown]    Go To    ${URL}

TC-LOG-007: Failed Login with Empty Credentials
    [Tags]    Login    Negative
    Click Login Button
    Verify Error Message    ${ERROR_USER_REQUIRED}
    [Teardown]    Go To    ${URL}

TC-LOG-001: Successful Login
    [Tags]    Login    Positive
    Input Username    ${VALID_USER}
    Input Password    ${PASSWORD}
    Click Login Button
    Location Should Be    https://www.saucedemo.com/inventory.html

TC-INV-002: Verify product sort functionality (Name A to Z)
    [Tags]    Inventory    Positive
    Select From List By Value    css:.product_sort_container    az
    ${first_item_name}=    Get Text    css:.inventory_item_name
    Should Be Equal    ${first_item_name}    Sauce Labs Backpack

TC-INV-003: Verify product sort functionality (Name Z to A)
    [Tags]    Inventory    Positive
    Select From List By Value    css:.product_sort_container    za
    ${first_item_name}=    Get Text    css:.inventory_item_name
    Should Be Equal    ${first_item_name}    Test.allTheThings() T-Shirt (Red)

TC-INV-006: Verify "Add to Cart" functionality
    [Tags]    Inventory    Positive
    Click Button    id:add-to-cart-sauce-labs-backpack
    ${cart_badge}=    Get Text    css:.shopping_cart_badge
    Should Be Equal    ${cart_badge}    1

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}

Input Username
    [Arguments]    ${username}
    Input Text    id:user-name    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id:password    ${password}

Click Login Button
    Click Button    id:login-button

Verify Error Message
    [Arguments]    ${expected_error}
    Wait Until Element Is Visible    ${ERROR_CONTAINER}
    Element Text Should Be          ${ERROR_CONTAINER}    ${expected_error}