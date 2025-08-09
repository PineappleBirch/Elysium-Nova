*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open The Browser
    [Arguments]    ${browser_name}
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Create Webdriver    ${browser_name}    options=${options}
    Go To    ${LOGIN_URL}

*** Keywords ***
Open And Go To Login Page
    [Arguments]    ${browser_name}    ${options_str}
    Open Browser    url=${LOGIN_URL}    browser=${browser_name}    options=${options_str}

Go To Login Page
    Go To    ${LOGIN_URL}

Input Username
    [Arguments]    ${username}
    Input Text    ${USERNAME_FIELD}    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    ${PASSWORD_FIELD}    ${password}

Click Login Button
    Click Button    ${LOGIN_BUTTON}

Verify Error Message Is
    [Arguments]    ${expected_error}
    Wait Until Element Is Visible    ${ERROR_CONTAINER}
    Element Text Should Be          ${ERROR_CONTAINER}    ${expected_error}