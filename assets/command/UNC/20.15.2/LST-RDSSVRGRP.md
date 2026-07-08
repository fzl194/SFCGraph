---
id: UNC@20.15.2@MMLCommand@LST RDSSVRGRP
type: MMLCommand
name: LST RDSSVRGRP（查询Radius服务器组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSSVRGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- Radius服务器组
status: active
---

# LST RDSSVRGRP（查询Radius服务器组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询RADIUS SERVER GROUP配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSSVRGRP]] · Radius服务器组（RDSSVRGRP）

## 使用实例

查询Radius服务器组：

```
LST RDSSVRGRP:RDSSVRGRPNAME="rsg";
```

```

RETCODE = 0  操作成功。

Radius Server Group
-------------------
                        Radius Server Group名称  =  rsg
                                           模式  =  主备模式
      Accounting Request ON应答之前是否激活用户  =  禁止
                             利用鉴权服务器计费  =  禁止
                                         DSCP值  =  255
                               支持可选计费消息  =  禁止
Accounting Request On/Off消息间的时间间隔（秒）  =  9
                  Accounting Request On重发次数  =  3
             Accounting Request On超时时间 (秒)  =  3
                 Accounting Request Off重发次数  =  3
             Accounting Request Off超时时间(秒)  =  3
              Radius Accounting Request重发次数  =  3
         Radius Accounting Request超时时间 (秒)  =  3
          Radius Authentication Request重发次数  =  3
     Radius Authentication Request超时时间 (秒)  =  3
                 Radius Accounting超时时长 (秒)  =  12
          Radius计费服务器Down状态保持时长 (秒)  =  180
                  Radius鉴权服务器超时时长 (秒)  =  12
          Radius鉴权服务器Down状态保持时长 (秒)  =  180
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSSVRGRP.md`
