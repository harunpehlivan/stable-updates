#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.cd("acpi_notifier-1.0.28")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("address_keeper-1.0.7")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("archive-0.6.13")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("att_remover-1.0.15")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("attachwarner-1.0")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("bsfilter_plugin-1.0.9")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("clamd-3.5.5")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("fancy-0.9.17")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("fetchinfo-plugin-0.4.25")
    autotools.configure()
    shelltools.cd("..")
    #shelltools.cd("gdata_plugin-0.5")
    #autotools.configure()
    #shelltools.cd("..")
    #shelltools.cd("geolocation_plugin-0.0.8")
    #autotools.configure()
    #shelltools.cd("..")
    shelltools.cd("gtkhtml2_viewer-0.34")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("mailmbox-1.15")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("newmail-0.0.16")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("notification_plugin-0.31")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("pdf_viewer-0.9.3")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("perl_plugin-0.9.20")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("python_plugin-0.11")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("rssyl-0.34")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("spam_report-0.3.17")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("tnef_parse-0.3.14")
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("vcalendar-2.0.14")
    autotools.configure()
    shelltools.cd("..")

def build():
    shelltools.cd("acpi_notifier-1.0.28")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("address_keeper-1.0.7")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("archive-0.6.13")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("att_remover-1.0.15")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("attachwarner-1.0")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("bsfilter_plugin-1.0.9")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("clamd-3.5.5")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("fancy-0.9.17")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("fetchinfo-plugin-0.4.25")
    autotools.make()
    shelltools.cd("..")
    #shelltools.cd("gdata_plugin-0.5")
    #autotools.make()
    #shelltools.cd("..")
    #shelltools.cd("geolocation_plugin-0.0.8")
    #autotools.make()
    #shelltools.cd("..")
    shelltools.cd("gtkhtml2_viewer-0.34")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("mailmbox-1.15")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("newmail-0.0.16")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("notification_plugin-0.31")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("pdf_viewer-0.9.3")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("perl_plugin-0.9.20")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("python_plugin-0.11")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("rssyl-0.34")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("spam_report-0.3.17")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("tnef_parse-0.3.14")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("vcalendar-2.0.14")
    autotools.make()
    shelltools.cd("..")

def install():    
    shelltools.cd("acpi_notifier-1.0.28")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/acpi-notifier", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/acpi-notifier", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/acpi-notifier", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/acpi-notifier", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/acpi-notifier", "README")
    shelltools.cd("..")
    shelltools.cd("address_keeper-1.0.7")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "README")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/address-keeper", "TODO")
    shelltools.cd("..")
    shelltools.cd("archive-0.6.13")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "README")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/archive", "TODO")
    shelltools.cd("..")
    shelltools.cd("att_remover-1.0.15")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/att-remover", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/att-remover", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/att-remover", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/att-remover", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/att-remover", "README")
    shelltools.cd("..")
    shelltools.cd("attachwarner-1.0")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "README")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/attachwarner", "TODO")
    shelltools.cd("..")
    shelltools.cd("bsfilter_plugin-1.0.9")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/bsfilter", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/bsfilter", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/bsfilter", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/bsfilter", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/bsfilter", "README")
    shelltools.cd("..")
    shelltools.cd("clamd-3.5.5")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/clamd", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/clamd", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/clamd", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/clamd", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/clamd", "README")
    shelltools.cd("..")
    shelltools.cd("fancy-0.9.17")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fancy", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fancy", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fancy", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fancy", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fancy", "README")
    shelltools.cd("..")
    shelltools.cd("fetchinfo-plugin-0.4.25")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fetchinfo", "ABOUT*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fetchinfo", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fetchinfo", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fetchinfo", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/fetchinfo", "README")
    shelltools.cd("..")
    #shelltools.cd("gdata_plugin-0.5")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #shelltools.cd("..")
    #shelltools.cd("geolocation_plugin-0.0.8")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #shelltools.cd("..")
    shelltools.cd("gtkhtml2_viewer-0.34")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/gtkhtml2", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/gtkhtml2", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/gtkhtml2", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/gtkhtml2", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/gtkhtml2", "README")
    shelltools.cd("..")
    shelltools.cd("mailmbox-1.15")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/mailmbox", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/mailmbox", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/mailmbox", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/mailmbox", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/mailmbox", "README")
    shelltools.cd("..")
    shelltools.cd("newmail-0.0.16")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/newmail", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/newmail", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/newmail", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/newmail", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/newmail", "README")
    shelltools.cd("..")
    shelltools.cd("notification_plugin-0.31")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/notification", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/notification", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/notification", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/notification", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/notification", "README")
    shelltools.cd("..")
    shelltools.cd("pdf_viewer-0.9.3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/pdf-viewer", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/pdf-viewer", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/pdf-viewer", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/pdf-viewer", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/pdf-viewer", "README")
    shelltools.cd("..")
    shelltools.cd("perl_plugin-0.9.20")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/perl", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/perl", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/perl", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/perl", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/perl", "README")
    shelltools.cd("..")
    shelltools.cd("python_plugin-0.11")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/python", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/python", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/python", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/python", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/python", "README")
    shelltools.cd("..")
    shelltools.cd("rssyl-0.34")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/rssyl", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/rssyl", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/rssyl", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/rssyl", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/rssyl", "README")
    shelltools.cd("..")
    shelltools.cd("spam_report-0.3.17")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/spam-report", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/spam-report", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/spam-report", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/spam-report", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/spam-report", "README")
    shelltools.cd("..")
    shelltools.cd("tnef_parse-0.3.14")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/tnef", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/tnef", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/tnef", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/tnef", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/tnef", "README")
    shelltools.cd("..")
    shelltools.cd("vcalendar-2.0.14")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/vcalendar", "AUTHORS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/vcalendar", "ChangeLog*")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/vcalendar", "COPYING")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/vcalendar", "NEWS")
    pisitools.insinto("/usr/share/doc/claws-mail-plugins/vcalendar", "README")