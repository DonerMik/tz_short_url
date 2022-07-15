#1 TASK
SELECT win.client_number, win.win as 'Побед', lose.lose as 'Поражений'

FROM
	(SELECT client_number, COUNT(outcome) AS win
    FROM bid, event_value
	WHERE bid.play_id=event_value.play_id AND bid.coefficient=event_value.value AND outcome='win'
    GROUP BY client_number) AS win,

	(SELECT client_number, COUNT(outcome) AS lose
    FROM bid, event_value
	WHERE bid.play_id=event_value.play_id AND bid.coefficient=event_value.value AND outcome='lose'
    GROUP BY client_number) AS lose
WHERE win.client_number = lose.client_number
GROUP BY win.client_number


#2 TASK
SELECT IF(event_entity.home_team < event_entity.away_team,
    CONCAT(event_entity.home_team,':',event_entity.away_team),
    CONCAT(event_entity.away_team,':',event_entity.home_team)) AS game,
    COUNT(play_id) AS games_count
FROM event_entity
GROUP BY game
ORDER BY games_count