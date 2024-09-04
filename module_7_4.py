team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2


if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'


result_team1_num = "В команде Мастера кода участников: %d !" % team1_num
result_total_num = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)


result_score_team2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result_time_team2 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)


result_scores = f"Команды решили {score_1} и {score_2} задач."
result_challenge_result = f"Результат битвы: {challenge_result}"
result_tasks_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."


print(result_team1_num)
print(result_total_num)
print(result_score_team2)
print(result_time_team2)
print(result_scores)
print(result_challenge_result)
print(result_tasks_info)
