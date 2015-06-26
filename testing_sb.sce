default_font_size = 48;
#log_key_presses = true;

response_matching = simple_matching;
active_buttons = 2;
button_codes = 16, 32;
begin;

TEMPLATE "words_arrays.tem";
TEMPLATE "semantic_block.tem";

/*
TEMPLATE "syntax_block.tem" {
	caption_1 caption_2 caption_3 caption_4;
	
	"хватает" "трогает" "гладит" "пишет";
}; */

begin_pcl;

sub semantic_block(string caption_1, string caption_2, string caption_3, string caption_4)
begin

#current_semantic_block.caption_1_pic.
caption_1_text.set_caption(caption_1);	
#caption_1_text.load();
caption_1_text.redraw();
show_caption_1.set_event_code(caption_1);

#current_semantic_block.caption_2_pic.
caption_2_text.set_caption(caption_2);	
caption_2_text.redraw();
show_caption_2.set_event_code(caption_2);

#current_semantic_block.caption_3_pic.
caption_3_text.set_caption(caption_3);	
caption_3_text.redraw();
show_caption_3.set_event_code(caption_3);

#current_semantic_block.caption_4_pic.
caption_4_text.set_caption(caption_4);	
caption_4_text.redraw();
show_caption_4.set_event_code(caption_4);

current_semantic_block.present();
	
end;

#semantic_block("хватает", "трогает", "гладит", "пишет", "Серия с нажатиями кнопок руками");
intro_text.set_caption("Серия с нажатиями кнопок руками\nПростая\nНажимать во время предъявления");
intro_text.redraw();

show_intro_title_trial.present();

i = 0;
loop until i >= word_array.count()
begin
	semantic_block(word_array[i], word_array[i+1], word_array[i+2], word_array[i+3]);
	i = i + 4;
end;
