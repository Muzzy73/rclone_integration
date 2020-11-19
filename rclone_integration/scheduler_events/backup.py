import frappe
from frappe import enqueue
from frappe.utils.backups import get_backup_path
from frappe.utils import now
import os


def enqueue_sync():
    enqueue("rclone_integration.scheduler_events.backup._execute")


def _execute():
    source = get_backup_path()
    remotes = [
        x.get("remote_name")
        for x in frappe.db.get_all(
            "Rclone Integration Settings Remote", fields=["remote_name"]
        )
    ]

    has_synced = False
    for remote in remotes:
        stream = os.popen(
            "rclone copy %(source)s %(remote)s:" % {"source": source, "remote": remote}
        )
        output = stream.read()
        if output:
            frappe.log_error(
                "Error in copying backup to remote", "Rclone Integration Backup Error"
            )
        has_synced = True

    if has_synced:
        frappe.db.set_value(
            "Rclone Integration Settings",
            "Rclone Integration Settings",
            "latest_backup_at",
            now(),
        )
