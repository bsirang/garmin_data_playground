import fitdecode
import pandas as pd
import sys


class GarminDecode:
    def __init__(self, filename):
        frame_dict = dict()
        decoded = dict()
        with fitdecode.FitReader(filename) as fit:
            for frame in fit:
                # The yielded frame object is of one of the following types:
                # * fitdecode.FitHeader
                # * fitdecode.FitDefinitionMessage
                # * fitdecode.FitDataMessage
                # * fitdecode.FitCRC
                if isinstance(frame, fitdecode.FitDefinitionMessage):
                    #print(frame.field_defs)
                    definition_key = self.definition_to_key(frame)
                    if definition_key not in decoded:
                        decoded[definition_key] = dict()
                        print("New definition found {}".format(definition_key))

                if isinstance(frame, fitdecode.FitDataMessage):
                    # Here, frame is a FitDataMessage object.
                    # A FitDataMessage object contains decoded values that
                    # are directly usable in your script logic.
                    # if frame.name == "monitoring":
                    if True:
                        if frame.name not in frame_dict:
                            frame_dict[frame.name] = dict()
    #                     frame_dict[frame.name].append(frame)
                        for field in frame.fields:
                            if field.name not in frame_dict[frame.name]:
                                frame_dict[frame.name][field.name] = list()
                            frame_dict[frame.name][field.name].append(field.value)
                            # print("{} {}".format(field.name, field.value))
        for frame_name, frame in frame_dict.items():
            for field_name, values in frame.items():
                pass
                # print("{}.{} {}".format(frame_name, field_name, len(values)))
        self.frame_dict = frame_dict

    @staticmethod
    def definition_to_key(definition):
        key = definition.name + ","
        for field in definition.field_defs:
            key += field.name + ","
        return key[:-1]


if __name__ == "__main__":
    filename = sys.argv[1]
    decoded = GarminDecode(filename)
