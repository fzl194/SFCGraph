---
id: UDG@20.15.2@MMLCommand@DSP MSSQUEDETINFOM
type: MMLCommand
name: DSP MSSQUEDETINFOM（显示指定队列详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSQUEDETINFOM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSQUEDETINFOM（显示指定队列详细信息）

## 功能

该命令用于显示指定队列详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| QUEUEID | 队列编号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示队列编号。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSQUEINFOM](显示队列总体信息（DSP MSSQUEINFOM）_92520052.md)**<br>查看队列编号。 |

## 操作的配置对象

- [指定队列详细信息（MSSQUEDETINFOM）](configobject/UDG/20.15.2/MSSQUEDETINFOM.md)

## 使用实例

显示类型为aa的微服务bb内指定队列详细信息：

```
DSP MSSQUEDETINFOM: CELLTYPE="aa", CELLINSTANCE="bb",QUEUEID="0x80000006";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                                          队列编号  =  0x80000006 
                                          队列状态  =  normal
                                          队列算法  =  MPSC
                              队列是否长时间未读取  =  no
                                      队列过载阈值  =  80
                                  队列过载恢复阈值  =  50
                                      队列过载状态  =  normal
                                      读成功的个数  =  1042877
              读失败的次数，魔术字破坏导致的读失败  =  0
                                        读空的次数  =  71928
                                      写成功的个数  =  1042877
写失败的个数，魔术字破坏与队列满导致的失败次数之和  =  0
                                    写队列满的次数  =  0
                                  每秒队列读取个数  =  11
                                  每秒队列写入个数  =  11
                              队列生产者逻辑进程号  =  0
                              队列消费者逻辑进程号  =  0
                                  队列生产者进程名  =  APP0
                                  队列消费者进程名  =  APP0
                                    生产者回收次数  =  2
                                    消费者回收次数  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示指定队列详细信息（DSP-MSSQUEDETINFOM）_92520015.md`
