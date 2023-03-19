"""
print("G", "F", sep="", end="")
print("G")
# \n provides new line after printing the year
print("09", "12", "2016", sep="-", end="\n")

print("prtk", "agarwal", sep="", end="@")
print("geeksforgeeks")

a = [1]
print(a)
b = list(a)
print(b)
b.append(2)
print(b)
print(a)
"""
"""
    >>> from collections import namedtuple
    >>> game_state = namedtuple('states', (f'state{i}' for i in range(6)))
    >>> p = game_state(0,0,0,0,0,0)
    >>> c = p._replace(state3=2)
    >>> p
    states(state0=0, state1=0, state2=0, state3=0, state4=0, state5=0)
    >>> c
    states(state0=0, state1=0, state2=0, state3=2, state4=0, state5=0)
"""


"""
    print(f"Wow! you guessed the secret number in {i} tr{('y', 'ies')[bool(i - 1)]}")
    print(f"Wow! you guessed the secret number in {i} tr{'ies' if i - 1 else 'y'}")
"""
import os
cur_dir = os.getcwd()
print(cur_dir)
print(os.path.dirname(__file__))
class UserConfig:
    """
    UserConfig: description of this class
    """
    _DEFAULT_CONFIG = "{0}\\Resources\\UserConfig.json".format(os.getcwd())
    #_DEFAULT_CONFIG = "{0}\\Resources\\UserConfig.json".format(os.path.dirname(__file__))
    _ALTERNATE_CONFIG = "{0}\\Resources\\TOOL.config".format(os.getcwd())
    #_ALTERNATE_CONFIG = "{0}\\Resources\\TOOL.config".format(os.path.dirname(__file__))
    def __init__(self, config_file=None, generate_file=False):
        """
        config_file (file, basestring=None): description
            if None, attempt to open or generate default (or alternate default) config file
        generate_file (bool=False): description
            if config_file exists or is None, option ignored
        """
        # Look for the default file, the alt file, and create the default file if neither exist.

        # If config_file is basestring and exists, open config_file.
        # If config_file is None, test default config files and open default one, if exist,
        # otherwise open alternate one. If neither exist (get_default_config() returns
        # None), generate and open default config file.
        try:
            self.config_file = open(
                config_file or self.get_default_config() or self.generate_config_file()
            )

        # If config_file is a file-type or a “bad” value (ValueError for open()), validate
        # if file-type and re-open -- This is the safer option because the file pointed to
        # or the file-pointer itself could have been modified before this process has
        # received it. This is the same reason for replacing a check for exists() before
        # attempting to open() with just open() with try…except block.
        except ValueError:
            try:
                config_file.close()
                config_file = config_file.name()
            except AttributeError:
                err_msg = (
                    "Expected file or path, got '{0}'. Leave arguments blank to open or create "
                    "the default file from the working directory."
                )
                # XXX  IronPython 2.7 may use `raise <error>(err_msg), None` instead of the
                #           line below  XXX
                raise TypeError(err_msg .format(type(config_file))) from None
            else:
                self.config_file = open(config_file)

        # If config_file is basestring but does not exist (IOError for open()) and generate_file
        # is True, generates default file with file name config_file and opens it.
        except IOError:
            if generate_file:
                self.config_file = open(self.generate_config_file(config_file))
            err_msg = (
                "'{0}' does not exist. If you want to create this file for user configuration, "
                "generate_file option must be set to 'True'. "
            )
            # XXX  IronPython 2.7 may use `raise <error>(err_msg), None` instead of the line
            #           below  XXX
            raise ValueError(err_msg.format(config_file)) from None

    def get_default_config(self):
        """
        get_default_config: Validate existence and return default (or alternate default)
            config file name.
        """
        for config_file in (self._DEFAULT_CONFIG, self._ALTERNATE_CONFIG):
            try:
                open(config_file)
            except IOError:
                continue
            else:
                return config_file
        return None

    def generate_config_file(self, config_file=None, user_config=None):
        """
        generate_config_file: Writes user configuration to JSON-formatted configuration
            file and returns name of generated file.

        config_file (basestring=self._DEFAULT_CONFIG): description
        user_config (dict=USER_CONFIG): description
        """
        with open(config_file or self._DEFAULT_CONFIG, 'w') as json_file:
            json.dump(user_config or USER_CONFIG, json_file) 
        return config_file or self._DEFAULT_CONFIG

def get_ips(text):
    from re import compile as createRegExPattern

    #ip_pattern = createRegExPattern('(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
    ip_pattern = createRegExPattern('(?:\d{1,3}\.){3}\d{1,3}')
    return ip_pattern.findall(text)
    
    
"""
(help) How could be the best way to extract the ip in this case?

Hey I am trying to learn, so I decide to creat a scrip that connect into some routers and get the ip address, at the moment I am able to get this

interface FastEthernet0/0

ip address 10.0.0.1 255.0.0.0

ip nat inside

ip virtual-reassembly

duplex auto

speed auto

end

and I just want to get the "[10.0.0.1](https://10.0.0.1) [255.0.0.0](https://255.0.0.0)" to save into a dic.

I tried to slip the lines  but I still get this:

`['', 'Building configuration...', '', 'Current configuration : 127 bytes', '!', 'interface FastEthernet0/0', ' ip address` [`10.0.0.1`](https://10.0.0.1) [`255.0.0.0`](https://255.0.0.0)`', ' ip nat inside', ' ip virtual-reassembly', ' duplex auto', ' speed auto', 'end']`

&#x200B;

any ideia please ? I bellow I leave this function:

`def create_connection(my_device2):`  
`net_conn = ConnectHandler(**my_device2)`  
`net_conn.send_command_timing("disable")`  
 `#print(net_conn.find_prompt())`  
 `net_conn.enable()`  
`output = net_conn.send_command("show running-config  interface fastEthernet 0/0")`  
 `print(output)`  
`lines= output.splitlines()`  
 `print(lines)`  


thank you all.
"""