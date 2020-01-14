## first story
* greet
 - utter_greet
 > ask_question

## monitor_issue+flicker+affirm+ticket
> ask_question
* problem_monitor
 - utter_monitor_question
* affirm
 - utter_monitor_answer
* problem_monitor_flicker
 - utter_monitor_flicker
 - utter_further_help
* ticket_creation
 - utter_ticket_reply
 - action_restart

## monitor_issue+flicker+affirm+bye
> ask_question
* problem_monitor
 - utter_monitor_question
* affirm
 - utter_monitor_answer
* problem_monitor_flicker
 - utter_monitor_flicker
 - utter_further_help
* goodbye
 - utter_goodbye
 - action_restart

## monitor_issue+flicker+affirm+analyst
> ask_question
* problem_monitor
 - utter_monitor_question
* affirm
 - utter_monitor_answer
* problem_monitor_flicker
 - utter_monitor_flicker
 - utter_further_help
* need_analyst
 - utter_analyst_reply
 - action_restart

## monitor_issue + deny
> ask_question
* problem_monitor
 - utter_monitor_question
* deny
 - utter_generic_deny
 - action_restart

## monitor_flicker+affirm+ticket
> ask_question
* problem_monitor_flicker
 - utter_monitor_flicker_confirm
* affirm
 - utter_monitor_flicker
 - utter_further_help
* ticket_creation
 - utter_ticket_reply
 - action_restart

## monitor_flicker+affirm+analyst
> ask_question
* problem_monitor_flicker
 - utter_monitor_flicker_confirm
* affirm
 - utter_monitor_flicker
 - utter_further_help
* need_analyst
 - utter_analyst_reply
 - action_restart

## monitor_flicker+affirm+bye
> ask_question
* problem_monitor_flicker
 - utter_monitor_flicker_confirm
* affirm
 - utter_monitor_flicker
 - utter_further_help
* goodbye
 - utter_goodbye
 - action_restart 

## monitor_flicker + deny
> ask_question
* problem_monitor_flicker
 - utter_monitor_flicker_confirm
* deny
 - utter_generic_deny
 - action_restart

## keyboard_issue + broken_keyboard + affirm
> ask_question
* problem_keyboard
 - utter_keyboard_question
* affirm
 - utter_keyboard_answer
* problem_keyboard_broken
 - utter_keyboard_broken
 - utter_goodbye
 - action_restart

## keyboard_issue + deny
> ask_question
* problem_keyboard
 - utter_keyboard_question
* deny
 - utter_generic_deny
 - action_restart

## keyboard_flicker + affirm
> ask_question
* problem_keyboard_broken
 - utter_keyboard_broken_confirm
* affirm
 - utter_keyboard_broken
 - utter_goodbye
 - action_restart

## monitor_flicker + deny
> ask_question
* problem_keyboard_broken
 - utter_keyboard_broken_confirm
* deny
 - utter_generic_deny
 - action_restart