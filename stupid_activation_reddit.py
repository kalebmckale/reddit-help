import operator as op

func = op.itemgetter("func")
args = op.itemgetter("args")
kwargs = op.itemgetter("kwargs")
X = op.itemgetter("x")

forward_pass = [
    {
        "func": self.conv,
        "args": (X,),
        "kwargs": {}
    },
    {
        "func": F.relu,
        "args": (X,),
        "kwargs": {}
    },
    {
        "func": F.max_pool2d,
        "args": (X, (2, 2)),
        "kwargs": {"stride": 2}
    },
    {
        "func": torch.flatten,
        "args": (X, 1),
        "kwargs": {}
    },
    {
        "func": self.fc1,
        "args": (X,),
        "kwargs": {}
    },
    {
        "func": F.relu,
        "args": (X,),
        "kwargs": {}
    },
    {
        "func": self.fc2,
        "args": (X,),
        "kwargs": {}
    },
    {
        "func": F.relu,
        "args": (X,),
        "kwargs": {}
    },
]
