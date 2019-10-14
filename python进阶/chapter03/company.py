class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])

# company1 = company[:2]  # 如果没有 __getitem__ 会报错
#
# print(len(company))
#
# for em in company1:  # 如果没有 __getitem__ 会报错
#     print(em)
