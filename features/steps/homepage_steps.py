from behave import given, when, then
from lib.helpers.env_config import  EnvConfig
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.environment import bin_path

@given(u'a user is on the Flora Homepage')
def user_on_homepage(context):
    # launch your browser
    driver = webdriver.Chrome(executable_path=bin_path())
    driver.get(EnvConfig.environment_config_for('homepage_url'))
    # go to the flora homepage
    print('')


@when(u'he clicks on Our Products button')
def clicks_on_our_products_button(context):
    print('user clicks our product button')


@then(u'he should go onto Our Products page')
def be_on_our_products_page(context):
    print('user is on our products page')

