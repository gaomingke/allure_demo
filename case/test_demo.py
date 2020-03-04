import allure


class Test(object):
    @allure.MASTER_HELPER.step("测试步骤1")
    def test_func1(self):
        print("测试用例1")

    def test_func2(self):
        allure.MASTER_HELPER.attach('测试步骤','1.输入账号 2.输入密码 3.点击登录')
        print("测试用例2")

    @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.CRITICAL)
    def test_func3(self):
        print("测试用例3")
        assert 0