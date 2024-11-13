from google.protobuf.message import Message
from google.protobuf.descriptor import Descriptor, FieldDescriptor
from autogen_core.base._serialization import ProtobufMessageSerializer


class TestProtoMessage(Message):
    """A simple test proto message."""

    DESCRIPTOR = Descriptor(
        name="TestProtoMessage",
        full_name="TestProtoMessage",
        filename=None,
        file=None,
        containing_type=None,
        fields=[
            FieldDescriptor(
                name="foo",
                full_name="TestProtoMessage.foo",
                index=0,
                number=1,
                type=FieldDescriptor.TYPE_INT32,
                cpp_type=FieldDescriptor.CPPTYPE_INT32,
                label=FieldDescriptor.LABEL_OPTIONAL,
                has_default_value=False,
                default_value=0,
                message_type=None,
                enum_type=None,
                containing_type=None,
                is_extension=False,
                extension_scope=None,
                options=None,
            ),
        ],
        extensions=[],
        nested_types=[],
        enum_types=[],
        options=None,
    )


def test_protobuf_message_serializer_serialize():
    """Test serialization of a protobuf message."""
    serializer = ProtobufMessageSerializer(TestProtoMessage)
    message = TestProtoMessage(foo=42)
    serialized_message = serializer.serialize(message)
    expected_output = b"\x08*"  # Serialized form of TestProtoMessage with foo=42
    assert serialized_message == expected_output


def test_protobuf_message_serializer_deserialize():
    """Test deserialization of a protobuf message."""
    serializer = ProtobufMessageSerializer(TestProtoMessage)
    payload = b"\x08*"  # Serialized form of TestProtoMessage with foo=42
    message = serializer.deserialize(payload)
    expected_message = TestProtoMessage(foo=42)
    assert message == expected_message
