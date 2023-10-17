# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import laserControl_pb2 as laserControl__pb2


class LaserControlServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLaserStatus = channel.unary_unary(
                '/laserControl.LaserControlService/GetLaserStatus',
                request_serializer=laserControl__pb2.GetLaserStatusRequest.SerializeToString,
                response_deserializer=laserControl__pb2.GetLaserStatusResponse.FromString,
                )
        self.SetBiasVoltage = channel.unary_unary(
                '/laserControl.LaserControlService/SetBiasVoltage',
                request_serializer=laserControl__pb2.SetBiasVoltageRequest.SerializeToString,
                response_deserializer=laserControl__pb2.SetBiasVoltageResponse.FromString,
                )
        self.EnableLaser = channel.unary_unary(
                '/laserControl.LaserControlService/EnableLaser',
                request_serializer=laserControl__pb2.EnableLaserRequest.SerializeToString,
                response_deserializer=laserControl__pb2.EnableLaserResponse.FromString,
                )
        self.DisableLaser = channel.unary_unary(
                '/laserControl.LaserControlService/DisableLaser',
                request_serializer=laserControl__pb2.DisableLaserRequest.SerializeToString,
                response_deserializer=laserControl__pb2.DisableLaserResponse.FromString,
                )


class LaserControlServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLaserStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBiasVoltage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableLaser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableLaser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LaserControlServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLaserStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLaserStatus,
                    request_deserializer=laserControl__pb2.GetLaserStatusRequest.FromString,
                    response_serializer=laserControl__pb2.GetLaserStatusResponse.SerializeToString,
            ),
            'SetBiasVoltage': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBiasVoltage,
                    request_deserializer=laserControl__pb2.SetBiasVoltageRequest.FromString,
                    response_serializer=laserControl__pb2.SetBiasVoltageResponse.SerializeToString,
            ),
            'EnableLaser': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableLaser,
                    request_deserializer=laserControl__pb2.EnableLaserRequest.FromString,
                    response_serializer=laserControl__pb2.EnableLaserResponse.SerializeToString,
            ),
            'DisableLaser': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableLaser,
                    request_deserializer=laserControl__pb2.DisableLaserRequest.FromString,
                    response_serializer=laserControl__pb2.DisableLaserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'laserControl.LaserControlService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LaserControlService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLaserStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/laserControl.LaserControlService/GetLaserStatus',
            laserControl__pb2.GetLaserStatusRequest.SerializeToString,
            laserControl__pb2.GetLaserStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetBiasVoltage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/laserControl.LaserControlService/SetBiasVoltage',
            laserControl__pb2.SetBiasVoltageRequest.SerializeToString,
            laserControl__pb2.SetBiasVoltageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableLaser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/laserControl.LaserControlService/EnableLaser',
            laserControl__pb2.EnableLaserRequest.SerializeToString,
            laserControl__pb2.EnableLaserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableLaser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/laserControl.LaserControlService/DisableLaser',
            laserControl__pb2.DisableLaserRequest.SerializeToString,
            laserControl__pb2.DisableLaserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)