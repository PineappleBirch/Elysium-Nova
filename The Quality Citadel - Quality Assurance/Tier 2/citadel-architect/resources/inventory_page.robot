*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${INVENTORY_URL}            https://www.saucedemo.com/inventory.html
${SORT_CONTAINER}           css:.product_sort_container
${FIRST_ITEM_NAME}          css:.inventory_item_name
${ADD_BACKPACK_BUTTON}      id:add-to-cart-sauce-labs-backpack
${CART_BADGE}               css:.shopping_cart_badge

*** Keywords ***
Verify User Is On Inventory Page
    Location Should Be    ${INVENTORY_URL}

Sort Items By
    [Arguments]    ${value}
    Select From List By Value    ${SORT_CONTAINER}    ${value}

Verify First Item Name Is
    [Arguments]    ${expected_name}
    ${actual_name}=    Get Text    ${FIRST_ITEM_NAME}
    Should Be Equal    ${actual_name}    ${expected_name}

Add Backpack To Cart
    Click Button    ${ADD_BACKPACK_BUTTON}

Verify Cart Badge Count Is
    [Arguments]    ${expected_count}
    ${actual_count}=    Get Text    ${CART_BADGE}
    Should Be Equal    ${actual_count}    ${expected_count}