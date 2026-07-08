---
id: UNC@20.15.2@MMLCommand@SET ADDRPARA
type: MMLCommand
name: SET ADDRPARA（设置ADDR参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ADDRPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- ADDR地址分配参数配置
status: active
---

# SET ADDRPARA（设置ADDR参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置ADDR参数，包括核查速率、去活间隔等参数。

## 注意事项

- 该命令执行后立即生效。

- 同步数据时间间隔过小，或者核查速率过大，会导致性能下降，业务可能受到影响。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SYNCINTERVAL | MAXHOP | ADDRCHECKRATE | SUBSECCHECKRATE | LEASECHECKRATE | ADDRRECYCLERATE | IPCHECKSW | IPRCSCHECKSW |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 240 | 2 | 6 | 6 | 2 | 6 | TRUE | TRUE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SYNCINTERVAL | 同步地址使用情况数据时间间隔(秒) | 可选必选说明：可选参数<br>参数含义：该参数用来设置地址分配管理节点实例向地址子段管理节点实例同步地址使用数据时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1800。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：无 |
| MAXHOP | 转发地址申请最大次数(次) | 可选必选说明：可选参数<br>参数含义：该参数用来设置地址分配管理节点实例间地址申请最大转发次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：无 |
| ADDRCHECKRATE | 地址使用情况核查速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用来设置每个DS每秒核查地址使用情况的地址池个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="AddrCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| SUBSECCHECKRATE | 地址子段分配情况核查速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用来设置每个DS每秒核查地址子段分配情况的地址池个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="AddrCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| LEASECHECKRATE | 租约核查速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用来设置每个DS的租约核查速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="AddrCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| ADDRRECYCLERATE | 地址回收速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用来设置每个DS每秒回收地址的个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~63，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：<br>DS个数 × 地址回收速率= 整系统地址回收速率。建议整系统地址回收速率大小不大于SET DEACTIVERATE命令中RATE字段取值。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="AddrCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| IPCHECKSW | 地址使用情况核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用来控制是否开启会话管理节点向地址分配管理节点的地址核查功能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：无 |
| IPRCSCHECKSW | 地址子段分配情况核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用来控制是否开启地址分配管理节点向地址子段管理节点的地址子段核查功能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ADDRPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [ADDR参数（ADDRPARA）](configobject/UNC/20.15.2/ADDRPARA.md)

## 使用实例

以下命令用于设置ADDRPARA记录，将同步地址使用情况数据时间间隔设为300秒，转发地址申请最大次数设为2次，地址使用情况核查速率设为2个/秒，地址子段分配情况核查速率设为2个/秒，租约核查速率设为2个/秒：

```
SET ADDRPARA:SYNCINTERVAL=300, MAXHOP=2,ADDRCHECKRATE=2,SUBSECCHECKRATE=2,LEASECHECKRATE=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置ADDR参数（SET-ADDRPARA）_37417403.md`
