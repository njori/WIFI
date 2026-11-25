from app.models.traffic import Traffic
from app.repositories.traffic_repository import TrafficRepository


class TrafficService:

    @staticmethod
    def save(
        router,
        interface,
        bytes_in,
        bytes_out,
        packets_in,
        packets_out,
        upload,
        download,
        utilization
    ):

        traffic = Traffic(

            router_id=router.id,

            interface=interface,

            bytes_in=bytes_in,

            bytes_out=bytes_out,

            packets_in=packets_in,

            packets_out=packets_out,

            upload=upload,

            download=download,

            utilization=utilization
        )

        return TrafficRepository.create(
            traffic
        )

    @staticmethod
    def latest():

        return TrafficRepository.latest()

    @staticmethod
    def router_history(router_id):

        return TrafficRepository.router_history(
            router_id
        )