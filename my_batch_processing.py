import os

# 需要处理的音频文件的路径(文件按0开始递增1的数字命名）
src_path = "src_voice"
# 输出文件路径
out_path = "out_voice"
# 文件类型
extended_name = "mp3"


# 调用系统命令
def sys_cmd(file_path):
    cmd = "python inference.py -i " + file_path + " -p -g 0 -o " + out_path
    ret1 = os.system(cmd)
    return ret1



try:
    for i in range(len(os.listdir(src_path))):
        file_name = str(i) + '.' + extended_name
        print('file_name=' + file_name)
        ret = sys_cmd(src_path + "/" + file_name)
        print('ret=' + str(ret))
except:
    print('run error')
