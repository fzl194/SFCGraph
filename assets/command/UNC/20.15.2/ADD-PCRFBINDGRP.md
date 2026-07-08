---
id: UNC@20.15.2@MMLCommand@ADD PCRFBINDGRP
type: MMLCommand
name: ADD PCRFBINDGRP（增加PCRF与PCRF Group的关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCRFBINDGRP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 3200
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF绑定
status: active
---

# ADD PCRFBINDGRP（增加PCRF与PCRF Group的关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于添加指定的PCRF到PCRF分组中。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3200。
- 单个PCRF分组内最多可以有32个PCRF。
- 如果一个PCRF Group的工作模式为主备模式，且PCRF Group中绑定多个备PCRF，在不执行绑定关系删除的操作时，先绑定的备PCRF优先级高。
- 使用EXP MML命令导出的配置文件中，备PCRF绑定的配置顺序会按PCRF名称的字典序排序，再进行配置导入时，备PCRF的选择顺序可能会改变，主PCRF不会改变，可能影响failover场景下PCRF切换的顺序。
- 如果需要明确备PCRF的使用顺序，且确保重启后或配置导出时顺序不变，建议规划备PCRF名称按备PCRF使用优先级的顺序进行排序。
- 如果从多个备PCRF中删除某个备PCRF的绑定关系，再添加新的备PCRF，则新加入的备PCRF的优先级未知，因此如果需要保证备PCRF的优先级，建议将备PCRF全部删除后重新添加。
- 当PCRF Group的工作模式由主备切换回负荷分担模式时，已配置的PCRF权重将重新生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF分组的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRFGROUP命令配置生成。 |
| PCRFHOSTNAME | PCRF主机名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRF命令配置生成。 |
| WEIGHT | PCRF权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF的权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：<br>- 当PCRFGROUP工作模式为MASTER_SLAVE时，该参数的配置不生效，默认设置成无效值255。<br>- 在负荷分担模式下，若PCRF组只绑定一个PCRF，不配置此参数时值默认为100，若PCRF组绑定多个PCRF，则未配置此参数的多个PCRF均分剩余未配置的权重（PCRF组内所有PCRF的权重和为100，均分权重可能由于无法整除导致存在不超过1的误差），权重高的PCRF，被选中和使用的概率较高。<br>- 同一个PCRF组中PCRF权重值之和不能超过100。<br>- PCRF权重值可以为0。当所属PCRF组的工作模式为负荷分担模式时，如果PCRF权重值之和等于100，不会选择该PCRF。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCRFBINDGRP]] · PCRF与PCRF Group的关联关系（PCRFBINDGRP）

## 使用实例

增加Pcrf与PCRF Group的关联关系，PCRF组名为“abc”，PCRF名为“aaa”，PCRF权重为默认值：

```
ADD PCRFBINDGRP:PCRFGRPNAME="abc",PCRFHOSTNAME="aaa", WEIGHT=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCRFBINDGRP.md`
