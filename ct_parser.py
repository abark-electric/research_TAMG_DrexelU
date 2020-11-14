import numpy as np
import iot_for_diagnostics_and_prognostics.iot_for_dp.constants as const


keys = const.CT_FILE_KEYS
vals = np.loadtxt(const.CT_FILE_NAME_DEV, skiprows=const.SKIP_ROW_NUM)

for each in vals:
    dict_all_features = dict(zip(keys, each))
    print(dict_all_features)
