import math
import sys

principal = 0
payment = 0
payment_adds = 0
periods = 0
interest = 0
args = []
menu = ""


def calculate_differential():
    global principal
    global periods
    global payment
    global payment_adds
    global interest

    interest = (interest / 100) / 12

    for number in range(1, periods + 1):
        payment = (principal / periods) + interest * (principal - (principal * (number - 1) / periods))
        payment = math.ceil(payment)
        payment_adds += payment
        print("Month {}: paid out {}".format(number, payment))

    print("")
    print("Overpayment = ", round(payment_adds - principal))


def calculate_months():
    global principal
    global periods
    global payment
    global payment_adds
    global interest

    months = 0
    years = 0
    result = ""

    interest = (interest / 100) / 12

    periods = math.log(payment / (payment - interest * principal), 1 + interest)
    periods = math.ceil(periods)

    payment_adds = payment * periods
    years = periods // 12
    months = periods % 12

    result = "You need "
    if years > 0:
        if years == 1:
            result += "1 year"
        else:
            result += str(years) + " years"
        if months > 0:
            result += " and "
            if months == 1:
                result += "1 month"
            else:
                result += str(months) + " months"
    else:
        if months == 1:
            result += "1 month"
        else:
            result += str(months) + " months"
    result += " to repay this credit!"
    print(result)
    print("Overpayment =", payment_adds - principal)


def calculate_principal():
    global principal
    global periods
    global payment
    global interest

    interest = (interest / 100) / 12

    principal = payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    print("Your credit principal = {}!".format(round(principal)))


def calculate_annuity():
    global principal
    global periods
    global payment
    global interest

    interest = (interest / 100) / 12

    payment = principal * ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))

    print("Your annuity payment = {}!".format(math.ceil(payment)))


def check_arguments():
    global principal
    global payment
    global periods
    global interest
    if len(args) < 5:
        print("Incorrect parameters")
        return False
    if args[1] != "--type=diff" and args[1] != "--type=annuity":
        print("Incorrect parameters")
        return False
    if args[1] == "--type=diff" and ("--payment" in args):
        print("Incorrect parameters")
        return False
    #if "--interest" in args:
    #    pass
    #else:
    #    print("Incorrect parameters")
    #    return False
    if float(arg2[1]) < 0.0:
        print("Incorrect parameters")
        return False
    if float(arg3[1]) < 0.0:
        print("Incorrect parameters")
        return False
    if float(arg4[1]) < 0.0:
        print("Incorrect parameters")
        return False

    if arg2[0] == "--principal":
        principal = float(arg2[1])
    if arg3[0] == "--principal":
        principal = float(arg3[1])
    if arg4[0] == "--principal":
        principal = float(arg4[1])

    if arg2[0] == "--payment":
        payment = float(arg2[1])
    if arg3[0] == "--payment":
        payment = float(arg3[1])
    if arg4[0] == "--payment":
        payment = float(arg4[1])

    if arg2[0] == "--periods":
        periods = int(arg2[1])
    if arg3[0] == "--periods":
        periods = int(arg3[1])
    if arg4[0] == "--periods":
        periods = int(arg4[1])

    if arg2[0] == "--interest":
        interest = float(arg2[1])
    if arg3[0] == "--interest":
        interest = float(arg3[1])
    if arg4[0] == "--interest":
        interest = float(arg4[1])

    return True


args = sys.argv
# args = ["", "--type=diff", "--principal=1000000", "--periods=10", "--interest=10"]
if len(args) > 4:
    arg1 = args[1].split('=')
    arg2 = args[2].split('=')
    arg3 = args[3].split('=')
    arg4 = args[4].split('=')

if check_arguments():
    if arg1[1] == "diff":
        calculate_differential()
    else:
        if principal == 0:
            calculate_principal()
        elif payment == 0:
            calculate_annuity()
        else:
            calculate_months()
