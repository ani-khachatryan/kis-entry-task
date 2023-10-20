import os
import hashlib
import difflib
from statistics import mean


def calculate_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def longest_common_subsequence_length(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def compare_large_binary_files(file1_path, file2_path):
    buffer_size = 8192
    ratios = []
    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        while True:
            data1 = file1.read(buffer_size)
            data2 = file2.read(buffer_size)

            if not data1 and not data2:
                break  # fully processed

            if data1 != data2:
                # If the chunks are not identical, calculate the similarity ratio
                lcs_length = longest_common_subsequence_length(data1, data2)
                similarity = lcs_length / max(len(data1), len(data2))
                ratios.append(similarity)
            else:
                ratios.append(1.0)
    return ratios

def similarity_ratio(s1, s2):
    chunk_ratios = compare_large_binary_files(s1, s2)
    similarity = mean(chunk_ratios)
    return similarity


def compare_directories(dir1, dir2, similarity_threshold):
    files1 = [os.path.join(dir1, f) for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
    files2 = [os.path.join(dir2, f) for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

    identical_files = []
    similar_files = []
    files_only_in_dir1 = []
    files_only_in_dir2 = []

    for file1 in files1:
        hash1 = calculate_hash(file1)
        for file2 in files2:
            hash2 = calculate_hash(file2)

            if hash1 == hash2:
                identical_files.append((file1, file2))
            else:
                # Calculate similarity
                similarity = similarity_ratio(file1, file2)
                if similarity * 100 >= similarity_threshold:
                    similar_files.append((file1, file2, similarity))

    for file1 in files1:
        if not any(file1 == pair[0] for pair in identical_files):
            files_only_in_dir1.append(file1)

    for file2 in files2:
        if not any(file2 == pair[1] for pair in identical_files):
            files_only_in_dir2.append(file2)

    return identical_files, similar_files, files_only_in_dir1, files_only_in_dir2

if __name__ == "__main__":
    dir1 = input("Enter the first directory path: ")
    dir2 = input("Enter the second directory path: ")
    similarity_threshold = float(input("Enter the similarity threshold % (0 to 100): "))

    dir1 = os.path.abspath(dir1)
    dir2 = os.path.abspath(dir2)

    identical, similar, only_in_dir1, only_in_dir2 = compare_directories(dir1, dir2, similarity_threshold)

    print("Идентичные файлы:")
    for pair in identical:
        print(f"{pair[0]} - {pair[1]}")

    print("\nПохожие файлы:")
    for pair in similar:
        print(f"{pair[0]} - {pair[1]} - {pair[2] * 100}% сходства")

    print("\nФайлы только в директории 1:")
    for file in only_in_dir1:
        print(file)

    print("\nФайлы только в директории 2:")
    for file in only_in_dir2:
        print(file)
