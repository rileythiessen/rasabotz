## user has issue
* greet
  - utter_greet
* problem{"problem_object":"mouse"}
  - utter_ask_problem
* goodbye
  - utter_goodbye

## user needs software
* greet
  - utter_greet
* software_request{"software_type":"adobe something"}
  - utter_ask_software

## user needs hardware
* greet
  - utter_greet
* hardware_request{"hardware_type":"laptop"}
  - utter_ask_hardware

## say goodbye
* goodbye
  - utter_goodbye