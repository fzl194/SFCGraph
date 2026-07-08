---
id: UNC@20.15.2@MMLCommand@DSP BFDSTATS
type: MMLCommand
name: DSP BFDSTATS（查询BFD的会话统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BFDSTATS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD会话统计
status: active
---

# DSP BFDSTATS（查询BFD的会话统计信息）

## 功能

该命令用于显示BFD会话的统计信息。可以按照本地描述符或者目的地址过滤。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALDISCR | 本地标识符 | 可选必选说明：可选参数<br>参数含义：该参数表示会话本地描述符。用于唯一标识本端会话。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～49152。<br>默认值：无 |
| DESTADDR | 目的IP地址 | 可选必选说明：可选参数<br>参数含义：该参数表示会话检测链路的目的地址。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～128。IPv4或者IPv6地址。<br>默认值：无 |

## 操作的配置对象

- [BFD的会话统计信息（BFDSTATS）](configobject/UNC/20.15.2/BFDSTATS.md)

## 使用实例

显示本地描述符为222会话的统计信息：

```
DSP BFDSTATS:LOCALDISCR=222;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                  本地标识符  =  222
              收到的报文数目  =  0
              发送的报文数目  =  0
              收到的坏包数目  =  0
              发送的坏包数目  =  0
                会话Down次数  =  0
                会话创建时间  =  2015-09-17 20:19:24
            上一次Down的时间  =  NULL
              上一次Up的时间  =  NULL
              会话创建的时长  =  000D:04H:27M:05S
      距离上次会话Down的时长  =  NULL
            上一次Up持续时长  =  NULL
                    会话名称  =  Huawei123
(结果个数 = 1)
---  END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BFD的会话统计信息（DSP-BFDSTATS）_00440309.md`
