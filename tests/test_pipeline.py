"""Pipeline 执行、去重、改名测试。"""
from modules.common.enums import RejectReason
from modules.common.node import Node
from modules.pipeline import RuleStats, deduplicate, fingerprint, rename_unique, run_pipeline
from modules.rules.base import Rule, RuleResult

UUID_A = "123e4567-e89b-12d3-a456-426614174000"
UUID_B = "223e4567-e89b-12d3-a456-426614174001"


def node(protocol="vless", server="1.2.3.4", port=443, name="n", raw=None):
    return Node(protocol=protocol, server=server, port=port, name=name, raw=raw or {})


class AlwaysReject(Rule):
    rule_id = "always_reject"
    category = None

    def evaluate(self, node):
        return RuleResult.reject(RejectReason.JUNK_KEYWORD)


class RejectWhen(Rule):
    rule_id = "reject_when"

    def __init__(self, cond):
        self._cond = cond

    def evaluate(self, node):
        return RuleResult.reject(RejectReason.INVALID_TARGET) if self._cond(node) else RuleResult.pass_()


class AlwaysPass(Rule):
    rule_id = "always_pass"
    category = None

    def evaluate(self, node):
        return RuleResult.pass_()


class ExplodingRule(Rule):
    rule_id = "exploding"

    def evaluate(self, node):
        raise RuntimeError("boom")


def test_run_pipeline_all_pass():
    nodes = [node(name="a"), node(name="b")]
    passed, stats = run_pipeline(nodes, [AlwaysPass()])
    assert len(passed) == 2
    assert stats.total_rejected() == 0


def test_run_pipeline_short_circuit():
    """第二个节点被拒后，后续规则不应再执行。"""
    calls = []

    class Counting(Rule):
        rule_id = "counting"

        def evaluate(self, n):
            calls.append(n.name)
            return RuleResult.pass_()

    nodes = [node(name="keep"), node(name="drop")]
    passed, stats = run_pipeline(nodes, [AlwaysPass(), RejectWhen(lambda n: n.name == "drop"), Counting()])
    assert [n.name for n in passed] == ["keep"]
    # drop 节点短路，Counting 只执行一次（对 keep）
    assert calls == ["keep"]


def test_run_pipeline_rule_error_fail_closed():
    nodes = [node(name="x")]
    passed, stats = run_pipeline(nodes, [ExplodingRule()])
    assert passed == []
    assert stats.errors["exploding"] == 1
    assert stats.counts["exploding"][RejectReason.RULE_ERROR.value] == 1


def test_fingerprint_per_protocol():
    a = node(protocol="vmess", raw={"uuid": UUID_A})
    b = node(protocol="vmess", raw={"uuid": UUID_B})
    # 同 server:port 不同 uuid = 不同指纹
    assert fingerprint(a) != fingerprint(b)
    # 不同协议不同指纹
    c = node(protocol="vless", raw={"uuid": UUID_A})
    assert fingerprint(a) != fingerprint(c)
    # 相同 → 相同
    assert fingerprint(a) == fingerprint(a)


def test_dedup():
    nodes = [
        node(protocol="vmess", server="1.2.3.4", port=443, raw={"uuid": UUID_A}, name="a"),
        node(protocol="vmess", server="1.2.3.4", port=443, raw={"uuid": UUID_A}, name="a2"),
        node(protocol="vmess", server="1.2.3.4", port=443, raw={"uuid": UUID_B}, name="b"),
    ]
    result = deduplicate(nodes)
    assert len(result) == 2
    assert result[0].name == "a"


def test_rename_unique():
    nodes = [node(name="香港 01"), node(name="香港 01"), node(name="香港 01"), node(name="其他")]
    rename_unique(nodes)
    names = [n.name for n in nodes]
    assert len(set(names)) == 4
    assert "香港 01" in names
    assert "香港 01-2" in names
    assert "香港 01-3" in names


def test_rule_stats():
    stats = RuleStats()
    stats.record("r1", RejectReason.JUNK_KEYWORD)
    stats.record("r1", RejectReason.JUNK_KEYWORD)
    stats.record("r1", RejectReason.INVALID_TARGET)
    stats.record_error("r2")
    assert stats.total_rejected() == 3
    assert stats.errors["r2"] == 1
