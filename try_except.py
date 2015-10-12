try:
    str1 = "123"
    # TypeError
    str1 / 5
    # ZeroDivisionError
    10 / 0

except ValueError:
    print "ya"

except ZeroDivisionError:
    print "ZeroDivisionError"

except:
    print "got everythings!"


# =====================================


def login(self):
        try:
            gmail_login_URL = """https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&lp=1&hl=zh-CN#identifier"""

            self.driver.get(gmail_login_URL)
            self.driver.find_element_by_id("Email").send_keys(self.email)
            self.driver.find_element_by_id("next").send_keys(Keys.ENTER)
            self.driver.find_element_by_id("Passwd").send_keys(self.password)
            self.driver.find_element_by_id("signIn").send_keys(Keys.ENTER)

            return True
        except Exception as error:
            print error

        return False
