```bash

cd frappe-bench/
chmod -R o+rx /home/frappe
bench new-site hs.rai
bench --site hs.rai add-to-hosts
bench use hs.rai
bench start

```
