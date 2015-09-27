default_font_size = 48;

response_matching = simple_matching;
active_buttons = 5;
button_codes = 1, 2, 0, 11, 22;
begin;

TEMPLATE "words.tem";
TEMPLATE "semantic_block.tem";

trial {
    trial_duration = forever;
    trial_type = specific_response;
    terminator_button = 3;
    
    picture {
        text {
            caption = "Ready";
        };
        x = 0; y = 0;
    };
} start_trial;

begin_pcl;

sub semantic_block(string caption_1, string caption_2, string caption_3, string caption_4)
begin

caption_1_text.set_caption(caption_1);	
caption_1_text.redraw();
show_caption_1.set_event_code(caption_1);

caption_2_text.set_caption(caption_2);	
caption_2_text.redraw();
show_caption_2.set_event_code(caption_2);

caption_3_text.set_caption(caption_3);	
caption_3_text.redraw();
show_caption_3.set_event_code(caption_3);

caption_4_text.set_caption(caption_4);	
caption_4_text.redraw();
show_caption_4.set_event_code(caption_4);

sound_response_recording_event.set_base_filename("C:/Documents and Settings/Admin/Рабочий стол/Experiments/Nastia PhD/recorded_responces/"+
logfile.subject()+"/response");
start_trial.present();
current_semantic_block.present();
	
end;

intro_text.set_caption("Серия без нажатий");
intro_text.redraw();

show_intro_title_trial.present();

int i = 1;
loop until i >= word_array.count()
begin
	semantic_block(word_array[i].caption(), word_array[i+1].caption(), word_array[i+2].caption(), word_array[i+3].caption());
	i = i + 4;
end;
