from vocode.streaming.action.base_action import BaseAction
from vocode.streaming.models.actions import ActionConfig
from vocode.streaming.action.transfer_call import TransferCall, TransferCallActionConfig


class ActionFactory:
    def create_action(self, action_config: ActionConfig) -> BaseAction:
        if isinstance(action_config, TransferCallActionConfig):
            return TransferCall(action_config)
        else:
            raise Exception("Invalid action type")
