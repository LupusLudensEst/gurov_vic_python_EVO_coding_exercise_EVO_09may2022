# Python version of coding exercise
# ---------------------------------


# This class holds two data values that get sent out on a web request to a payment processing API, and
# writes two returning values when processing the web response.

class CreditCardTransaction:
    # Outgoing values in a web request sent to a payment processing API.
    _amount = None  # Numeric x.xx between 0.00 and 1000.00
    _credit_card_number = None  # String of 16 numeric digits.

    # Incoming values in a web request received from a payment processing API.
    _status = None  # Expected to be a string of "processed" or "rejected".
    _processed_amount = None  # Expected to be the same as amount if status is "processed",

    # or None if status is rejected.

    # 1.TODO: Fill in missing getter and setter code.
    def set_amount(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount


    # 2.TODO: Fill in missing getter and setter code.
    def set_credit_card_number(self, credit_card_number):
        self._credit_card_number = credit_card_number


    def get_credit_card_number(self):
        return self._credit_card_number


    # 3.TODO: Write a getter for each of _status and _processedAmount.
    # Getter code goes here.
    def get_status(self):
        return self._status

    def get_processed_amount(self):
        return self._processed_amount

    def send_transaction(self):
        #code for send_transaction()
        raise NotImplementedError()


# Assume code exists to send the _amount and _credit_card_number out in a web request and
# gets back two values, which are then set in _status and _processed_amount.  If the
# payment processing API is reached, then its returning values will be expected to be present.
# If the payment processing API cannot be reached due to a networking or other problem, then
# _status and _processed_amount are not set to any value.


# test for happy path with valid amount with type - integer
def test_send_credit_card_transaction_happy_path():
    transaction = CreditCardTransaction()
    transaction.set_amount(5)
    transaction.set_credit_card_number("4485328462885964")  # 0, .00000

    transaction.send_transaction()

    assert transaction.get_status() == "processed"
    assert transaction.get_processed_amount() == 5


# test for happy path with valid amount with type - float
def test_send_credit_card_transaction_happy_path_float():
    transaction = CreditCardTransaction()
    transaction.set_amount(5.50)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "processed"
    assert transaction.get_processed_amount() == 5.50


# test for happy path with valid amount value - 0.00
def test_send_credit_card_transaction_happy_path_float_0():
    transaction = CreditCardTransaction()
    transaction.set_amount(0.00)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "processed"
    assert transaction.get_processed_amount() == 0.00


# test for happy path with valid amount value - 1000.00
def test_send_credit_card_transaction_happy_path_float_1000():
    transaction = CreditCardTransaction()
    transaction.set_amount(1000.00)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "processed"
    assert transaction.get_processed_amount() == 1000.00


# test for negative path with invalid amount type - string
def test_send_credit_card_transaction_amount_str():
    transaction = CreditCardTransaction()
    transaction.set_amount("str")
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None


# test for negative path with invalid amount value - negative int
def test_send_credit_card_transaction_negative_int():
    transaction = CreditCardTransaction()
    transaction.set_amount(-5)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None


# test for negative path with invalid amount value (above limit) - 1000.01
def test_send_credit_card_transaction_value_above_limit_1():
    transaction = CreditCardTransaction()
    transaction.set_amount(1000.01)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None

# test for negative path with invalid amount value (above limit) - 1001.00
def test_send_credit_card_transaction_value_above_limit_2():
    transaction = CreditCardTransaction()
    transaction.set_amount(1001.00)
    transaction.set_credit_card_number("4485328462885964")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None


# test for negative path with invalid credit card number - "00000"
def test_send_credit_card_transaction_invalid_cc_1():
    transaction = CreditCardTransaction()
    transaction.set_amount(5.00)
    transaction.set_credit_card_number("00000")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None

# test for negative path with invalid credit card number - "asdfg"
def test_send_credit_card_transaction_invalid_cc_string():
    transaction = CreditCardTransaction()
    transaction.set_amount(5.00)
    transaction.set_credit_card_number("asdfg")

    transaction.send_transaction()

    assert transaction.get_status() == "rejected"
    assert transaction.get_processed_amount() == None

# TODO: create test for empty string cc input, validation with missing input for amount, invalid symbols

# TODO: create assertions for error messages
# TODO: response time test
# TODO: json schema test
