*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  KuusSeittema
    Set Password  salasana1
    Set Password Confirmation  salasana1
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  salasana1
    Set Password Confirmation  salasana1
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  KuusSeittema
    Set Password  sala1
    Set Password Confirmation  sala1
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  KuusSeittema
    Set Password  salasana
    Set Password Confirmation  salasana
    Click Button  Register
    Register Should Fail With Message  Password cannot consist of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  KuusSeittema
    Set Password  salasana1
    Set Password Confirmation  salasana2
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username is already taken


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
  Reset Application
  Create User  kalle  kalle123
  Go To Register Page