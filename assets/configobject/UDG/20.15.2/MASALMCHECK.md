---
id: UDG@20.15.2@ConfigObject@MASALMCHECK
type: ConfigObject
name: MASALMCHECK（5G告警核查）
nf: UDG
version: 20.15.2
object_name: MASALMCHECK
object_kind: action
status: active
---

# MASALMCHECK（5G告警核查）

## 说明

当发现系统存在未恢复的故障告警时，可通过该命令启动告警核查功能，若系统识别出该故障已经恢复，则自动恢复该故障告警。

当前支持核查的告警包括ALM-100155 HTTP链路故障告警。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统核查速率为每秒20条告警。
> - 系统每半个小时会对半小时以前产生的故障告警进行自动核查。
> - 命令返回成功表示系统开始核查所有支持核查的故障告警，核查操作将在后台完成。
> - 当系统正在核查告警时，该命令返回失败。

## 操作本对象的命令

- [DSP MASALMCHECK](command/UDG/20.15.2/DSP-MASALMCHECK.md)
- [STR MASALMCHECK](command/UDG/20.15.2/STR-MASALMCHECK.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/启动5G告警核查（STR-MASALMCHECK）_80751076.md`
- 原始手册：`evidence/UDG/20.15.2/显示5G告警核查状态（DSP-MASALMCHECK）_32103567.md`
