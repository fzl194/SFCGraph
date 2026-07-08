---
id: UDG@20.15.2@MMLCommand@DSP MSSPORTPMDDRV
type: MMLCommand
name: DSP MSSPORTPMDDRV（显示端口PMD驱动信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSPORTPMDDRV
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSPORTPMDDRV（显示端口PMD驱动信息）

## 功能

该命令用于显示pmd驱动信息，在其他驱动环境下使用，结果不可控。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| PORTNAME | 端口名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSPORTINFO](显示端口信息（DSP MSSPORTINFO）_92520022.md)**<br>查看端口名。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSPORTPMDDRV]] · 端口PMD驱动信息（MSSPORTPMDDRV）

## 使用实例

显示类型为aa的微服务bb的端口pmd驱动的信息：

```
DSP MSSPORTPMDDRV:CELLTYPE="aa", CELLINSTANCE="bb",PORTNAME="eth1";
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
                                     设备端口号  =  6
                                 驱动端口索引号  =  5
                                       链路状态  =  down
                               链路速率（Mbps）  =  10000
                                    MTU（byte）  =  1500
                                DAL接收报文个数  =  0
                                DAL发送报文个数  =  0
                          PMD适配层内部错误次数  =  0
                    PMD适配层接收端端口down次数  =  411183462
                    PMD适配层接收报文为空的次数  =  0
                    PMD适配层发送端口down的次数  =  0
                      PMD适配层发送报文错误次数  =  0
                              PMD接收报文的个数  =  0
                              PMD发送报文的个数  =  0
                                PMD接收的字节数  =  0
                                PMD发送的字节数  =  0
                          PMD接收报文错误的个数  =  0
                          PMD发送报文错误的个数  =  0
                                PMD发送队列长度  =  4096
                        端口接收报文速率（pps）  =  4
                        端口发送报文速率（pps）  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSPORTPMDDRV.md`
