from copy import deepcopy
from urllib.parse import urljoin

from django import forms
import liqpay

from . import constants, settings


class CallbackForm(forms.Form):
    data = forms.CharField(widget=forms.HiddenInput)
    signature = forms.CharField(widget=forms.HiddenInput)


class CheckoutForm(CallbackForm):
    method = 'POST'

    def __init__(self, params, *args, **kwargs):
        self.params = {} if params is None else deepcopy(params)
        self.liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY,
                             settings.LIQPAY_PRIVATE_KEY)
        self.action_url = urljoin(self.liqpay._host, constants.CHECKOUT_URL)
        self.params.update(
            version=constants.API_VERSION,
            sandbox=str(
                int(bool(params.get('sandbox', settings.LIQPAY_SANDBOX)))),
        )
        initial = {
            'data': self.liqpay.cnb_data(self.params),
            'signature': self.liqpay.cnb_signature(self.params),
        }
        super().__init__(initial=initial, *args, **kwargs)