# -*- coding: utf-8 -*-
from django.db import models


class NetworkElement(models.Model):
    identifier = models.CharField(max_length=50, null=False, blank=False)
    ip = models.IPAddressField(null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    port = models.IntegerField(null=False, blank=False, default=22)
    os = models.CharField(max_length=80, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parent_network_element')
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    memory_size_in_m = models.IntegerField(null=True, blank=True)
    vendor = models.CharField(max_length=255, null=True, blank=True)
    model_or_part_number = models.CharField(max_length=255, null=True, blank=True)
    cpu_info = models.CharField(max_length=255, null=True, blank=True)
    hard_disk_size_in_m = models.IntegerField(null=True, blank=True)
    other_info = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return self.identifier
