def run_timimg():
    total_time =0
    number_of_run = 0
    # := 指派運算式 空字串會返回False
    while run_time := input('輸入跑十公里時間： (直接按Enter結束)'):
        try:
            run_time_value =float(run_time)
            total_time+= run_time_value
            number_of_run += 1
        except Exception as e:
            print('產生錯誤',e)
        if number_of_run > 0:
            avgage_time = (total_time/number_of_run)
        else:
            avgage_time = 0.0
        print(f'跑{number_of_run}次的平均時間為{avgage_time}分鐘')
run_timimg()


