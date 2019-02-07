import xlsxwriter
import datetime

BUSINESS = 90.00
FREE = 0.75
LITE = 0.75
PRO = 3.50
OVERAGE = 260.00


class ResellerExport:
    def __init__(self, filename):
        _date = datetime.date.today()
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet('{} Sitelock Usage'.format(_date))
        self.worksheet1 = self.workbook.add_worksheet("Plan Cost")
        self.worksheet2 = self.workbook.add_worksheet("Summary")
        self.worksheet.set_column('A:B', width=15)
        self.worksheet.set_column('C:E', width=16)
        self.worksheet.set_column('F:F', width=10)
        self.worksheet.set_column('G:G', width=15)
        self.worksheet1.set_column('A:A', width=15)
        self.money = self.workbook.add_format({'num_format': '$#,##0.00'})

    def add_header(self):
        headers = ["Name", "Plan", "Earlier billing cycle", "Previous billing cycle",
                   "Current billing cycle", "Cost", "Monthly Overage"]
        col = 0
        for header in headers:
            self.worksheet.write(0, col, header)
            col += 1

        headers = ["Plan", "Cost"]
        col = 0
        for header in headers:
            self.worksheet1.write(0, col, header)
            col += 1
        self.worksheet1.write(1, 0, "Business")
        self.worksheet1.write(2, 0, "Free")
        self.worksheet1.write(3, 0, "SiteLock-Lite")
        self.worksheet1.write(4, 0, "SiteLock-Pro")
        self.worksheet1.write(1, 1, BUSINESS, self.money)
        self.worksheet1.write(2, 1, FREE, self.money)
        self.worksheet1.write(3, 1, LITE, self.money)
        self.worksheet1.write(4, 1, PRO, self.money)

        headers = ["Plan", "Count of Plan", "Sum of Cost", "Sum of Monthly Overages"]
        col = 0
        for header in headers:
            self.worksheet2.write(0, col, header)
            col += 1

    def add_account_data(self, data):
        row = 1
        for account in data:
            accountName = account["account_name"]
            accountId = account["account_id"]
            plan_name = account["plan_name"]
            name = "{}({})".format(accountName, accountId)
            for bandwidthHistory in account["bandwidthHistory"]:
                if bandwidthHistory["billingCycle"] == "Previous billing cycle":
                    previous_bits = bandwidthHistory["alwaysOnBandwidth"]
                if bandwidthHistory["billingCycle"] == "Current billing cycle":
                    current_bits = bandwidthHistory["alwaysOnBandwidth"]
                if bandwidthHistory["billingCycle"] == "Earlier billing cycle":
                    earlier_bits = bandwidthHistory["alwaysOnBandwidth"]
            self.worksheet.write(row, 0, name)
            self.worksheet.write(row, 1, plan_name)
            self.worksheet.write(row, 2, self.convert_bits(earlier_bits))
            self.worksheet.write(row, 3, self.convert_bits(previous_bits))
            self.worksheet.write(row, 4, self.convert_bits(current_bits))
            self.worksheet.write(row, 5, self.find_cost(plan_name), self.money)
            self.worksheet.write(row, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
            row += 1

    def convert_bits(self, data):
        if "Tbps" in data:
            bits = data.replace("Tbps", "")
            total_bits = float(bits) * 1000 * 1000 * 1000 * 1000
            return int(total_bits)
        elif "Gbps" in data:
            bits = data.replace("Gbps", "")
            total_bits = float(bits) * 1000 * 1000 * 1000
            return int(total_bits)
        elif "Mbps" in data:
            bits = data.replace("Mbps", "")
            total_bits = float(bits) * 1000 * 1000
            return int(total_bits)
        elif "Kbps" in data:
            bits = data.replace("Kbps", "")
            total_bits = float(bits) * 1000
            return int(total_bits)
        elif "bps" in data:
            bits = data.replace("bps", "")
            return int(bits)
        else:
            return "none"

    def find_cost(self, data):
        if "Business" in data:
            return BUSINESS
        elif "Free" in data:
            return FREE
        elif "SiteLock-Lite" in data:
            return LITE
        elif "SiteLock-Pro" in data:
            return PRO
        else:
            return "none"

    def get_overage(self, bits, plan):
        print(str(bits))
        if 5000000 <= bits <= 20000000:
            print("Found one:{}".format(str(bits)))
            return OVERAGE
