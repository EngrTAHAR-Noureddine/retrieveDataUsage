import docker


class Docker_collecter:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_count(self):
        try:
            info = self.client.info()
            containers_running = info["ContainersRunning"]
            containers_all = info["Containers"]
            container_paused = info["ContainersPaused"]
            containers_stopped = info["ContainersStopped"]
        except Exception:
            containers_running = None
            containers_all = None
            container_paused = None
            containers_stopped = None

        return [containers_all, containers_running, container_paused, containers_stopped]

# {
#   'ID': 'SL4K:5NZ4:YASY:AJAI:BL4D:EAJN:STF4:TK6P:5S5H:IEI6:6PMT:7OYV',
#   'Containers': 37,
#   'ContainersRunning': 37,
#   'ContainersPaused': 0,
#   'ContainersStopped': 0,
#   'Images': 33,
#   'Driver': 'overlay2',
#   'DriverStatus': [['Backing Filesystem', 'extfs'], ['Supports d_type', 'true'], ['Native Overlay Diff', 'true'], ['userxattr', 'false']], 'Plugins': {'Volume': ['local'], 'Network': ['bridge', 'host', 'ipvlan', 'macvlan', 'null', 'overlay'], 'Authorization': None, 'Log': ['awslogs', 'fluentd', 'gcplogs', 'gelf', 'journald', 'json-file', 'local', 'logentries', 'splunk', 'syslog']}, 'MemoryLimit': True, 'SwapLimit': False, 'KernelMemory': True, 'KernelMemoryTCP': True, 'CpuCfsPeriod': True, 'CpuCfsQuota': True, 'CPUShares': True, 'CPUSet': True, 'PidsLimit': True, 'IPv4Forwarding': True, 'BridgeNfIptables': True, 'BridgeNfIp6tables': True, 'Debug': False, 'NFd': 339, 'OomKillDisable': True, 'NGoroutines': 270, 'SystemTime': '2023-08-01T15:41:37.126342412Z', 'LoggingDriver': 'json-file', 'CgroupDriver': 'cgroupfs', 'CgroupVersion': '1', 'NEventsListener': 2, 'KernelVersion': '5.4.0-100-generic', 'OperatingSystem': 'Ubuntu 20.04.3 LTS', 'OSVersion': '20.04', 'OSType': 'linux', 'Architecture': 'x86_64', 'IndexServerAddress': 'https://index.docker.io/v1/', 'RegistryConfig': {'AllowNondistributableArtifactsCIDRs': [], 'AllowNondistributableArtifactsHostnames': [], 'InsecureRegistryCIDRs': ['127.0.0.0/8'], 'IndexConfigs': {'docker.io': {'Name': 'docker.io', 'Mirrors': [], 'Secure': True, 'Official': True}}, 'Mirrors': []}, 'NCPU': 12, 'MemTotal': 33552580608, 'GenericResources': None, 'DockerRootDir': '/var/lib/docker', 'HttpProxy': '', 'HttpsProxy': '', 'NoProxy': '', 'Name': 'aster', 'Labels': [], 'ExperimentalBuild': False, 'ServerVersion': '20.10.12', 'Runtimes': {'io.containerd.runc.v2': {'path': 'runc'}, 'io.containerd.runtime.v1.linux': {'path': 'runc'}, 'runc': {'path': 'runc'}}, 'DefaultRuntime': 'runc', 'Swarm': {'NodeID': '', 'NodeAddr': '', 'LocalNodeState': 'inactive', 'ControlAvailable': False, 'Error': '', 'RemoteManagers': None}, 'LiveRestoreEnabled': False, 'Isolation': '', 'InitBinary': 'docker-init', 'ContainerdCommit': {'ID': '7b11cfaabd73bb80907dd23182b9347b4245eb5d', 'Expected': '7b11cfaabd73bb80907dd23182b9347b4245eb5d'}, 'RuncCommit': {'ID': 'v1.0.2-0-g52b36a2', 'Expected': 'v1.0.2-0-g52b36a2'}, 'InitCommit': {'ID': 'de40ad0', 'Expected': 'de40ad0'}, 'SecurityOptions': ['apparmor', 'seccomp'], 'Warnings': ['WARNING: No swap limit support'], 'ExecutionDriver': '<not supported>'}