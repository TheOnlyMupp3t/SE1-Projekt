class Dataset:

    #Constructor
    def __init__(self, cpuUsage, ramUsage, serverLoginFailed, serverLoginSuccess, trafficUpload, trafficDownload, news):
        self.cpuUsage = cpuUsage
        self.ramUsage = ramUsage
        self.serverLoginFailed = serverLoginFailed
        self.serverLoginSuccess = serverLoginSuccess
        self.trafficUpload = trafficUpload
        self.trafficDownload = trafficDownload
        self.news = news

    def __dir__(self):
        return ["cpuUsage", "ramUsage", "serverLoginFailed", "serverLoginSuccess", "trafficUpload", "trafficDownload"]

