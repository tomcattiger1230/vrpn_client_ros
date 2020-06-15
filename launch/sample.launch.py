import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='vrpn_client_ros',
            node_executable='vrpn_client_node',
            output='screen',
            emulate_tty=True,
            parameters=["sample.conf.yaml"],
        ),
    ])
