import pytest
import requests
import DuckDuckGo_API

url_ddg = "https://api.duckduckgo.com"

PRESIDENTS = ['George Washington', 'John Adams', 'Thomas Jefferson',
                'James Madison', 'James Monroe', 'John Quincy Adams',
                'Andrew Jackson', 'Martin Van Buren', 'William Henry Harrison',
                'John Tyler', 'James K. Polk', 'Zachary Taylor',
                'Millard Fillmore', 'Franklin Pierce', 'James Buchanan',
                'Abraham Lincoln', 'Andrew Johnson', 'Ulysses S. Grant',
                'Rutherford B. Hayes', 'James A. Garfield', 'Chester A. Arthur',
                'Grover Cleveland', 'Benjamin Harrison', 'William McKinley',
                'Theodore Roosevelt', 'William Howard Taft', 'Woodrow Wilson',
                'Warren G. Harding', 'Calvin Coolidge', 'Herbert Hoover',
                'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower',
                'John F. Kennedy', 'Lyndon B. Johnson', 'Richard Nixon',
                'Gerald Ford', 'Jimmy Carter', 'Ronald Reagan',
                'George H. W. Bush', 'Bill Clinton', 'George W. Bush',
                'Barack Obama', 'Donald Trump', 'Joe Biden']


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


@pytest.mark.parametrize('president', PRESIDENTS)
def test_ddg_query(president):
    presidents_list = DuckDuckGo_API.ddg_query()
    assert president in presidents_list
