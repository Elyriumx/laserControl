from concurrent import futures
import grpc
import laserControl_pb2
import laserControl_pb2_grpc

from laser import Laser

class LaserControlService(laserControl_pb2_grpc.LaserControlService):

    laser = Laser()

    def SetBiasVoltage(self, request, context):
        response = laserControl_pb2.SetBiasVoltageResponse()
        response.success = self.laser.setBiasVoltage(request.voltage)
        return response
    
    def GetLaserStatus(self, request, context):
        response = laserControl_pb2.GetLaserStatusResponse()
        response.status = self.laser.getStatus().value
        return response
    
    def EnableLaser(self, request, context):
        response = laserControl_pb2.EnableLaserResponse()
        response.success = self.laser.enableLaser()
        return response
    
    def DisableLaser(self, request, context):
        response = laserControl_pb2.DisableLaserResponse()
        self.laser.disableLaser()
        return response

def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    laserControl_pb2_grpc.add_LaserControlServiceServicer_to_server(LaserControlService(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
