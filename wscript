## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    obj = bld.create_ns3_module('maher', ['internet', 'wifi'])

    obj.source = [
        'model/maher-information-element-vector.cc',
        'model/maher-point-device.cc',
        'model/maher-l2-routing-protocol.cc',
        'model/maher-wifi-beacon.cc',
        'model/maher-wifi-interface-mac.cc',
        'model/dot11s/ie-dot11s-beacon-timing.cc',
        'model/dot11s/ie-dot11s-configuration.cc',
        'model/dot11s/ie-dot11s-id.cc',
        'model/dot11s/ie-dot11s-peer-management.cc',
        'model/dot11s/ie-dot11s-preq.cc',
        'model/dot11s/ie-dot11s-prep.cc',
        'model/dot11s/ie-dot11s-perr.cc',
        'model/dot11s/ie-dot11s-rann.cc',
        'model/dot11s/ie-dot11s-peering-protocol.cc',
        'model/dot11s/ie-dot11s-metric-report.cc',
        'model/dot11s/dot11s-mac-header.cc',
        'model/dot11s/peer-link-frame.cc',
        'model/dot11s/peer-link.cc',
        'model/dot11s/peer-management-protocol-mac.cc',
        'model/dot11s/peer-management-protocol.cc',
        'model/dot11s/hwmp-tag.cc',
        'model/dot11s/hwmp-rtable.cc',
        'model/dot11s/hwmp-protocol-mac.cc',
        'model/dot11s/hwmp-protocol.cc',
        'model/dot11s/airtime-metric.cc',
        'model/flame/flame-header.cc',
        'model/flame/flame-rtable.cc',
        'model/flame/flame-protocol-mac.cc',
        'model/flame/flame-protocol.cc',
        'helper/maher-helper.cc',
        'helper/maher-stack-installer.cc',
        'helper/dot11s/dot11s-installer.cc',
        'helper/flame/flame-installer.cc',
        ]

    obj_test = bld.create_ns3_module_test_library('maher')
    obj_test.source = [
        'test/maher-information-element-vector-test-suite.cc',
        'test/dot11s/dot11s-test-suite.cc',
        'test/dot11s/pmp-regression.cc',
        'test/dot11s/hwmp-reactive-regression.cc',
        'test/dot11s/hwmp-proactive-regression.cc',
        'test/dot11s/hwmp-simplest-regression.cc',
        'test/dot11s/hwmp-target-flags-regression.cc',
        'test/dot11s/regression.cc',
        'test/flame/flame-test-suite.cc',
        'test/flame/flame-regression.cc',
        'test/flame/regression.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'maher'
    headers.source = [
        'model/maher-information-element-vector.h',
        'model/maher-point-device.h',
        'model/maher-l2-routing-protocol.h',
        'model/maher-wifi-beacon.h',
        'model/maher-wifi-interface-mac.h',
        'model/maher-wifi-interface-mac-plugin.h',
        'model/dot11s/hwmp-protocol.h',
        'model/dot11s/peer-management-protocol.h',
        'model/dot11s/ie-dot11s-beacon-timing.h',
        'model/dot11s/ie-dot11s-configuration.h',
        'model/dot11s/ie-dot11s-peer-management.h',
        'model/dot11s/ie-dot11s-id.h',
        'model/dot11s/peer-link.h',
        'model/dot11s/dot11s-mac-header.h',
        'model/dot11s/peer-link-frame.h',
        'model/dot11s/hwmp-rtable.h',
        'model/dot11s/ie-dot11s-peering-protocol.h',
        'model/dot11s/ie-dot11s-metric-report.h',
        'model/dot11s/ie-dot11s-perr.h',
        'model/dot11s/ie-dot11s-prep.h',
        'model/dot11s/ie-dot11s-preq.h',
        'model/dot11s/ie-dot11s-rann.h',
        'model/flame/flame-protocol.h',
        'model/flame/flame-header.h',
        'model/flame/flame-rtable.h',
        'model/flame/flame-protocol-mac.h',
        'helper/maher-helper.h',
        'helper/maher-stack-installer.h',
        'helper/dot11s/dot11s-installer.h',
        'helper/flame/flame-installer.h',
        ]

    if bld.env['ENABLE_EXAMPLES']:
        bld.recurse('examples')

    bld.ns3_python_bindings()
