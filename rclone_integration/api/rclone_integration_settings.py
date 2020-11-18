import frappe
import re
from frappe import _
from rclone_integration.scheduler_events.backup import enqueue_sync


@frappe.whitelist()
def get_config(path):
    if not path:
        frappe.throw(_('Please input RClone configuration path'))
    return _get_remotes(path)


@frappe.whitelist()
def sync_backup():
    frappe.msgprint('Enqueueing sync backup to remotes')
    enqueue_sync()


def _get_remotes(path):
    with open(path, 'r') as config_file:
        return re.findall(r'\[(.*?)\]', config_file.read())
