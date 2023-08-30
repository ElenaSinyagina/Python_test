from hw import ssh_find_text_in_command, ssh_download_files, ssh_find_text_Negative
import crc
import yaml

with open('config.yaml') as file:
    data = yaml.safe_load(file)

class Test_Positive:
    def test_1_find_text_in_command(self, make_folders_local, make_folders, make_files, print_time):
        assert ssh_find_text_in_command(host=str(data["host"]),
                                        user=str(data["user"]),
                                        password=str(data["password"]),
                                        command=f'cd {data["folderin"]}; 7z a -t{data["typearch"]} '
                                                f'{data["folderout"]}/{data["filename"]}',
                                        text='Everything is Ok'), 'Test1 FAIL'

    def test_2_find_text_in_command(self, print_time):
        assert ssh_find_text_in_command(host=str(data["host"]),
                                        user=str(data["user"]),
                                        password=str(data["password"]),
                                        command=f'ls {data["folderout"]}',
                                        text=f'{data["filename"]}'), 'Test2 FAIL'

    def test_3_find_text_in_command(self, clear_folders_local, clear_folders, print_time):
        ssh_download_files(host=str(data["host"]),
                           user=str(data["user"]),
                           password=str(data["password"]),
                           remote_path=f'{data["folderoutget"]}/{data["filename"]}.{data["typearch"]}',
                           local_path=f'{data["folderoutlocal"]}/{data["filename"]}.{data["typearch"]}')

        assert ssh_find_text_in_command(host=str(data["host"]),
                                        user=str(data["user"]),
                                        password=str(data["password"]),
                                        command=f'crc32 {data["folderout"]}/*',
                                        text=crc.crc32(f'{data["folderoutlocal"]}/{data["filename"]}.{data["typearch"]}').lower()), \
            'Test3 FAIL'

class Test_Negative:
    def test_1Neg_find_text_in_command(self, make_folders_local, make_folders, make_files, print_time):
        assert ssh_find_text_Negative(host=str(data["host"]),
                                      user=str(data["user"]),
                                      password=str(data["password"]),
                                      command=f'cd {data["folderin"]}; 7z a -t{data["typearch"]} {data["folderout"]}/{data["filename"]}',
                                      text='FAILED'), 'Test1 FAIL'

    def test_2Neg_find_text_in_command(self, print_time):
        assert ssh_find_text_Negative(host=str(data["host"]),
                                      user=str(data["user"]),
                                      password=str(data["password"]),
                                      command=f'ls {data["folderoutlocal"]}',
                                      text=f'{data["filename"]}'), 'Test2 FAIL'

    def test_3Neg_find_text_in_command(self, clear_folders_local, clear_folders, print_time):
        ssh_download_files(host=str(data["host"]),
                           user=str(data["user"]),
                           password=str(data["password"]),
                           remote_path=f'{data["folderoutget"]}/{data["filename"]}.{data["typearch"]}',
                           local_path=f'{data["folderoutlocal"]}/{data["filename"]}.{data["typearch"]}')

        assert ssh_find_text_Negative(host=str(data["host"]),
                                      user=str(data["user"]),
                                      password=str(data["password"]),
                                      command=f'crc322 {data["folderout"]}/*',
                                      text=crc.crc32(f'{data["folderoutlocal"]}/{data["filename"]}.{data["typearch"]}').lower()), \
            'Test3 FAIL'