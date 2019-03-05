# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/ad_schedule_view_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import ad_schedule_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__schedule__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/ad_schedule_view_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v0.servicesB\032AdScheduleViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services\352\002$Google::Ads::GoogleAds::V0::Services'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v0/proto/services/ad_schedule_view_service.proto\x12 google.ads.googleads.v0.services\x1a>google/ads/googleads_v0/proto/resources/ad_schedule_view.proto\x1a\x1cgoogle/api/annotations.proto\"1\n\x18GetAdScheduleViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xd7\x01\n\x15\x41\x64ScheduleViewService\x12\xbd\x01\n\x11GetAdScheduleView\x12:.google.ads.googleads.v0.services.GetAdScheduleViewRequest\x1a\x31.google.ads.googleads.v0.resources.AdScheduleView\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v0/{resource_name=customers/*/adScheduleViews/*}B\x81\x02\n$com.google.ads.googleads.v0.servicesB\x1a\x41\x64ScheduleViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Services\xea\x02$Google::Ads::GoogleAds::V0::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__schedule__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETADSCHEDULEVIEWREQUEST = _descriptor.Descriptor(
  name='GetAdScheduleViewRequest',
  full_name='google.ads.googleads.v0.services.GetAdScheduleViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetAdScheduleViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=250,
)

DESCRIPTOR.message_types_by_name['GetAdScheduleViewRequest'] = _GETADSCHEDULEVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdScheduleViewRequest = _reflection.GeneratedProtocolMessageType('GetAdScheduleViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADSCHEDULEVIEWREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.ad_schedule_view_service_pb2'
  ,
  __doc__ = """Request message for
  [AdScheduleViewService.GetAdScheduleView][google.ads.googleads.v0.services.AdScheduleViewService.GetAdScheduleView].
  
  
  Attributes:
      resource_name:
          The resource name of the ad schedule view to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetAdScheduleViewRequest)
  ))
_sym_db.RegisterMessage(GetAdScheduleViewRequest)


DESCRIPTOR._options = None

_ADSCHEDULEVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='AdScheduleViewService',
  full_name='google.ads.googleads.v0.services.AdScheduleViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=253,
  serialized_end=468,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdScheduleView',
    full_name='google.ads.googleads.v0.services.AdScheduleViewService.GetAdScheduleView',
    index=0,
    containing_service=None,
    input_type=_GETADSCHEDULEVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__schedule__view__pb2._ADSCHEDULEVIEW,
    serialized_options=_b('\202\323\344\223\0023\0221/v0/{resource_name=customers/*/adScheduleViews/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADSCHEDULEVIEWSERVICE)

DESCRIPTOR.services_by_name['AdScheduleViewService'] = _ADSCHEDULEVIEWSERVICE

# @@protoc_insertion_point(module_scope)