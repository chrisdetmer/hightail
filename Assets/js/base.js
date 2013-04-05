$(document).ready(function(){
	
	var boardWidth = function(){
		var boards = $('div.board');
		// compare widths of sibling boards and expand container accordingly
	}
	
	var reorderBoards = function(){
		var boards = $('div.board');
		for(i=0,len=boards.length;i<len;i++){
			console.log($(boards[i]).attr('id') + ' = ' + (i+1));
			$(boards[i]).attr('data-sort-order', i+1);
		}
	}
	
	var editStory = function(story, action){
		var updateColor = function(story, list){
			var story_class = $.trim(story.attr('class').replace('story', '').replace('open', '')), color = list.find('option:selected').val();
			story.removeClass(story_class).addClass(color);
		}
		var updateList = function(list, value){
			list.find('option[value=' + value + ']').attr('selected', 'selected');
		}
		var member_list = $('#id_member_list').clone().removeAttr('id'), color_list = $('#id_color_list').clone().removeAttr('id');
		if(action == 'open'){
			var color = story.attr('data-color'), member = story.find('span.member').attr('data-user-id');
			if(story.find('select').length){
				color_list = story.find('select.color-list');
				member_list = story.find('select.member-list');
			}
			updateList(color_list, color);
			updateList(member_list, member);
			story.find('.story-info').prepend(color_list).prepend(member_list);
			story.find(':input').show();
			story.find('.cancel').click(function(){
				editStory(story, 'close');
			});
			story.find('.submit').click(function(){
				var new_member = member_list.find('option:selected');
				story.find('span.description').text(story.find('textarea.content').val());
				story.find('span.points').text(story.find('input.points').val());
				story.find('span.member').attr('data-userid', new_member.val()).text(new_member.text());
				updateColor(story, color_list);
				editStory(story, 'close');
			});
			story.addClass('open');
		}else{
			story.removeClass('open');
			story.find(':input').hide();
			story.find('.submit').unbind('click');
		}
	}
	
	$('li.story a.edit-story').click(function(){
		var story = $(this).parent(), action = 'open';
		if(story.hasClass('open')){
			action = 'close';
		}
		editStory(story, action);
		return false;
	});
	$('li.story textarea.content, li.story input.point-count, li.story strong.member').dblclick(function(){
		var story = $(this).parent();
		if(!story.hasClass('open')){
			editStory(story, 'open');
		}
	});
	
	//$('li.story').draggable();
	$('div.sprint').sortable({ items: "> div.board", opacity: 0.5, handle: 'h2', stop: function(){ reorderBoards() } });
	$('ul.story-list').sortable({ items: "> li.story", opacity: 0.5, containtment: 'div.sprint', connectWith: 'ul.story-list' });
});