import configparser
import keyring
from getpass import getpass


class ProxMoxConfig:

    def __init__(self):
        # attempt to read local config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.pmServer = config['general']['server']
        self.pmServerPort = config['general']['server_port']
        self.pmApi = "https://" + self.pmServer + ":" + self.pmServerPort
        self.pmUser = config['general']['username']
        self.pmAuth = config['general']['auth_header_string']
        self.pmAuthJson = {
            "Authorization" : self.pmAuth
        }

        requestConfigUpdate = False

        if self.pmServer == '':
            self.pmServer, self.pmServerPort = ProxMoxConfig.getServerDetails(self)
            config['general']['server'] = self.pmServer
            config['general']['server_port'] = self.pmServerPort
            requestConfigUpdate = True


        if self.pmUser == '':
            self.pmUser = ProxMoxConfig.getUser(self)
            config['general']['username'] = self.pmUser
            requestConfigUpdate = True

        if self.pmAuth == '':
            print('No authentication token string found in config, gathering credentials for access... ')
            ProxMoxConfig.getPassword(self, self.pmUser)

        if requestConfigUpdate:
            saveConfig = input('Would you like to save your updated config (y or n)? ')
            if saveConfig == 'y' or saveConfig == 'Y' or saveConfig == 'yes' or saveConfig == 'Yes':
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
        return





    def getServerDetails(self):
        servIP = input('Enter your proxmox server IP: ')
        servPort = input('Enter your proxmox server port (8006): ')
        if servPort == '':
            servPort = '8006'
        return servIP, servPort

    def getUser(self):
        servUser = input('Enter your proxmox user (root): ')
        if servUser == '':
            servUser = 'root'
        return servUser

    def getPassword(self, servUser):
        pmPassKeyRingExists = False
        servPass = keyring.get_password("pypmmgr", servUser)

        if bool(servPass) is False:
            servPass = getpass("Enter your ProxMox password for '" + servUser + "': ")
            keyring.set_password("pypmmgr", servUser, servPass)
        else:
            yorn = input("Password found for '" + servUser + "' would you like to update it (y or n)?")
            if yorn == 'y' or yorn == 'Y' or yorn == 'yes' or yorn == 'Yes':
                servPass = getpass("Enter your ProxMox password for '" + servUser + "': ")
                keyring.set_password("pypmmgr", servUser, servPass)
            else:
                print('Using your current saved password...')


""""
class ProxMoxConfig:
    pmServer = None
    pmServerPort = None
    pmUser = None
    pmPass = None
    apiUrlBase = None
    pmAuthHeader = None

    config = configparser.ConfigParser()
    config.read('config.ini')

    def initialize_config(self):
        global pmServer
        global pmServerPort
        global pmUser
        global pmPass
        global apiUrlBase
        global pmAuthHeader
        global config

        askToSet = False

        try:
            pmServer = config['general']['server']
        except:
            print('Error checking config for server.')

        if !pmServer:
            askToSet = True
            pmServer = input('Enter your proxmox server IP: ')

        try:
            pmServerPort = config['general']['server_port']
        except:
            print('Error checking config for server port.')

        if bool(pmServerPort) is False:
            pmServerPort = input('Enter your proxmox server port (8006): ')
            if pmServerPort == '':
                pmServerPort = '8006'

        self.check_for_api_token()
        print(pmAuthHeader)

        # Get username
        try:
            pmUser = config['general']['username']
        except:
            print('Error checking config for user.')

        if bool(pmUser) is False:
            askToSet = True
            pmUser = input('Enter your proxmox username: ')

        # Get password
        pmPassKeyRingExists = False

        try:
            pmPass = keyring.get_password("pypmmgr", pmUser)
            pmPassKeyRingExists = True
        except:
            print('Error checking for keyring password.')

        if bool(pmPass) is False:
            askToSet = True
            pmPassKeyRingExists = False
            pmPass = getpass('Enter your ProxMox password: ')

        # Check to save credentials
        if pmPassKeyRingExists is False:
            yorn = input('Save credentials to system keyring (y or n): ')
            if yorn == 'y' or yorn == 'Y' or yorn == 'yes' or yorn == 'Yes':
                try:
                    keyring.set_password("pypmmgr", pmUser, pmPass)
                except:
                    print('Failed to set keyring.')

        apiUrlBase = "https://" + pmServer + ":" + pmServerPort

        # Save the updated config file
        if askToSet is True:
            yorn = input('Save connection details to config (y or n): ')
            if yorn == 'y' or yorn == 'Y' or yorn == 'yes' or yorn == 'Yes':
                config['general']['server'] = pmServer
                config['general']['server_port'] = pmServerPort
                config['general']['username'] = pmUser
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

    def check_for_api_token(self):
        # Get API Token if available

        global pmAuthHeader

        try:
            pmAuthHeaderPveApiToken = config['general']['auth_header_pveapitoken']
        except:
            print('Error retrieving authentication header token ID.')

        try:
            pmAuthHeaderTokenSecret = config['general']['auth_header_tokensecret']
        except:
            print('Error retrieving authentication header token secret.')

        pmAuthString = "PVEAPIToken=" + pmAuthHeaderPveApiToken + "=" + pmAuthHeaderTokenSecret

        pmAuthHeader = {
            "Authorization": pmAuthString
        }

    def setUser(self, myUser):
        global pmUser
        pmUser = myUser
        return

    def getUser(self):
        global pmUser
        return pmUser

    def setPass(self, myPass):
        global pmPass
        pmPass = myPass
        return

    def getPass(self):
        global pmPass
        return pmPass

    def setApiUrlBase(self, myApi):
        global apiUrlBase
        apiUrlBase = myApi
        return

    def getApiUrlBase(self):
        global apiUrlBase
        return apiUrlBase

    def setAuthHeader(self, myAuthHeader):
        global pmAuthHeader
        pmAuthHeader = myAuthHeader
        return

    def getAuthHeader(self):
        global pmAuthHeader
        return pmAuthHeader

"""
