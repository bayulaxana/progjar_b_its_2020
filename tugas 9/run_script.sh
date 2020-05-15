# async server
# n = 1000
# concurrency_list=(500)
# for i in "${concurrency_list[@]}"; do
#     ab -n 1000 -c "$i" http://127.0.0.1:45000/ > benchmark_async/test_result_"$i".txt
# done

# thread server
# n = 1000
concurrency_list=(15)
for i in "${concurrency_list[@]}"; do
    ab -n 1000 -c "$i" http://127.0.0.1:46000/ > benchmark_thread/test_result_"$i".txt
done