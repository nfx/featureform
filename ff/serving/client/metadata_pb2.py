# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emetadata.proto\x12\"featureform.serving.metadata.proto\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\"|\n\x10SetStatusRequest\x12\x41\n\x08resource\x18\x01 \x01(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\",\n\x0bNameVariant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\"\x07\n\x05\x45mpty\"R\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_variant\x18\x03 \x01(\t\x12\x10\n\x08variants\x18\x04 \x03(\t\"4\n\x07\x43olumns\x12\x0e\n\x06\x65ntity\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\n\n\x02ts\x18\x03 \x01(\t\"\xf8\x02\n\x0e\x46\x65\x61tureVariant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\x12?\n\x06source\x18\x03 \x01(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0e\n\x06\x65ntity\x18\x05 \x01(\t\x12\x0f\n\x07\x63reated\x18\x06 \x01(\t\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x10\n\x08provider\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x45\n\x0ctrainingsets\x18\x0b \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12>\n\x07\x63olumns\x18\x0c \x01(\x0b\x32+.featureform.serving.metadata.proto.ColumnsH\x00\x42\n\n\x08location\"P\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_variant\x18\x03 \x01(\t\x12\x10\n\x08variants\x18\x04 \x03(\t\"\xf6\x02\n\x0cLabelVariant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12?\n\x06source\x18\x05 \x01(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x0e\n\x06\x65ntity\x18\x06 \x01(\t\x12\x0f\n\x07\x63reated\x18\x07 \x01(\t\x12\r\n\x05owner\x18\x08 \x01(\t\x12\x10\n\x08provider\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x45\n\x0ctrainingsets\x18\x0b \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12>\n\x07\x63olumns\x18\x0c \x01(\x0b\x32+.featureform.serving.metadata.proto.ColumnsH\x00\x42\n\n\x08location\"\x93\x03\n\x08Provider\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08software\x18\x04 \x01(\t\x12\x0c\n\x04team\x18\x05 \x01(\t\x12\x19\n\x11serialized_config\x18\x06 \x01(\x0c\x12\x0e\n\x06status\x18\x07 \x01(\t\x12@\n\x07sources\x18\x08 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x41\n\x08\x66\x65\x61tures\x18\t \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x45\n\x0ctrainingsets\x18\n \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12?\n\x06labels\x18\x0b \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"V\n\x0bTrainingSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_variant\x18\x03 \x01(\t\x12\x10\n\x08variants\x18\x04 \x03(\t\"\x8d\x02\n\x12TrainingSetVariant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x0f\n\x07\x63reated\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x41\n\x08\x66\x65\x61tures\x18\x08 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12>\n\x05label\x18\t \x01(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"\x86\x02\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x41\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12?\n\x06labels\x18\x05 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x45\n\x0ctrainingsets\x18\x06 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"\x85\x02\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x41\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12?\n\x06labels\x18\x05 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x45\n\x0ctrainingsets\x18\x06 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"\xb1\x02\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x41\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12?\n\x06labels\x18\x04 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x45\n\x0ctrainingsets\x18\x05 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12@\n\x07sources\x18\x06 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"Q\n\x06Source\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_variant\x18\x03 \x01(\t\x12\x10\n\x08variants\x18\x04 \x03(\t\"\x83\x04\n\rSourceVariant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t\x12L\n\x0etransformation\x18\x0e \x01(\x0b\x32\x32.featureform.serving.metadata.proto.TransformationH\x00\x12\x46\n\x0bprimaryData\x18\x0f \x01(\x0b\x32/.featureform.serving.metadata.proto.PrimaryDataH\x00\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x0f\n\x07\x63reated\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\r\n\x05table\x18\t \x01(\t\x12\x45\n\x0ctrainingsets\x18\n \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12\x41\n\x08\x66\x65\x61tures\x18\x0b \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\x12?\n\x06labels\x18\x0c \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariantB\x0c\n\ndefinition\"l\n\x0eTransformation\x12R\n\x11SQLTransformation\x18\x01 \x01(\x0b\x32\x35.featureform.serving.metadata.proto.SQLTransformationH\x00\x42\x06\n\x04type\"c\n\x11SQLTransformation\x12\r\n\x05query\x18\x01 \x01(\t\x12?\n\x06source\x18\x02 \x03(\x0b\x32/.featureform.serving.metadata.proto.NameVariant\"_\n\x0bPrimaryData\x12\x44\n\x05table\x18\x01 \x01(\x0b\x32\x33.featureform.serving.metadata.proto.PrimarySQLTableH\x00\x42\n\n\x08location\"\x1f\n\x0fPrimarySQLTable\x12\x0c\n\x04name\x18\x01 \x01(\t2\x89\x19\n\x08Metadata\x12h\n\x0cListFeatures\x12).featureform.serving.metadata.proto.Empty\x1a+.featureform.serving.metadata.proto.Feature0\x01\x12u\n\x14\x43reateFeatureVariant\x12\x32.featureform.serving.metadata.proto.FeatureVariant\x1a).featureform.serving.metadata.proto.Empty\x12h\n\x0bGetFeatures\x12(.featureform.serving.metadata.proto.Name\x1a+.featureform.serving.metadata.proto.Feature(\x01\x30\x01\x12}\n\x12GetFeatureVariants\x12/.featureform.serving.metadata.proto.NameVariant\x1a\x32.featureform.serving.metadata.proto.FeatureVariant(\x01\x30\x01\x12\x64\n\nListLabels\x12).featureform.serving.metadata.proto.Empty\x1a).featureform.serving.metadata.proto.Label0\x01\x12q\n\x12\x43reateLabelVariant\x12\x30.featureform.serving.metadata.proto.LabelVariant\x1a).featureform.serving.metadata.proto.Empty\x12\x64\n\tGetLabels\x12(.featureform.serving.metadata.proto.Name\x1a).featureform.serving.metadata.proto.Label(\x01\x30\x01\x12y\n\x10GetLabelVariants\x12/.featureform.serving.metadata.proto.NameVariant\x1a\x30.featureform.serving.metadata.proto.LabelVariant(\x01\x30\x01\x12p\n\x10ListTrainingSets\x12).featureform.serving.metadata.proto.Empty\x1a/.featureform.serving.metadata.proto.TrainingSet0\x01\x12}\n\x18\x43reateTrainingSetVariant\x12\x36.featureform.serving.metadata.proto.TrainingSetVariant\x1a).featureform.serving.metadata.proto.Empty\x12p\n\x0fGetTrainingSets\x12(.featureform.serving.metadata.proto.Name\x1a/.featureform.serving.metadata.proto.TrainingSet(\x01\x30\x01\x12\x85\x01\n\x16GetTrainingSetVariants\x12/.featureform.serving.metadata.proto.NameVariant\x1a\x36.featureform.serving.metadata.proto.TrainingSetVariant(\x01\x30\x01\x12\x66\n\x0bListSources\x12).featureform.serving.metadata.proto.Empty\x1a*.featureform.serving.metadata.proto.Source0\x01\x12s\n\x13\x43reateSourceVariant\x12\x31.featureform.serving.metadata.proto.SourceVariant\x1a).featureform.serving.metadata.proto.Empty\x12\x66\n\nGetSources\x12(.featureform.serving.metadata.proto.Name\x1a*.featureform.serving.metadata.proto.Source(\x01\x30\x01\x12{\n\x11GetSourceVariants\x12/.featureform.serving.metadata.proto.NameVariant\x1a\x31.featureform.serving.metadata.proto.SourceVariant(\x01\x30\x01\x12\x62\n\tListUsers\x12).featureform.serving.metadata.proto.Empty\x1a(.featureform.serving.metadata.proto.User0\x01\x12\x61\n\nCreateUser\x12(.featureform.serving.metadata.proto.User\x1a).featureform.serving.metadata.proto.Empty\x12\x62\n\x08GetUsers\x12(.featureform.serving.metadata.proto.Name\x1a(.featureform.serving.metadata.proto.User(\x01\x30\x01\x12j\n\rListProviders\x12).featureform.serving.metadata.proto.Empty\x1a,.featureform.serving.metadata.proto.Provider0\x01\x12i\n\x0e\x43reateProvider\x12,.featureform.serving.metadata.proto.Provider\x1a).featureform.serving.metadata.proto.Empty\x12j\n\x0cGetProviders\x12(.featureform.serving.metadata.proto.Name\x1a,.featureform.serving.metadata.proto.Provider(\x01\x30\x01\x12g\n\x0cListEntities\x12).featureform.serving.metadata.proto.Empty\x1a*.featureform.serving.metadata.proto.Entity0\x01\x12\x65\n\x0c\x43reateEntity\x12*.featureform.serving.metadata.proto.Entity\x1a).featureform.serving.metadata.proto.Empty\x12g\n\x0bGetEntities\x12(.featureform.serving.metadata.proto.Name\x1a*.featureform.serving.metadata.proto.Entity(\x01\x30\x01\x12\x64\n\nListModels\x12).featureform.serving.metadata.proto.Empty\x1a).featureform.serving.metadata.proto.Model0\x01\x12\x63\n\x0b\x43reateModel\x12).featureform.serving.metadata.proto.Model\x1a).featureform.serving.metadata.proto.Empty\x12\x64\n\tGetModels\x12(.featureform.serving.metadata.proto.Name\x1a).featureform.serving.metadata.proto.Model(\x01\x30\x01\x12t\n\x11SetResourceStatus\x12\x34.featureform.serving.metadata.proto.SetStatusRequest\x1a).featureform.serving.metadata.proto.Empty2\x98\x06\n\x03\x41pi\x12\x61\n\nCreateUser\x12(.featureform.serving.metadata.proto.User\x1a).featureform.serving.metadata.proto.Empty\x12i\n\x0e\x43reateProvider\x12,.featureform.serving.metadata.proto.Provider\x1a).featureform.serving.metadata.proto.Empty\x12s\n\x13\x43reateSourceVariant\x12\x31.featureform.serving.metadata.proto.SourceVariant\x1a).featureform.serving.metadata.proto.Empty\x12\x65\n\x0c\x43reateEntity\x12*.featureform.serving.metadata.proto.Entity\x1a).featureform.serving.metadata.proto.Empty\x12u\n\x14\x43reateFeatureVariant\x12\x32.featureform.serving.metadata.proto.FeatureVariant\x1a).featureform.serving.metadata.proto.Empty\x12q\n\x12\x43reateLabelVariant\x12\x30.featureform.serving.metadata.proto.LabelVariant\x1a).featureform.serving.metadata.proto.Empty\x12}\n\x18\x43reateTrainingSetVariant\x12\x36.featureform.serving.metadata.proto.TrainingSetVariant\x1a).featureform.serving.metadata.proto.EmptyB/Z-github.com/featureform/serving/metadata/protob\x06proto3')



_NAME = DESCRIPTOR.message_types_by_name['Name']
_SETSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SetStatusRequest']
_NAMEVARIANT = DESCRIPTOR.message_types_by_name['NameVariant']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_COLUMNS = DESCRIPTOR.message_types_by_name['Columns']
_FEATUREVARIANT = DESCRIPTOR.message_types_by_name['FeatureVariant']
_LABEL = DESCRIPTOR.message_types_by_name['Label']
_LABELVARIANT = DESCRIPTOR.message_types_by_name['LabelVariant']
_PROVIDER = DESCRIPTOR.message_types_by_name['Provider']
_TRAININGSET = DESCRIPTOR.message_types_by_name['TrainingSet']
_TRAININGSETVARIANT = DESCRIPTOR.message_types_by_name['TrainingSetVariant']
_ENTITY = DESCRIPTOR.message_types_by_name['Entity']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
_USER = DESCRIPTOR.message_types_by_name['User']
_SOURCE = DESCRIPTOR.message_types_by_name['Source']
_SOURCEVARIANT = DESCRIPTOR.message_types_by_name['SourceVariant']
_TRANSFORMATION = DESCRIPTOR.message_types_by_name['Transformation']
_SQLTRANSFORMATION = DESCRIPTOR.message_types_by_name['SQLTransformation']
_PRIMARYDATA = DESCRIPTOR.message_types_by_name['PrimaryData']
_PRIMARYSQLTABLE = DESCRIPTOR.message_types_by_name['PrimarySQLTable']
Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), {
  'DESCRIPTOR' : _NAME,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Name)
  })
_sym_db.RegisterMessage(Name)

SetStatusRequest = _reflection.GeneratedProtocolMessageType('SetStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETSTATUSREQUEST,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.SetStatusRequest)
  })
_sym_db.RegisterMessage(SetStatusRequest)

NameVariant = _reflection.GeneratedProtocolMessageType('NameVariant', (_message.Message,), {
  'DESCRIPTOR' : _NAMEVARIANT,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.NameVariant)
  })
_sym_db.RegisterMessage(NameVariant)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Empty)
  })
_sym_db.RegisterMessage(Empty)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Feature)
  })
_sym_db.RegisterMessage(Feature)

Columns = _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNS,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Columns)
  })
_sym_db.RegisterMessage(Columns)

FeatureVariant = _reflection.GeneratedProtocolMessageType('FeatureVariant', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREVARIANT,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.FeatureVariant)
  })
_sym_db.RegisterMessage(FeatureVariant)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Label)
  })
_sym_db.RegisterMessage(Label)

LabelVariant = _reflection.GeneratedProtocolMessageType('LabelVariant', (_message.Message,), {
  'DESCRIPTOR' : _LABELVARIANT,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.LabelVariant)
  })
_sym_db.RegisterMessage(LabelVariant)

Provider = _reflection.GeneratedProtocolMessageType('Provider', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDER,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Provider)
  })
_sym_db.RegisterMessage(Provider)

TrainingSet = _reflection.GeneratedProtocolMessageType('TrainingSet', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGSET,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.TrainingSet)
  })
_sym_db.RegisterMessage(TrainingSet)

TrainingSetVariant = _reflection.GeneratedProtocolMessageType('TrainingSetVariant', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGSETVARIANT,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.TrainingSetVariant)
  })
_sym_db.RegisterMessage(TrainingSetVariant)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Entity)
  })
_sym_db.RegisterMessage(Entity)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Model)
  })
_sym_db.RegisterMessage(Model)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.User)
  })
_sym_db.RegisterMessage(User)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Source)
  })
_sym_db.RegisterMessage(Source)

SourceVariant = _reflection.GeneratedProtocolMessageType('SourceVariant', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEVARIANT,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.SourceVariant)
  })
_sym_db.RegisterMessage(SourceVariant)

Transformation = _reflection.GeneratedProtocolMessageType('Transformation', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMATION,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.Transformation)
  })
_sym_db.RegisterMessage(Transformation)

SQLTransformation = _reflection.GeneratedProtocolMessageType('SQLTransformation', (_message.Message,), {
  'DESCRIPTOR' : _SQLTRANSFORMATION,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.SQLTransformation)
  })
_sym_db.RegisterMessage(SQLTransformation)

PrimaryData = _reflection.GeneratedProtocolMessageType('PrimaryData', (_message.Message,), {
  'DESCRIPTOR' : _PRIMARYDATA,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.PrimaryData)
  })
_sym_db.RegisterMessage(PrimaryData)

PrimarySQLTable = _reflection.GeneratedProtocolMessageType('PrimarySQLTable', (_message.Message,), {
  'DESCRIPTOR' : _PRIMARYSQLTABLE,
  '__module__' : 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:featureform.serving.metadata.proto.PrimarySQLTable)
  })
_sym_db.RegisterMessage(PrimarySQLTable)

_METADATA = DESCRIPTOR.services_by_name['Metadata']
_API = DESCRIPTOR.services_by_name['Api']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/featureform/serving/metadata/proto'
  _NAME._serialized_start=54
  _NAME._serialized_end=74
  _SETSTATUSREQUEST._serialized_start=76
  _SETSTATUSREQUEST._serialized_end=200
  _NAMEVARIANT._serialized_start=202
  _NAMEVARIANT._serialized_end=246
  _EMPTY._serialized_start=248
  _EMPTY._serialized_end=255
  _FEATURE._serialized_start=257
  _FEATURE._serialized_end=339
  _COLUMNS._serialized_start=341
  _COLUMNS._serialized_end=393
  _FEATUREVARIANT._serialized_start=396
  _FEATUREVARIANT._serialized_end=772
  _LABEL._serialized_start=774
  _LABEL._serialized_end=854
  _LABELVARIANT._serialized_start=857
  _LABELVARIANT._serialized_end=1231
  _PROVIDER._serialized_start=1234
  _PROVIDER._serialized_end=1637
  _TRAININGSET._serialized_start=1639
  _TRAININGSET._serialized_end=1725
  _TRAININGSETVARIANT._serialized_start=1728
  _TRAININGSETVARIANT._serialized_end=1997
  _ENTITY._serialized_start=2000
  _ENTITY._serialized_end=2262
  _MODEL._serialized_start=2265
  _MODEL._serialized_end=2526
  _USER._serialized_start=2529
  _USER._serialized_end=2834
  _SOURCE._serialized_start=2836
  _SOURCE._serialized_end=2917
  _SOURCEVARIANT._serialized_start=2920
  _SOURCEVARIANT._serialized_end=3435
  _TRANSFORMATION._serialized_start=3437
  _TRANSFORMATION._serialized_end=3545
  _SQLTRANSFORMATION._serialized_start=3547
  _SQLTRANSFORMATION._serialized_end=3646
  _PRIMARYDATA._serialized_start=3648
  _PRIMARYDATA._serialized_end=3743
  _PRIMARYSQLTABLE._serialized_start=3745
  _PRIMARYSQLTABLE._serialized_end=3776
  _METADATA._serialized_start=3779
  _METADATA._serialized_end=6988
  _API._serialized_start=6991
  _API._serialized_end=7783
# @@protoc_insertion_point(module_scope)