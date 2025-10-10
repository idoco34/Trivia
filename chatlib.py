# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT",
"login_failed_msg" : "ERROR"
} # .. Add more commands if needed


PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
} # ..  Add more commands if needed


# Other constants

ERROR_RETURN = None  # What is returned in case of an error
ERROR_RETURN_ARR = (ERROR_RETURN, ERROR_RETURN)

def is_string_int(s):
    try:
        # Attempt to convert the string to an integer
        int(s)
        # If conversion succeeds, return True
        return True
    except ValueError:
        # If conversion fails (e.g., if s contains letters or decimals), return False
        return False


def build_message(cmd, data):
	if cmd not in PROTOCOL_CLIENT.values():
		return ERROR_RETURN
	i = len(cmd)
	spaces = CMD_FIELD_LENGTH-i
	msg = cmd + " " * spaces
	k = len(data)
	k = str(k)
	add = 4-len(k)
	for l in range (add):
		k+= '0'
	k = k[::-1]
	msg += '|' + k + '|' + data
	return msg

	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""




def parse_message(data):
	fields = data.split('|')
	if len(fields) != 3:
		return ERROR_RETURN_ARR
	cmd = fields[0].rstrip().lstrip()
	if not is_string_int(fields[1]):
		return ERROR_RETURN_ARR
	if cmd not in PROTOCOL_CLIENT.values():
		return ERROR_RETURN_ARR
	length_msg = int(fields[1])
	if len(fields[2]) != length_msg:
		return ERROR_RETURN_ARR
	msg = fields[2]
	tup = (cmd, msg)
	return tup
	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""
    # Implement code ...

    # The function should return 2 values


	
def split_data(msg, expected_fields):
	split_string = []
	if msg.count('#') != expected_fields:
		return ERROR_RETURN_ARR
	str1 = ""
	for c in msg:
		if c != '#':
			str1 += c
		else:
			split_string.append(str1)
			str1 = ""
	split_string.append(str1)
	return tuple(split_string)


	"""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""
	# Implement code ...


def join_data(msg_fields):
	str1 = ""
	for msg in msg_fields:
		str1+= msg +"#"
	str1 = str1[:-1]
	return str1
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""
	# Implement code ...


if __name__ == '__main__':
	print("chatlib main")