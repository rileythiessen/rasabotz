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

## issue+entrust+affirm+other
> specific_entrust_issue
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

## issue+entrust
> issue_asked
* problem_entrust
 - utter_entrust_question 
 > entrust_issue_asked

## issue+entrust+deny
> entrust_issue_asked
* deny
 - utter_further_help
 > entrust_issue_ticket

## issue+entrust+deny+affirm
> entrust_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+entrust+deny+deny
> entrust_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+entrust+affirm
> entrust_issue_asked
* affirm
 - utter_generic_apology
 - utter_entrust_options
 > specific_entrust_issue

## issue+entrust+certificates
> specific_entrust_issue
* problem_entrust_certificates
 - utter_entrust_certificates
 > entrust_certificates_fixed_q

## issue+entrust+certificates+fixed
> entrust_certificates_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+entrust+certificates+notfixed
> entrust_certificates_fixed_q
* deny
 - utter_ticket_reply
 > entrust_certificates_not_fixed

## issue+entrust+certificates+notfixed+affirmanalyst
> entrust_certificates_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+entrust+certificates+notfixed+denyanalyst
> entrust_certificates_not_fixed
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

## issue+office
> issue_asked
* problem_office
 - utter_office_question 
 > office_issue_asked

## issue+office+deny
> office_issue_asked
* deny
 - utter_further_help
 > office_issue_ticket

## issue+office+deny+affirm
> office_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+office+deny+deny
> office_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+office+affirm
> office_issue_asked
* affirm
 - utter_generic_apology
 - utter_office_options
 > specific_office_issue

## issue+office+affirm+other
> specific_office_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+office+word
> specific_office_issue
* problem_office_word
 - utter_office_word
 > office_word_fixed_q

## issue+office+word+fixed
> office_word_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+office+word+notfixed
> office_word_fixed_q
* deny
 - utter_ticket_reply
 > office_word_not_fixed

## issue+office+word+notfixed+affirmanalyst
> office_word_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+office+word+notfixed+denyanalyst
> office_word_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+office+powerpoint
> specific_office_issue
* problem_office_powerpoint
 - utter_office_powerpoint
 > office_powerpoint_fixed_q

## issue+office+powerpoint+fixed
> office_powerpoint_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+office+powerpoint+notfixed
> office_powerpoint_fixed_q
* deny
 - utter_ticket_reply
 > office_powerpoint_not_fixed

## issue+office+powerpoint+notfixed+affirmanalyst
> office_powerpoint_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+office+powerpoint+notfixed+denyanalyst
> office_powerpoint_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+office+excel
> specific_office_issue
* problem_office_excel
 - utter_office_excel
 > office_excel_fixed_q

## issue+office+excel+fixed
> office_excel_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+office+excel+notfixed
> office_excel_fixed_q
* deny
 - utter_ticket_reply
 > office_excel_not_fixed

## issue+office+excel+notfixed+affirmanalyst
> office_excel_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+office+excel+notfixed+denyanalyst
> office_excel_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+adobe
> issue_asked
* problem_adobe
 - utter_adobe_question 
 > adobe_issue_asked

## issue+adobe+deny
> adobe_issue_asked
* deny
 - utter_further_help
 > adobe_issue_ticket

## issue+adobe+deny+affirm
> adobe_issue_ticket
* affirm
 - utter_ticket_created_reply
 - action_restart

## issue+adobe+deny+deny
> adobe_issue_ticket
* deny
 - utter_call_it
 - action_restart

## issue+adobe+affirm
> adobe_issue_asked
* affirm
 - utter_generic_apology
 - utter_adobe_options
 > specific_adobe_issue

## issue+adobe+affirm+other
> specific_adobe_issue
* issue_not_listed
 - utter_issue_not_found
 > other_ticket

## issue+adobe+acrobat
> specific_adobe_issue
* problem_adobe_acrobat
 - utter_adobe_acrobat
 > adobe_acrobat_fixed_q

## issue+adobe+acrobat+fixed
> adobe_acrobat_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+adobe+acrobat+notfixed
> adobe_acrobat_fixed_q
* deny
 - utter_ticket_reply
 > adobe_acrobat_not_fixed

## issue+adobe+acrobat+notfixed+affirmanalyst
> adobe_acrobat_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+adobe+acrobat+notfixed+denyanalyst
> adobe_acrobat_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+adobe+creative
> specific_adobe_issue
* problem_adobe_creative
 - utter_adobe_creative
 > adobe_creative_fixed_q

## issue+adobe+creative+fixed
> adobe_creative_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+adobe+creative+notfixed
> adobe_creative_fixed_q
* deny
 - utter_ticket_reply
 > adobe_creative_not_fixed

## issue+adobe+creative+notfixed+affirmanalyst
> adobe_creative_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+adobe+creative+notfixed+denyanalyst
> adobe_creative_not_fixed
* deny
 - utter_goodbye
 - action_restart

## issue+adobe+illustrator
> specific_adobe_issue
* problem_adobe_illustrator
 - utter_adobe_illustrator
 > adobe_illustrator_fixed_q

## issue+adobe+illustrator+fixed
> adobe_illustrator_fixed_q
* affirm
 - utter_goodbye
 - action_restart

## issue+adobe+illustrator+notfixed
> adobe_illustrator_fixed_q
* deny
 - utter_ticket_reply
 > adobe_illustrator_not_fixed

## issue+adobe+illustrator+notfixed+affirmanalyst
> adobe_illustrator_not_fixed
* affirm
 - utter_analyst_reply
 - action_restart

## issue+adobe+illustrator+notfixed+denyanalyst
> adobe_illustrator_not_fixed
* deny
 - utter_goodbye
 - action_restart

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