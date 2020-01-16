# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# #
# #
# class ActionReturnQuestion(Action):
#
#     def name(self) -> Text:
#         return "action_return_q"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="test")
#
#         return []

class ActionSetIntents(Action):
	def name(self):
		return "action_set_intents"

	def run(self,dispatcher,tracker,domain):

		intent_current = tracker.latest_message['intent'].get('name')
		return[SlotSet("intents",intent_current)]

# class ActionSaveIntent(Action):

# 	def name(self) -> Text:
# 		return "action_saveIntent"

# 	def run(self, dispatcher, tracker, domain):

# 		intent = tracker.latest_message['intent'].get('name')
# 		return [SlotSet('cur_context', intent)]

# class ActionGetDetails(Action):

#     def name(self) -> Text:
#         return "action_getDetails"

#     def run(self, dispatcher, tracker, domain):
#         # CALLING THE ActionSaveIntent.run METHOD and storing the data in intent variable
#         intent = tracker.get_slot("cur_context")