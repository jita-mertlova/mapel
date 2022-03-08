#!/usr/bin/env python


from mapel.main.objects.Family import Family


class ElectionFamily(Family):
    """ Family of elections: a set of elections from the same election model_id """

    def __init__(self,
                 model_id: str = None,
                 family_id='none',
                 params: dict = None,
                 size: int = 1,
                 label: str = "none",
                 color: str = "black",
                 alpha: float = 1.,
                 ms: int = 20,
                 show=True,
                 marker='o',
                 starting_from: int = 0,
                 path: dict = None,
                 single: bool = False,

                 num_candidates=None,
                 num_voters=None,
                 single_election: bool = False,
                 election_ids=None,
                 ballot: str = 'ordinal'):

        super().__init__(model_id=model_id,
                         family_id=family_id,
                         params=params,
                         size=size,
                         label=label,
                         color=color,
                         alpha=alpha,
                         ms=ms,
                         show=show,
                         marker=marker,
                         starting_from=starting_from,
                         path=path,
                         single=single,
                         instance_ids=election_ids)

        self.num_candidates = num_candidates
        self.num_voters = num_voters
        self.single_election = single_election
        self.ballot = ballot

    def __getattr__(self, attr):
        if attr == 'election_ids':
            return self.instance_ids
        else:
            return self.__dict__[attr]

    def __setattr__(self, name, value):
        if name == "election_ids":
            return setattr(self, 'instance_ids', value)
        else:
            self.__dict__[name] = value


# # # # # # # # # # # # # # # #
# LAST CLEANUP ON: 12.10.2021 #
# # # # # # # # # # # # # # # #
