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
        self.wsBusiness = self.workbook.add_worksheet('{} (Business) Usage'.format(_date))
        self.wsPro = self.workbook.add_worksheet('{} (Pro) Usage'.format(_date))
        self.wsLite = self.workbook.add_worksheet('{} (Lite) Usage'.format(_date))
        self.wsFree = self.workbook.add_worksheet('{} (Free) Usage'.format(_date))
        self.wsOverage = self.workbook.add_worksheet('{} Overage'.format(_date))
        self.wsPlanCost = self.workbook.add_worksheet("Plan Cost")
        self.wsSummary = self.workbook.add_worksheet("Summary")
        self.wsBusiness.set_column('A:B', width=15)
        self.wsBusiness.set_column('C:E', width=16)
        self.wsBusiness.set_column('F:F', width=10)
        self.wsPro.set_column('A:B', width=15)
        self.wsPro.set_column('C:E', width=16)
        self.wsPro.set_column('F:F', width=10)
        self.wsLite.set_column('A:B', width=15)
        self.wsLite.set_column('C:E', width=16)
        self.wsLite.set_column('F:F', width=10)
        self.wsFree.set_column('A:B', width=15)
        self.wsFree.set_column('C:E', width=16)
        self.wsFree.set_column('F:F', width=10)
        self.wsOverage.set_column('A:B', width=15)
        self.wsOverage.set_column('C:E', width=16)
        self.wsOverage.set_column('F:F', width=10)
        self.wsOverage.set_column('G:G', width=15)
        self.wsPlanCost.set_column('A:A', width=15)
        self.wsSummary.set_column('A:C', width=10)
        self.wsSummary.set_column('D:D', width=20)
        self.money = self.workbook.add_format({'num_format': '$#,##0.00'})
        self.summary = self.workbook.add_format({'num_format': '$#,##0.00', 'bg_color': 'cyan', 'bold': True})

        self.tBusiness = 0
        self.tPro = 0
        self.tLite = 0
        self.tFree = 0
        self.oBusiness = 0
        self.oPro = 0
        self.oLite = 0
        self.oFree = 0

    def add_header(self):
        headers = ["Name", "Plan", "Earlier billing cycle", "Previous billing cycle",
                   "Current billing cycle", "Cost"]

        col = 0
        for header in headers:
            self.wsBusiness.write(0, col, header)
            self.wsPro.write(0, col, header)
            self.wsLite.write(0, col, header)
            self.wsFree.write(0, col, header)
            self.wsOverage.write(0, col, header)
            col += 1
        self.wsOverage.write(0, col, "Monthly Overage")

        headers = ["Plan", "Cost"]
        col = 0
        for header in headers:
            self.wsPlanCost.write(0, col, header)
            col += 1
        self.wsPlanCost.write(1, 0, "Business")
        self.wsPlanCost.write(2, 0, "Free")
        self.wsPlanCost.write(3, 0, "SiteLock-Lite")
        self.wsPlanCost.write(4, 0, "SiteLock-Pro")
        self.wsPlanCost.write(1, 1, BUSINESS, self.money)
        self.wsPlanCost.write(2, 1, FREE, self.money)
        self.wsPlanCost.write(3, 1, LITE, self.money)
        self.wsPlanCost.write(4, 1, PRO, self.money)

        headers = ["Plan", "Count of Plan", "Sum of Cost", "Sum of Monthly Overages"]
        col = 0
        for header in headers:
            self.wsSummary.write(0, col, header)
            col += 1

    def add_account_data(self, data):
        rBusiness = 1
        rPro = 1
        rLite = 1
        rFree = 1
        rOverage = 1
        earlier_bits = None
        previous_bits = None
        current_bits = None
        for account in data:
            accountName = account["account_name"]
            accountId = account["account_id"]
            plan_name = account["plan_name"]
            name = "{}({})".format(accountName, accountId)
            for bandwidthHistory in account["bandwidthHistory"]:
                if bandwidthHistory["billingCycle"] == "Previous billing cycle":
                    previous_bits = bandwidthHistory["alwaysOnBandwidth"] or 0
                if bandwidthHistory["billingCycle"] == "Current billing cycle":
                    current_bits = bandwidthHistory["alwaysOnBandwidth"] or 0
                if bandwidthHistory["billingCycle"] == "Earlier billing cycle":
                    earlier_bits = bandwidthHistory["alwaysOnBandwidth"] or 0
            if self.get_overage(self.convert_bits(previous_bits), plan_name):
                self.wsOverage.write(rOverage, 0, name)
                self.wsOverage.write(rOverage, 1, plan_name)
                self.wsOverage.write(rOverage, 2, self.convert_bits(earlier_bits))
                self.wsOverage.write(rOverage, 3, self.convert_bits(previous_bits))
                self.wsOverage.write(rOverage, 4, self.convert_bits(current_bits))
                self.wsOverage.write(rOverage, 5, self.find_cost(plan_name), self.money)
                self.wsOverage.write(rOverage, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
                rOverage += 1
                if "Business" in plan_name:
                    self.oBusiness += 1
                if "SiteLock-Pro" in plan_name:
                    self.oPro += 1
                if "SiteLock-Lite" in plan_name:
                    self.oLite += 1
                if "Free" in plan_name:
                    self.oFree += 1
            else:
                if "Business" in plan_name:
                    self.wsBusiness.write(rBusiness, 0, name)
                    self.wsBusiness.write(rBusiness, 1, plan_name)
                    self.wsBusiness.write(rBusiness, 2, self.convert_bits(earlier_bits))
                    self.wsBusiness.write(rBusiness, 3, self.convert_bits(previous_bits))
                    self.wsBusiness.write(rBusiness, 4, self.convert_bits(current_bits))
                    self.wsBusiness.write(rBusiness, 5, self.find_cost(plan_name), self.money)
                    self.wsBusiness.write(rBusiness, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
                    rBusiness += 1

                if "SiteLock-Pro" in plan_name:
                    self.wsPro.write(rPro, 0, name)
                    self.wsPro.write(rPro, 1, plan_name)
                    self.wsPro.write(rPro, 2, self.convert_bits(earlier_bits))
                    self.wsPro.write(rPro, 3, self.convert_bits(previous_bits))
                    self.wsPro.write(rPro, 4, self.convert_bits(current_bits))
                    self.wsPro.write(rPro, 5, self.find_cost(plan_name), self.money)
                    self.wsPro.write(rPro, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
                    rPro += 1

                if "SiteLock-Lite" in plan_name:
                    self.wsLite.write(rLite, 0, name)
                    self.wsLite.write(rLite, 1, plan_name)
                    self.wsLite.write(rLite, 2, self.convert_bits(earlier_bits))
                    self.wsLite.write(rLite, 3, self.convert_bits(previous_bits))
                    self.wsLite.write(rLite, 4, self.convert_bits(current_bits))
                    self.wsLite.write(rLite, 5, self.find_cost(plan_name), self.money)
                    self.wsLite.write(rLite, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
                    rLite += 1

                if "Free" in plan_name:
                    self.wsFree.write(rFree, 0, name)
                    self.wsFree.write(rFree, 1, plan_name)
                    self.wsFree.write(rFree, 2, self.convert_bits(earlier_bits))
                    self.wsFree.write(rFree, 3, self.convert_bits(previous_bits))
                    self.wsFree.write(rFree, 4, self.convert_bits(current_bits))
                    self.wsFree.write(rFree, 5, self.find_cost(plan_name), self.money)
                    self.wsFree.write(rFree, 6, self.get_overage(self.convert_bits(previous_bits), plan_name), self.money)
                    rFree += 1

        #Summerize
        self.tBusiness = rBusiness - 1
        self.tPro = rPro - 1
        self.tLite = rLite - 1
        self.tFree = rFree - 1

        self.wsSummary.write(1, 0, "Business")
        self.wsSummary.write(1, 1, self.tBusiness)
        self.wsSummary.write(1, 2, self.tBusiness * BUSINESS, self.money)
        self.wsSummary.write(1, 3, self.oBusiness * OVERAGE, self.money)

        self.wsSummary.write(2, 0, "SiteLock-Pro")
        self.wsSummary.write(2, 1, self.tPro)
        self.wsSummary.write(2, 2, self.tPro * PRO, self.money)
        self.wsSummary.write(2, 3, self.oPro * OVERAGE, self.money)

        self.wsSummary.write(3, 0, "SiteLock-Lite")
        self.wsSummary.write(3, 1, self.tLite)
        self.wsSummary.write(3, 2, self.tLite * LITE, self.money)
        self.wsSummary.write(3, 3, self.oLite * OVERAGE, self.money)

        self.wsSummary.write(4, 0, "Free")
        self.wsSummary.write(4, 1, self.tFree)
        self.wsSummary.write(4, 2, self.tFree * FREE, self.money)
        self.wsSummary.write(4, 3, self.oFree * OVERAGE, self.money)

        self.wsSummary.write(5, 0, "Total")
        self.wsSummary.write(5, 1, self.tBusiness + self.tPro + self.tLite + self.tFree)
        self.wsSummary.write(5, 2, (self.tBusiness * BUSINESS) + (self.tPro * PRO) + (self.tLite * LITE) + (self.tFree * FREE), self.money)
        self.wsSummary.write(5, 3, (self.oBusiness + self.oPro + self.oLite + self.oFree) * OVERAGE, self.money)

        self.wsSummary.write(6, 0, "Grand Total")
        self.wsSummary.write(6, 3, ((self.oBusiness + self.oPro + self.oLite + self.oFree) * OVERAGE) +
                             (self.tBusiness * BUSINESS) + (self.tPro * PRO) + (self.tLite * LITE) + (self.tFree * FREE), self.summary)

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
