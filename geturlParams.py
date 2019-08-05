import readConfig as readConfig

readconfig = readConfig.ReadConfig()


class geturlParams():
    ''' 读取配置信息地址 '''
    def get_Url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl')+ ":" +readconfig.get_http(
            'port')
        # logger.info('new_url'+new_url)
        return new_url

