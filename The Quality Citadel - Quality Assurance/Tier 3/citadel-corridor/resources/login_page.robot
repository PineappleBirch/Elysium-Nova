*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}            https://www.saucedemo.com/
${USERNAME_FIELD}       id:user-name
${PASSWORD_FIELD}       id:password
${LOGIN_BUTTON}         id:login-button
${ERROR_CONTAINER}      css:h3[data-test="error"]

*** Keywords ***
Open And Configure Browser
    [Arguments]    ${browser_name}
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Create Webdriver    ${browser_name}    options=${chrome_options}
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