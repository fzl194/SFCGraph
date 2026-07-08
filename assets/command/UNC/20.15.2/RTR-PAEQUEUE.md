---
id: UNC@20.15.2@MMLCommand@RTR PAEQUEUE
type: MMLCommand
name: RTR PAEQUEUE（清除PAE队列统计信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: PAEQUEUE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# RTR PAEQUEUE（清除PAE队列统计信息）

## 功能

该命令用于清除PAE队列统计信息。

通过清除PAE队列收发报文数目、收发速率，从而方便故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无 |
| QUEUEID | 队列ID | 可选必选说明：可选参数<br>参数含义：该参数用于清除指定队列ID的统计信息；若不输入，则表示清除所有队列的统计信息。该参数可以使用<br>**[DSP PAEQUEUEINFO](显示PAE队列信息（DSP PAEQUEUEINFO）_92520012.md)**<br>获取。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围是0x80000000～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [PAE队列统计信息（PAEQUEUE）](configobject/UNC/20.15.2/PAEQUEUE.md)

## 使用实例

清除PAE队列统计信息：

```
RTR PAEQUEUE:CELLTYPE="aa", CELLINSTANCE="bb";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除PAE队列统计信息（RTR-PAEQUEUE）_92520044.md`
