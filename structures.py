cell = [[True]]
dead_cell = [[False]]
glider = [[None, True, None],
          [None, None, True],
          [True, True, True]]
glider_gun = [
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, True, None, True, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None, None, None, None, None, None, True, True],
    [None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, True, None, None, None, None, True, True, None, None, None, None, None, None, None, None, None, None, None, None, True, True],
    [True, True, None, None, None, None, None, None, None, None, True, None, None, None, None, None, True, None, None, None, True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [True, True, None, None, None, None, None, None, None, None, True, None, None, None, True, None, True, True, None, None, None, None, True, None, True, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, True, None, None, None, None, None, True, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

tub_stretcher = [[None, None, None, None, None, None, None, True, True, True, None, None, None, None, None],
                 [None, None, None, None, None, None, None, True, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, True, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, True, True, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, True, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, True, True, None, None, None, True, None],
                 [True, True, True, None, None, None, None, None, True, True, None, None, True, None, True],
                 [True, None, None, None, None, None, None, True, None, True, None, None, None, True, None],
                 [None, True, None, None, None, None, True, True, None, None, None, None, None, None, None],
                 [None, None, None, True, True, True, True, None, True, None, None, None, None, None, None],
                 [None, None, None, None, True, True, None, None, None, None, None, None, None, None, None]]

weekender = [
    [None, None, True, None, None, None, None, None, None, None, None, None, None, None, None, True, None, None],
    [None, True, True, True, None, None, None, None, None, None, None, None, None, None, True, True, True, None],
    [True, True, True, True, True, None, None, None, None, None, None, None, None, True, True, True, True, True],
    [True, True, True, True, True, None, None, None, None, None, None, None, None, True, True, True, True, True],
    [None, True, None, None, None, None, None, None, True, True, None, None, None, None, None, None, True, None],
    [None, None, True, True, True, None, None, None, True, True, None, None, None, True, True, True, None, None],
    [None, None, None, None, None, True, None, True, None, None, True, None, True, None, None, None, None, None],
    [None, None, None, None, None, None, None, True, None, None, True, None, None, None, None, None, None, None],
    [None, None, None, None, None, True, None, None, None, None, None, None, True, None, None, None, None, None],
    [None, None, None, None, None, None, True, True, True, True, True, True, None, None, None, None, None, None],
    [None, None, None, None, None, None, True, None, None, None, None, True, None, None, None, None, None, None]]

schick_engine = [[True, True, True, True, None, None, None, None, None, None, None, None, None, None, None],
                 [True, None, None, None, True, None, None, None, None, None, None, None, None, None, None],
                 [True, None, None, None, None, None, None, None, True, None, None, None, None, None, None],
                 [None, True, None, None, True, None, None, True, True, True, True, True, True, True, None],
                 [None, None, None, None, None, None, True, True, None, True, True, True, None, None, True],
                 [None, True, None, None, True, None, None, True, True, True, True, True, True, True, None],
                 [True, None, None, None, None, None, None, None, True, None, None, None, None, None, None],
                 [True, None, None, None, True, None, None, None, None, None, None, None, None, None, None],
                 [True, True, True, True, None, None, None, None, None, None, None, None, None, None, None]]

pulsar = [[None, None, True, True, None, None, None, None, None, True, True, None, None],
          [None, None, None, True, True, None, None, None, True, True, None, None, None],
          [True, None, None, True, None, True, None, True, None, True, None, None, True],
          [True, True, True, None, True, True, None, True, True, None, True, True, True],
          [None, True, None, True, None, True, None, True, None, True, None, True, None],
          [None, None, True, True, True, None, None, None, True, True, True, None, None],
          [None, None, None, None, None, None, None, None, None, None, None, None, None],
          [None, None, True, True, True, None, None, None, True, True, True, None, None],
          [None, True, None, True, None, True, None, True, None, True, None, True, None],
          [True, True, True, None, True, True, None, True, True, None, True, True, True],
          [True, None, None, True, None, True, None, True, None, True, None, None, True],
          [None, None, None, True, True, None, None, None, True, True, None, None, None],
          [None, None, True, True, None, None, None, None, None, True, True, None, None]]

pinwheel = [[None, None, None, None, None, None, True, True, None, None, None, None],
            [None, None, None, None, None, None, True, True, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, True, True, True, True, None, None, None, None],
            [True, True, None, True, None, None, True, None, True, None, None, None],
            [True, True, None, True, True, None, None, None, True, None, None, None],
            [None, None, None, True, None, True, None, None, True, None, True, True],
            [None, None, None, True, None, None, None, None, True, None, True, True],
            [None, None, None, None, True, True, True, True, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, True, True, None, None, None, None, None, None],
            [None, None, None, None, True, True, None, None, None, None, None, None]]

octagon_II = [[None, True, None, None, True, None],
              [True, None, True, True, None, True],
              [None, True, None, None, True, None],
              [None, True, None, None, True, None],
              [True, None, True, True, None, True],
              [None, True, None, None, True, None]]

octagon_IV = [[None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, True, True, True, True, None, None, None, None, None, None],
             [None, None, None, None, None, True, None, None, None, None, True, None, None, None, None, None],
             [None, None, None, None, True, None, None, None, None, None, None, True, None, None, None, None],
             [None, None, None, True, None, None, None, None, None, None, None, None, True, None, None, None],
             [True, True, None, True, None, None, None, None, None, None, None, None, True, None, True, True],
             [True, True, None, True, None, None, None, None, None, None, None, None, True, None, True, True],
             [None, None, None, True, None, None, None, None, None, None, None, None, True, None, None, None],
             [None, None, None, None, True, None, None, None, None, None, None, True, None, None, None, None],
             [None, None, None, None, None, True, None, None, None, None, True, None, None, None, None, None],
             [None, None, None, None, None, None, True, True, True, True, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None]]

cross = [[None, None, True, True, True, True, None, None],
         [None, None, True, None, None, True, None, None],
         [True, True, True, None, None, True, True, True],
         [True, None, None, None, None, None, None, True],
         [True, None, None, None, None, None, None, True],
         [True, True, True, None, None, True, True, True],
         [None, None, True, None, None, True, None, None],
         [None, None, True, True, True, True, None, None]]


names = {
    'Cell': cell,
    'Dead Cell': dead_cell,
    'Glider': glider,
    'Pulsar': pulsar,
    'Pinwheel': pinwheel,
    'Cross': cross,
    'Octagon II': octagon_II,
    'Octagon IV': octagon_IV,
    'Glider Gun': glider_gun,
    'Tub Stretcher': tub_stretcher,
    'Weekender': weekender,
    'Schick Engine': schick_engine
}
