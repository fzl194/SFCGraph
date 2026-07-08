---
id: UDG@20.15.2@MMLCommand@LST GLOBALL2TP
type: MMLCommand
name: LST GLOBALL2TP（查询L2TP配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLOBALL2TP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP缺省配置
status: active
---

# LST GLOBALL2TP（查询L2TP配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看L2TP的缺省配置信息。运营商如果需要查看L2TP隧道本端名称、HELLO报文发送开关、HELLO报文重发间隔和报文重发次数，可以使用该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLOBALL2TP]] · L2TP配置（GLOBALL2TP）

## 使用实例

假设运营商想要查看当前配置的L2TP隧道的缺省属性，可以使用该命令：

```
LST GLOBALL2TP:;
```

```

RETCODE = 0  操作成功。

全局L2TP配置信息
----------------
                 是否支持Magic-Number协商  =  不使能
                             初始隧道个数  =  1
                      HELLO报文间隔（秒）  =  60
                             发送窗口上限  =  64
                             报文重发次数  =  3
                            HELLO报文开关  =  使能
                           隧道本端的名称  =  huawei
               每条隧道承载的会话个数上限  =  32767
对LNS服务器发送探测消息的时间间隔（分钟）  =  5
               L2TP无效隧道存活时长(小时)  =  24
        对LNS服务器发送探测消息的功能开关  =  使能

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLOBALL2TP.md`
