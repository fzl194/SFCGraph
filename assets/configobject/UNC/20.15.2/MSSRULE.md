---
id: UNC@20.15.2@ConfigObject@MSSRULE
type: ConfigObject
name: MSSRULE（匹配规则）
nf: UNC
version: 20.15.2
object_name: MSSRULE
object_kind: global_setting
status: active
---

# MSSRULE（匹配规则）

## 说明

该命令用于设置匹配规则。

用户只有设置规则后，才能绑定该规则对消息或者报文进行匹配，匹配规则是从消息、报文的偏移类型对应的位置加上偏移大小开始，比较“规则内容&规则掩码”和“报文内容&规则掩码”是否一致。

当前通信模块可通过DSP MSSCOMMSTAT命令查询匹配统计个数。

输入的规则内容和掩码应为字符串形式，只能是英文字母、数字的组合，英文字母只能是a～f，且不区分大小写，且字符个数只能是偶数个，输入不符合规范的字符串有错误信息“规则无效。”。

当规则ID被使用时无法删除或者修改，有错误信息“规则正在使用。”。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-MSSRULE]] · DSP MSSRULE
- [[command/UNC/20.15.2/SET-MSSRULE]] · SET MSSRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/MSSRULE.md`
- 原始手册：`evidence/UNC/20.15.2/MSSRULE.md`
