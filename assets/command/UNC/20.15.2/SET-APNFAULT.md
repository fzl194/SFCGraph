---
id: UNC@20.15.2@MMLCommand@SET APNFAULT
type: MMLCommand
name: SET APNFAULT（设置APN粒度的故障处理开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNFAULT
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- APN故障处理
status: active
---

# SET APNFAULT（设置APN粒度的故障处理开关）

## 功能

![](设置APN粒度的故障处理开关（SET APNFAULT）_98988893.assets/notice_3.0-zh-cn_2.png)

UPFAULTMODE设置为DETECTION时，SMF会隔离故障的N6链路，UPF存在过载风险。RESTOREFAULT设置为ENABLE时，SMF收到UPF上报的N6故障消息后，如果链路故障的UPF是主锚点UPF，则会去活使用故障N6链路的用户。

**适用NF：PGW-C、GGSN、SMF**

该命令用于控制APN粒度的故障处理开关。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录。
- 记录中参数的初始设置值如下：UPFAULTMODE: NOHANDLING。
- 每个UPF最多可支持1000个APN检测到故障后隔离。
- 禁止将停机APN的UPFAULTMODE设置为DETECTION。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无。<br>配置原则：无 |
| UPFAULTMODE | UP链路故障处理模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UP链路故障处理模式。<br>数据来源：全网规划<br>取值范围：<br>- NOHANDLING（无处理）<br>- “DETECTION（检测到故障后隔离）”：检测到故障后隔离APN网络和UPF之间的链路。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNFAULT查询当前参数配置值。<br>配置原则：无 |
| RESTOREFAULT | SMF是否支持用户面链路故障恢复 | 可选必选说明：该参数在"UPFAULTMODE"配置为"DETECTION"时为条件可选参数。<br>参数含义：该参数用于用户面链路（N6）故障时，控制SMF是否进行恢复流程。当配置为Enable时，如果链路故障的UPF为主锚点，则删除会话；如果链路故障的UPF为辅锚点，则根据参数AUXMIGFUNC判断是否需要进行辅锚点迁移流程；当配置为Disable时，则不进行恢复流程。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNFAULT查询当前参数配置值。<br>配置原则：无 |
| AUXMIGFUNC | 辅锚点UPF迁移功能开关 | 可选必选说明：该参数在"RESTOREFAULT"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制当辅锚点发生链路（N6）故障时，是否进行辅锚点会话迁移流程。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNFAULT查询当前参数配置值。<br>配置原则：<br>当该参数置为ENABLE时，如果ADD UPNODE中的APSAMIGFUNC开关置为DISABLE，则会删除辅锚点上的会话，如果APSAMIGFUNC开关置为ENABLE，则会尝试迁移会话到其他可用辅锚点；当该参数置为DISABLE时，则不处理已创建的N6故障的辅锚点会话。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNFAULT]] · APN粒度的故障处理开关（APNFAULT）

## 使用实例

APN配置UP链路故障处理模式为检测到故障后隔离。

```
SET APNFAULT: APN="test",UPFAULTMODE=DETECTION;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN粒度的故障处理开关（SET-APNFAULT）_98988893.md`
