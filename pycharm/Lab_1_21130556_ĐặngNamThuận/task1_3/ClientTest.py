from datetime import datetime

from lab1.task1_3.Account import Account
from lab1.task1_3.AccountManager import AccountManager
from lab1.task1_3.NormalProduct import NormalProduct
from lab1.task1_3.Post import Post
from lab1.task1_3.VerifiedAccount import VerifiedAccount


def main():
    p1 = Post("Hôm nay trời nắng!", "Thời tiết", 16)
    p2 = Post("C1: BAYERN 3-0 LAZIO", "Thể thao", 20)
    p3 = Post("Tai nạn tại đèo Cẩm Phả", "Giao thông", 25)
    p4 = Post("FB bị sự cố toàn cầu", "Thế giới", 10)
    p5 = Post("Suy thoái kinh tế nặng nề tại Mỹ", "Kinh tế", 20)
    p6 = Post("C1: REAL SOCIEDAD 1-2 PSG", "Thể thao", 22)
    p7 = Post("Họp chính phủ thường niên khoá 40", "Chính trị", 18)
    p8 = Post("Covid được kiểm soát tại Việt Nam", "Y tế", 13)
    p9 = Post("Sinh con nhiều trong năm 2024", "Xã hội", 11)
    p10 = Post("Tảo hôn & sinh con cận huyết ở miền núi", "Xã hội", 31)

    acc1 = VerifiedAccount("Trần Văn Vũ", "vudeptrai@gmail.com", "Việt Nam", datetime(2024, 3, 7))
    acc2 = VerifiedAccount("Lê Thị Hải Hồng", "durianforfood@gmail.com", "Việt Nam", datetime(2024, 2, 29))
    acc3 = NormalProduct("Nguyễn Văn Cang", "nghiavan123@gmail.com", "Việt Nam")
    acc4 = NormalProduct("Martin Leon", "leonmartin@gmail.com", "Úc")
    acc5 = VerifiedAccount("Kim Tae Hook", "kimtae123@gmail.com", "Hàn Quốc", datetime(2024, 12, 3))

    manager = AccountManager()

    manager.add_account(acc1)
    manager.add_account(acc2)
    manager.add_account(acc3)
    manager.add_account(acc4)
    manager.add_account(acc5)

    acc1.add_post(p1)
    acc1.add_post(p2)
    acc1.add_post(p3)
    acc1.add_post(p4)
    acc1.add_post(p5)
    acc1.add_post(p6)
    acc1.add_post(p7)
    acc1.add_post(p8)
    acc1.add_post(p9)
    acc1.add_post(p10)

    acc2.add_post(p3)
    acc2.add_post(p4)
    acc2.add_post(p5)
    acc2.add_post(p6)
    acc2.add_post(p7)
    acc2.add_post(p8)

    acc3.add_post(p5)
    acc3.add_post(p6)
    acc3.add_post(p7)
    acc3.add_post(p8)
    acc3.add_post(p9)
    acc3.add_post(p10)

    acc4.add_post(p7)
    acc4.add_post(p8)

    acc5.add_post(p9)
    acc5.add_post(p10)

    acc1.add_friend(acc2)
    acc1.add_friend(acc3)
    acc1.add_friend(acc4)

    acc2.add_friend(acc1)
    acc2.add_friend(acc5)
    acc2.add_friend(acc3)

    print(acc1.getMaxLikePostByFriend())
    print(manager.groupAccountsByPostLike())
    print(manager.filterAccounts("Việt Nam"))


if __name__ == "__main__":
    main()
