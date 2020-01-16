## first story
* greet
 - utter_greet
 > ask_question

## issue
> ask_question
* generic_problem
 - utter_generic_issue
 > issue_asked

## issue+monitor
> issue_asked
* problem_monitor
 - utter_monitor_question 
 > monitor_issue_asked

## issue+monitor+deny
> monitor_issue_asked
* deny
 - utter_further_help
 > monitor_issue_ticket

## issue+monitor+deny+affirm
> monitor_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+monitor+deny+deny
> monitor_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+monitor+affirm
> monitor_issue_asked
* affirm
 - utter_generic_apology
 - utter_monitor_options
 > specific_monitor_issue

## issue+monitor+affirm+other
> specific_monitor_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+mykey+affirm+other
> specific_mykey_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+phone+affirm+other
> specific_phone_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+outlook+affirm+other
> specific_outlook_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+vpn+affirm+other
> specific_vpn_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+printer+affirm+other
> specific_printer_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+keyboard+affirm+other
> specific_keyboard_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+monitor+flicker
> specific_monitor_issue
* problem_monitor_flicker
 - utter_monitor_flicker
 > monitor_fixed_q

## issue+monitor+broken
> specific_monitor_issue
* problem_monitor_broken
 - utter_generic_broken
 > broken_q

## issue+broken+affirm
> broken_q
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+broken+deny
> broken_q
* deny
 - utter_call_it
 - action_restart

## issue+monitor+flicker+fixed
> monitor_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+monitor+flicker+notfixed
> monitor_fixed_q
* deny
 - utter_ticket_reply
 > monitor_not_fixed

## issue+monitor+flicker+notfixed+affirmanalyst
> monitor_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+monitor+flicker+notfixed+denyanalyst
> monitor_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+keyboard
> issue_asked
* problem_keyboard
 - utter_keyboard_question
 > keyboard_issue_asked

## issue+keyboard+deny
> keyboard_issue_asked
* deny
 - utter_further_help
 > keyboard_issue_ticket

## issue+keyboard+deny+affirm
> keyboard_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+keyboard+deny+deny
> keyboard_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+keyboard+affirm
> keyboard_issue_asked
* affirm
 - utter_generic_apology
 - utter_keyboard_options
 > specific_keyboard_issue

## issue+keyboard+broken
> specific_keyboard_issue
* problem_keyboard_broken
 - utter_generic_broken
 > broken_q

## issue+printer
> issue_asked
* problem_printer
 - utter_printer_question 
 > printer_issue_asked

## issue+printer+deny
> printer_issue_asked
* deny
 - utter_further_help
 > printer_issue_ticket

## issue+printer+deny+affirm
> printer_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+printer+deny+deny
> printer_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+printer+affirm
> printer_issue_asked
* affirm
 - utter_generic_apology
 - utter_printer_options
 > specific_printer_issue

## issue+printer+slow
> specific_printer_issue
* problem_printer_slow
 - utter_printer_slow
 > printer_slow_fixed_q

## issue+printer+slow+fixed
> printer_slow_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+printer+slow+notfixed
> printer_slow_fixed_q
* deny
 - utter_ticket_reply
 > printer_slow_not_fixed

## issue+printer+slow+notfixed+affirmanalyst
> printer_slow_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+printer+slow+notfixed+denyanalyst
> printer_slow_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+printer+error
> specific_printer_issue
* problem_printer_error
 - utter_printer_error
 > printer_error_fixed_q

## issue+printer+error+fixed
> printer_error_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+printer+error+notfixed
> printer_error_fixed_q
* deny
 - utter_ticket_reply
 > printer_error_not_fixed

## issue+printer+error+notfixed+affirmanalyst
> printer_error_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+printer+error+notfixed+denyanalyst
> printer_error_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+printer+missing
> specific_printer_issue
* problem_printer_missing
 - utter_printer_missing
 > printer_missing_fixed_q

## issue+printer+missing+fixed
> printer_missing_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+printer+missing+notfixed
> printer_missing_fixed_q
* deny
 - utter_ticket_reply
 > printer_missing_not_fixed

## issue+printer+missing+notfixed+affirmanalyst
> printer_missing_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+printer+missing+notfixed+denyanalyst
> printer_missing_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+vpn
> issue_asked
* problem_vpn
 - utter_vpn_question 
 > vpn_issue_asked

## issue+vpn+deny
> vpn_issue_asked
* deny
 - utter_further_help
 > vpn_issue_ticket

## issue+vpn+deny+affirm
> vpn_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+vpn+deny+deny
> vpn_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+vpn+affirm
> vpn_issue_asked
* affirm
 - utter_generic_apology
 - utter_vpn_options
 > specific_vpn_issue

## issue+vpn+connection
> specific_vpn_issue
* problem_vpn_connection
 - utter_vpn_connection
 > vpn_connection_fixed_q

## issue+vpn+connection+fixed
> vpn_connection_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+vpn+connection+notfixed
> vpn_connection_fixed_q
* deny
 - utter_ticket_reply
 > vpn_connection_not_fixed

## issue+vpn+connection+notfixed+affirmanalyst
> vpn_connection_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+vpn+connection+notfixed+denyanalyst
> vpn_connection_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+vpn+entrust
> specific_vpn_issue
* problem_vpn_entrust
 - utter_vpn_entrust
 > vpn_entrust_fixed_q

## issue+vpn+entrust+fixed
> vpn_entrust_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+vpn+entrust+notfixed
> vpn_entrust_fixed_q
* deny
 - utter_ticket_reply
 > vpn_entrust_not_fixed

## issue+vpn+entrust+notfixed+affirmanalyst
> vpn_entrust_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+vpn+entrust+notfixed+denyanalyst
> vpn_entrust_not_fixed
* deny
 - utter_goodbye
 - action_restart


## issue+mykey
> issue_asked
* problem_mykey
 - utter_mykey_question 
 > mykey_issue_asked

## issue+mykey+deny
> mykey_issue_asked
* deny
 - utter_further_help
 > mykey_issue_ticket

## issue+mykey+deny+affirm
> mykey_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+mykey+deny+deny
> mykey_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+mykey+affirm
> mykey_issue_asked
* affirm
 - utter_generic_apology
 - utter_mykey_options
 > specific_mykey_issue


## issue+mykey+general
> specific_mykey_issue
* problem_mykey_general
 - utter_mykey_general
 > mykey_general_fixed_q

## issue+mykey+general+fixed
> mykey_general_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+mykey+general+notfixed
> mykey_general_fixed_q
* deny
 - utter_ticket_reply
 > mykey_general_not_fixed

## issue+mykey+general+notfixed+affirmanalyst
> mykey_general_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+mykey+general+notfixed+denyanalyst
> mykey_general_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+outlook
> issue_asked
* problem_outlook
 - utter_outlook_question 
 > outlook_issue_asked

## issue+outlook+deny
> outlook_issue_asked
* deny
 - utter_further_help
 > outlook_issue_ticket

## issue+outlook+deny+affirm
> outlook_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+outlook+deny+deny
> outlook_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+outlook+affirm
> outlook_issue_asked
* affirm
 - utter_generic_apology
 - utter_outlook_options
 > specific_outlook_issue

## issue+outlook+wopen
> specific_outlook_issue
* problem_outlook_wopen
 - utter_outlook_wopen
 > outlook_wopen_fixed_q

## issue+outlook+wopen+fixed
> outlook_wopen_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+outlook+wopen+notfixed
> outlook_wopen_fixed_q
* deny
 - utter_ticket_reply
 > outlook_wopen_not_fixed

## issue+outlook+wopen+notfixed+affirmanalyst
> outlook_wopen_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+outlook+wopen+notfixed+denyanalyst
> outlook_wopen_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+outlook+password
> specific_outlook_issue
* problem_outlook_password
 - utter_outlook_password
 > outlook_password_fixed_q

## issue+outlook+password+fixed
> outlook_password_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+outlook+password+notfixed
> outlook_password_fixed_q
* deny
 - utter_ticket_reply
 > outlook_password_not_fixed

## issue+outlook+password+notfixed+affirmanalyst
> outlook_password_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+outlook+password+notfixed+denyanalyst
> outlook_password_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+phone
> issue_asked
* problem_phone
 - utter_phone_question 
 > phone_issue_asked

## issue+phone+deny
> phone_issue_asked
* deny
 - utter_further_help
 > phone_issue_ticket

## issue+phone+deny+affirm
> phone_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+phone+deny+deny
> phone_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+phone+affirm
> phone_issue_asked
* affirm
 - utter_generic_apology
 - utter_phone_options
 > specific_phone_issue

## issue+phone+other
> specific_phone_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+other+affirm
> other_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+other+deny
> other_ticket
* deny
 - utter_call_it
 - action_restart

## issue+phone+password
> specific_phone_issue
* problem_phone_password
 - utter_phone_password
 > phone_password_fixed_q

## issue+phone+password+fixed
> phone_password_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+phone+password+notfixed
> phone_password_fixed_q
* deny
 - utter_ticket_reply
 > phone_password_not_fixed

## issue+phone+password+notfixed+affirmanalyst
> phone_password_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+phone+password+notfixed+denyanalyst
> phone_password_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+phone+broken
> specific_phone_issue
* problem_phone_broken
 - utter_generic_broken
 > broken_q

## issue+mouse
> issue_asked
* problem_mouse
 - utter_mouse_question 
 > mouse_issue_asked

## issue+mouse+deny
> mouse_issue_asked
* deny
 - utter_further_help
 > mouse_issue_ticket

## issue+mouse+deny+affirm
> mouse_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+mouse+deny+deny
> mouse_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+mouse+affirm
> mouse_issue_asked
* affirm
 - utter_generic_apology
 - utter_mouse_options
 > specific_mouse_issue

## issue+mouse+affirm+other
> specific_mouse_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+mouse+broken
> specific_mouse_issue
* problem_mouse_broken
 - utter_generic_broken
 > broken_q

## issue+sound
> issue_asked
* problem_sound
 - utter_sound_question 
 > sound_issue_asked

## issue+sound+deny
> sound_issue_asked
* deny
 - utter_further_help
 > sound_issue_ticket

## issue+sound+deny+affirm
> sound_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+sound+deny+deny
> sound_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+sound+affirm
> sound_issue_asked
* affirm
 - utter_generic_apology
 - utter_sound_options
 > specific_sound_issue

## issue+sound+affirm+other
> specific_sound_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+sound+nwork
> specific_sound_issue
* problem_sound_nwork
 - utter_sound_nwork
 > sound_nwork_fixed_q

## issue+sound+nwork+fixed
> sound_nwork_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+sound+nwork+notfixed
> sound_nwork_fixed_q
* deny
 - utter_ticket_reply
 > sound_nwork_not_fixed

## issue+sound+nwork+notfixed+affirmanalyst
> sound_nwork_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+sound+nwork+notfixed+denyanalyst
> sound_nwork_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+sound+hw
> specific_sound_issue
* problem_sound_hw
 - utter_sound_hw
 > sound_hw_fixed_q

## issue+sound+hw+fixed
> sound_hw_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+sound+hw+notfixed
> sound_hw_fixed_q
* deny
 - utter_ticket_reply
 > sound_hw_not_fixed

## issue+sound+hw+notfixed+affirmanalyst
> sound_hw_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+sound+hw+notfixed+denyanalyst
> sound_hw_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+word
> issue_asked
* problem_word
 - utter_word_question 
 > word_issue_asked

## issue+word+deny
> word_issue_asked
* deny
 - utter_further_help
 > word_issue_ticket

## issue+word+deny+affirm
> word_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+word+deny+deny
> word_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+word+affirm
> word_issue_asked
* affirm
 - utter_generic_apology
 - utter_word_options
 > specific_word_issue

## issue+word+affirm+other
> specific_word_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket


## issue+word+generalerrors
> specific_word_issue
* problem_word_generalerrors
 - utter_word_generalerrors
 > word_generalerrors_fixed_q

## issue+word+generalerrors+fixed
> word_generalerrors_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+word+generalerrors+notfixed
> word_generalerrors_fixed_q
* deny
 - utter_ticket_reply
 > word_generalerrors_not_fixed

## issue+word+generalerrors+notfixed+affirmanalyst
> word_generalerrors_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+word+generalerrors+notfixed+denyanalyst
> word_generalerrors_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+powerpoint
> issue_asked
* problem_powerpoint
 - utter_powerpoint_question 
 > powerpoint_issue_asked

## issue+powerpoint+deny
> powerpoint_issue_asked
* deny
 - utter_further_help
 > powerpoint_issue_ticket

## issue+powerpoint+deny+affirm
> powerpoint_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+powerpoint+deny+deny
> powerpoint_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+powerpoint+affirm
> powerpoint_issue_asked
* affirm
 - utter_generic_apology
 - utter_powerpoint_options
 > specific_powerpoint_issue

## issue+powerpoint+affirm+other
> specific_powerpoint_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+powerpoint+generalerrors
> specific_powerpoint_issue
* problem_powerpoint_generalerrors
 - utter_powerpoint_generalerrors
 > powerpoint_generalerrors_fixed_q

## issue+powerpoint+generalerrors+fixed
> powerpoint_generalerrors_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+powerpoint+generalerrors+notfixed
> powerpoint_generalerrors_fixed_q
* deny
 - utter_ticket_reply
 > powerpoint_generalerrors_not_fixed

## issue+powerpoint+generalerrors+notfixed+affirmanalyst
> powerpoint_generalerrors_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+powerpoint+generalerrors+notfixed+denyanalyst
> powerpoint_generalerrors_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+excel
> issue_asked
* problem_excel
 - utter_excel_question 
 > excel_issue_asked

## issue+excel+deny
> excel_issue_asked
* deny
 - utter_further_help
 > excel_issue_ticket

## issue+excel+deny+affirm
> excel_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+excel+deny+deny
> excel_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+excel+affirm
> excel_issue_asked
* affirm
 - utter_generic_apology
 - utter_excel_options
 > specific_excel_issue

## issue+excel+affirm+other
> specific_excel_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket





## issue+excel+generalissues
> specific_excel_issue
* problem_excel_generalissues
 - utter_excel_generalissues
 > excel_generalissues_fixed_q

## issue+excel+generalissues+fixed
> excel_generalissues_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+excel+generalissues+notfixed
> excel_generalissues_fixed_q
* deny
 - utter_ticket_reply
 > excel_generalissues_not_fixed

## issue+excel+generalissues+notfixed+affirmanalyst
> excel_generalissues_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+excel+generalissues+notfixed+denyanalyst
> excel_generalissues_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+aacrobat
> issue_asked
* problem_aacrobat
 - utter_aacrobat_question 
 > aacrobat_issue_asked

## issue+aacrobat+deny
> aacrobat_issue_asked
* deny
 - utter_further_help
 > aacrobat_issue_ticket

## issue+aacrobat+deny+affirm
> aacrobat_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+aacrobat+deny+deny
> aacrobat_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+aacrobat+affirm
> aacrobat_issue_asked
* affirm
 - utter_generic_apology
 - utter_aacrobat_options
 > specific_aacrobat_issue

## issue+aacrobat+affirm+other
> specific_aacrobat_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket





## issue+aacrobat+generalissues
> specific_aacrobat_issue
* problem_aacrobat_generalissues
 - utter_aacrobat_generalissues
 > aacrobat_generalissues_fixed_q

## issue+aacrobat+generalissues+fixed
> aacrobat_generalissues_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+aacrobat+generalissues+notfixed
> aacrobat_generalissues_fixed_q
* deny
 - utter_ticket_reply
 > aacrobat_generalissues_not_fixed

## issue+aacrobat+generalissues+notfixed+affirmanalyst
> aacrobat_generalissues_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+aacrobat+generalissues+notfixed+denyanalyst
> aacrobat_generalissues_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+skype
> issue_asked
* problem_skype
 - utter_skype_question 
 > skype_issue_asked

## issue+skype+deny
> skype_issue_asked
* deny
 - utter_further_help
 > skype_issue_ticket

## issue+skype+deny+affirm
> skype_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+skype+deny+deny
> skype_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+skype+affirm
> skype_issue_asked
* affirm
 - utter_generic_apology
 - utter_skype_options
 > specific_skype_issue

## issue+skype+affirm+other
> specific_skype_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+skype+login
> specific_skype_issue
* problem_skype_login
 - utter_skype_login
 > skype_login_fixed_q

## issue+skype+login+fixed
> skype_login_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+skype+login+notfixed
> skype_login_fixed_q
* deny
 - utter_ticket_reply
 > skype_login_not_fixed

## issue+skype+login+notfixed+affirmanalyst
> skype_login_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+skype+login+notfixed+denyanalyst
> skype_login_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+skype+msgs
> specific_skype_issue
* problem_skype_msgs
 - utter_skype_msgs
 > skype_msgs_fixed_q

## issue+skype+msgs+fixed
> skype_msgs_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+skype+msgs+notfixed
> skype_msgs_fixed_q
* deny
 - utter_ticket_reply
 > skype_msgs_not_fixed

## issue+skype+msgs+notfixed+affirmanalyst
> skype_msgs_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+skype+msgs+notfixed+denyanalyst
> skype_msgs_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+sas
> issue_asked
* problem_sas
 - utter_sas_question 
 > sas_issue_asked

## issue+sas+deny
> sas_issue_asked
* deny
 - utter_further_help
 > sas_issue_ticket

## issue+sas+deny+affirm
> sas_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+sas+deny+deny
> sas_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+sas+affirm
> sas_issue_asked
* affirm
 - utter_generic_apology
 - utter_sas_options
 > specific_sas_issue

## issue+sas+affirm+other
> specific_sas_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+sas+general
> specific_sas_issue
* problem_sas_general
 - utter_sas_general
 > sas_general_fixed_q

## issue+sas+general+fixed
> sas_general_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+sas+general+notfixed
> sas_general_fixed_q
* deny
 - utter_ticket_reply
 > sas_general_not_fixed

## issue+sas+general+notfixed+affirmanalyst
> sas_general_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+sas+general+notfixed+denyanalyst
> sas_general_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+slack
> issue_asked
* problem_slack
 - utter_slack_question 
 > slack_issue_asked

## issue+slack+deny
> slack_issue_asked
* deny
 - utter_further_help
 > slack_issue_ticket

## issue+slack+deny+affirm
> slack_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+slack+deny+deny
> slack_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+slack+affirm
> slack_issue_asked
* affirm
 - utter_generic_apology
 - utter_slack_options
 > specific_slack_issue

## issue+slack+affirm+other
> specific_slack_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket





## issue+slack+general
> specific_slack_issue
* problem_slack_general
 - utter_slack_general
 > slack_general_fixed_q

## issue+slack+general+fixed
> slack_general_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+slack+general+notfixed
> slack_general_fixed_q
* deny
 - utter_ticket_reply
 > slack_general_not_fixed

## issue+slack+general+notfixed+affirmanalyst
> slack_general_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+slack+general+notfixed+denyanalyst
> slack_general_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+drives
> issue_asked
* problem_drives
 - utter_drives_question 
 > drives_issue_asked

## issue+drives+deny
> drives_issue_asked
* deny
 - utter_further_help
 > drives_issue_ticket

## issue+drives+deny+affirm
> drives_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+drives+deny+deny
> drives_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+drives+affirm
> drives_issue_asked
* affirm
 - utter_generic_apology
 - utter_drives_options
 > specific_drives_issue

## issue+drives+affirm+other
> specific_drives_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket





## issue+drives+connect
> specific_drives_issue
* problem_drives_connect
 - utter_drives_connect
 > drives_connect_fixed_q

## issue+drives+connect+fixed
> drives_connect_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+drives+connect+notfixed
> drives_connect_fixed_q
* deny
 - utter_ticket_reply
 > drives_connect_not_fixed

## issue+drives+connect+notfixed+affirmanalyst
> drives_connect_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+drives+connect+notfixed+denyanalyst
> drives_connect_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+drives+files
> specific_drives_issue
* problem_drives_files
 - utter_drives_files
 > drives_files_fixed_q

## issue+drives+files+fixed
> drives_files_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+drives+files+notfixed
> drives_files_fixed_q
* deny
 - utter_ticket_reply
 > drives_files_not_fixed

## issue+drives+files+notfixed+affirmanalyst
> drives_files_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+drives+files+notfixed+denyanalyst
> drives_files_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+jabber
> issue_asked
* problem_jabber
 - utter_jabber_question 
 > jabber_issue_asked

## issue+jabber+deny
> jabber_issue_asked
* deny
 - utter_further_help
 > jabber_issue_ticket

## issue+jabber+deny+affirm
> jabber_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+jabber+deny+deny
> jabber_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+jabber+affirm
> jabber_issue_asked
* affirm
 - utter_generic_apology
 - utter_jabber_options
 > specific_jabber_issue

## issue+jabber+affirm+other
> specific_jabber_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+jabber+error
> specific_jabber_issue
* problem_jabber_error
 - utter_jabber_error
 > jabber_error_fixed_q

## issue+jabber+error+fixed
> jabber_error_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+jabber+error+notfixed
> jabber_error_fixed_q
* deny
 - utter_ticket_reply
 > jabber_error_not_fixed

## issue+jabber+error+notfixed+affirmanalyst
> jabber_error_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+jabber+error+notfixed+denyanalyst
> jabber_error_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+browser
> issue_asked
* problem_browser
 - utter_browser_question 
 > browser_issue_asked

## issue+browser+deny
> browser_issue_asked
* deny
 - utter_further_help
 > browser_issue_ticket

## issue+browser+deny+affirm
> browser_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+browser+deny+deny
> browser_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+browser+affirm
> browser_issue_asked
* affirm
 - utter_generic_apology
 - utter_browser_options
 > specific_browser_issue

## issue+browser+affirm+other
> specific_browser_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket





## issue+browser+general
> specific_browser_issue
* problem_browser_general
 - utter_browser_general
 > browser_general_fixed_q

## issue+browser+general+fixed
> browser_general_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+browser+general+notfixed
> browser_general_fixed_q
* deny
 - utter_ticket_reply
 > browser_general_not_fixed

## issue+browser+general+notfixed+affirmanalyst
> browser_general_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+browser+general+notfixed+denyanalyst
> browser_general_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+browser+edge
> specific_browser_issue
* problem_browser_edge
 - utter_browser_edge
 > browser_edge_fixed_q

## issue+browser+edge+fixed
> browser_edge_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+browser+edge+notfixed
> browser_edge_fixed_q
* deny
 - utter_ticket_reply
 > browser_edge_not_fixed

## issue+browser+edge+notfixed+affirmanalyst
> browser_edge_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+browser+edge+notfixed+denyanalyst
> browser_edge_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+browser+firefox
> specific_browser_issue
* problem_browser_firefox
 - utter_browser_firefox
 > browser_firefox_fixed_q

## issue+browser+firefox+fixed
> browser_firefox_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+browser+firefox+notfixed
> browser_firefox_fixed_q
* deny
 - utter_ticket_reply
 > browser_firefox_not_fixed

## issue+browser+firefox+notfixed+affirmanalyst
> browser_firefox_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+browser+firefox+notfixed+denyanalyst
> browser_firefox_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+browser+ie
> specific_browser_issue
* problem_browser_ie
 - utter_browser_ie
 > browser_ie_fixed_q

## issue+browser+ie+fixed
> browser_ie_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+browser+ie+notfixed
> browser_ie_fixed_q
* deny
 - utter_ticket_reply
 > browser_ie_not_fixed

## issue+browser+ie+notfixed+affirmanalyst
> browser_ie_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+browser+ie+notfixed+denyanalyst
> browser_ie_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+browser+chrome
> specific_browser_issue
* problem_browser_chrome
 - utter_browser_chrome
 > browser_chrome_fixed_q

## issue+browser+chrome+fixed
> browser_chrome_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+browser+chrome+notfixed
> browser_chrome_fixed_q
* deny
 - utter_ticket_reply
 > browser_chrome_not_fixed

## issue+browser+chrome+notfixed+affirmanalyst
> browser_chrome_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+browser+chrome+notfixed+denyanalyst
> browser_chrome_not_fixed
* deny
 - utter_goodbye
 - action_restart