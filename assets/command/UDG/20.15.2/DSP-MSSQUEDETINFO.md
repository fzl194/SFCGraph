---
id: UDG@20.15.2@MMLCommand@DSP MSSQUEDETINFO
type: MMLCommand
name: DSP MSSQUEDETINFO（查询指定队列详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSQUEDETINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- MSS资源管理统计查询
status: active
---

# DSP MSSQUEDETINFO（查询指定队列详细信息）

## 功能

该命令用于查询指定队列详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| QUEUEID | 队列编号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示队列编号。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSQUEDETINFO]] · 指定队列详细信息（MSSQUEDETINFO）

## 使用实例

查询指定队列详细信息：

```
DSP MSSQUEDETINFO: RUNAME="VNODE_VNRS_VNFC_IPU_0066",QUEUEID="0x80000006";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                          队列编号  =  0x80000006
                                          队列名字  =  dp_to_dp_pkt
                                          队列属性  =  pbuffer share
                              队列状态，是否被破坏  =  normal
                                          队列长度  =  2047
                                          队列深度  =  0
                                          队列算法  =  MPSC
                                          队列参数  =  0
                              队列是否长时间未读取  =  no
                                      队列过载阈值  =  0
                                  队列过载恢复阈值  =  0
                                      队列过载状态  =  normal
                                      读成功的个数  =  1041946
              读失败的次数，魔术字破坏导致的读失败  =  0
                                        读空的次数  =  71879
                                      写成功的个数  =  1041946
写失败的个数，魔术字破坏与队列满导致的失败次数之和  =  0
                                    写队列满的次数  =  0
                                  每秒队列读取个数  =  0
                                  每秒队列写入个数  =  0
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

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSQUEDETINFO.md`
