---
id: UNC@20.15.2@MMLCommand@DSP PAEPORT
type: MMLCommand
name: DSP PAEPORT（显示PAE端口统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPORT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEPORT（显示PAE端口统计信息）

## 功能

该命令用于显示PAE端口统计信息。

通过统计PAE外联端口、Fabric端口、Loop端口、Control端口收发报文的数目以及收发速率，可了解PAE模块与其他模块通信是否正常，并进行故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| PORTTYPE | 端口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PAE端口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- extern：外联口。<br>- fabric：内联口。<br>- loop：Loop口。<br>- base：base口。<br>- acc：加速端口。<br>- control：控制端口。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPORT]] · PAE端口统计信息（PAEPORT）

## 使用实例

显示所有微服务类型为aa的微服务实例aa的PAE外联口统计信息：

```
DSP PAEPORT:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
--------
微服务类型  微服务实例号 端口类型    端口名称    接收报文数目    发送报文数目    接收报文速率（pps）    发送报文速率（pps）    重发次数    丢包统计 
		
aa          aa           外联口      eth5        1316            1311            5                      6                      0           0        
aa          aa           外联口      eth6        0               0               0                      0                      0           0        
aa          aa           外联口      eth7        0               0               0                      0                      0           0        
aa          aa           外联口      eth8        0               0               0                      0                      0           0        
aa          aa           外联口      eth9        0               0               0                      0                      0           0 
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE端口统计信息（DSP-PAEPORT）_92520027.md`
