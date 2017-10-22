def hanoi_qulleleri(disk_sayi, menbe_sutun, komekci_sutun, hedef_sutun):
  print("hanoi_qulleleri( ", disk_sayi, menbe_sutun, komekci_sutun, hedef_sutun, " cagrildi...)")
  if disk_sayi:
    # (n - 1) sutununu menbeden komekciye yerleshdirmek
    hanoi_qulleleri(disk_sayi-1, menbe_sutun, hedef_sutun, komekci_sutun)
    # deyildiyi kimi, n-ci diski menbeden hedefe yerleshdiririk
    if menbe_sutun:
        disk = menbe_sutun.pop()
        print("Disk {}-in menbe_sutun-dan hedef_sutun-a yerleshdirilmesi".format(disk))
        hedef_sutun.append(disk)
    # (n - 1) sutununu komekciden hedefe yerleshdiririk
    hanoi_qulleleri(disk_sayi-1, komekci_sutun, menbe_sutun, hedef_sutun)


menbe_sutun = [3, 2, 1]
hedef_sutun = []
komekci_sutun = []
hanoi_qulleleri(len(menbe_sutun), menbe_sutun, komekci_sutun, hedef_sutun)

print("son netice")
print(menbe_sutun, komekci_sutun, hedef_sutun)
