from datetime import datetime, timedelta

from garbage_destroyer.app import clean


def test_should_clean_files_with_extension(os_mock, glob_mock, config_mock):
    config_mock.return_value = {'Scheduler': {'hour': '*', 'minute': '*', 'second': '*'},
                                'Cleaning': {'dir': '/Users/victorpereira/Downloads', 'time_diff_in_days': '1',
                                'file_extension': 'jpg'}}
    glob_mock.return_value = ['alou.jpg', 'tchau.jpg']
    os_mock.path.getatime.return_value = (datetime.now() - timedelta(days=5)).timestamp()
    os_mock.path.isfile.return_value = True
    os_mock.remove.return_value = True
    clean()

    os_mock.remove.assert_called()
    glob_mock.assert_called()
    os_mock.path.getatime.assert_called()
    os_mock.path.isfile.assert_called()