import sys
import RW_ACCOUNT
import MENU
import CATCH_PUBLIC_COURSE as pub
import CATCH_PLANNED_COURSE as plan
import LOGIN


def begin_catch_course():
    catch_course_dic = {
        "1":"计划内选课",
        "2":"公选课",
        "0":"返回主菜单"
    }
    catch_course_menu = MENU.MENU(catch_course_dic)
    catch_course_menu.print_list()
    while True:
        _key = input(">>>")
        if _key == "1":
            planned_course_spider = plan.PlannedCourse(account)
            planned_course_spider.init_menu()
            planned_course_spider.attack()
        elif _key == "2":
            public = pub.PublicCourse(account)
            public.run()
        elif _key == "0":
            return
        else:
            print("请输入正确的数字")


if __name__ == "__main__":
    init_dic = {
        "1": "设置账号密码",
        "2": "开始抢课",
        "0": "退出"
    }
    init_menu = MENU.MENU(init_dic)
    init_menu.print_list()
    while True:
        key = input(">>>")
        if key == "1":
            RW_ACCOUNT.set_account()
            init_menu.print_list()
        elif key == "2":
            account = LOGIN.Account()
            account.login()
            begin_catch_course()
            init_menu.print_list()
        elif key == "0":
            sys.exit()
        else:
            print("请输入正确的数字")
