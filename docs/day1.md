[Previous](index.md) | [Index](index.md) | [Next](day2.md)

---

## Day 1

```bash
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench/
chmod -R o+rx /home/frappe
bench new-site hs.rai
bench --site hs.rai add-to-hosts
bench use hs.rai
bench start

# // In new terminal // #

bench new-app library_management
bench --site library.test install-app library_management

```

---

[Previous](index.md) | [Index](index.md) | [Next](day2.md)
