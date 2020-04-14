# n = 10
concurrency_list=(1 5 10)
for i in "${concurrency_list[@]}"; do
    ab -n 10 -c "$i" http://127.0.0.1:10001/ > benchmark_result/test_result_10_"$i".txt
done

# n = 50
concurrency_list=(1 10 30 50)
for i in "${concurrency_list[@]}"; do
    ab -n 50 -c "$i" http://127.0.0.1:10001/ > benchmark_result/test_result_50_"$i".txt
done

# n = 100
concurrency_list=(1 10 50 100)
for i in "${concurrency_list[@]}"; do
    ab -n 100 -c "$i" http://127.0.0.1:10001/ > benchmark_result/test_result_100_"$i".txt
done