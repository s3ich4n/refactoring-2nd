# tracking.py


class TrackingInformation:
    def __init__(self):
        self._shipping_company = None
        self._tracking_number = None

    @property
    def shipping_company(self):
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, arg):
        self._shipping_company = arg

    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, arg):
        self._tracking_number = arg

    @property
    def display(self):
        return f"{self.shipping_company}: {self.tracking_number}"


class Shipment:
    def __init__(self):
        self._tracking_information = None

    @property
    def tracking_info(self):
        # 자바스크립트의 get trackingInfo() { return this._trackingInformation.display; }에 해당
        return (
            self._tracking_information.display if self._tracking_information else None
        )

    @property
    def tracking_information(self):
        return self._tracking_information

    @tracking_information.setter
    def tracking_information(self, a_tracking_information):
        self._tracking_information = a_tracking_information
