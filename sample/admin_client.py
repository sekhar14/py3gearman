import py3gearman

gm_admin_client = py3gearman.GearmanAdminClient(['localhost:4730'])
workers = gm_admin_client.get_workers()
print(workers)
