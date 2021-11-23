# -*- coding: utf-8 -*-

from config.celery import app


@app.task
def sync():

    from .models import SalesforceField

    SalesforceField.sync()

    return None


@app.task
def send(lead_id):

    from .models import SalesforceLead

    try:
        lead = SalesforceLead.objects.get(id=lead_id)
    except SalesforceLead.DoesNotExist:
        return False

    lead.send()
