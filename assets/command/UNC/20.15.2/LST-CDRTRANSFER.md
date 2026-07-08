---
id: UNC@20.15.2@MMLCommand@LST CDRTRANSFER
type: MMLCommand
name: LST CDRTRANSFER（查询话单发送控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRTRANSFER
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- 话单发送参数
status: active
---

# LST CDRTRANSFER（查询话单发送控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询话单发送控制参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRTRANSFER]] · 话单发送控制参数（CDRTRANSFER）

## 使用实例

查询话单发送控制参数：

```
LST CDRTRANSFER:;
```

```

RETCODE = 0  操作成功

话单发送控制参数
----------------
                GTP'消息最大可携带的话单字节数  =  2000
 Echo and Data Record Transfer Request重传次数  =  3
Data Record Transfer Request重传时间间隔（秒）  =  3
              Node Alive消息重传时间间隔（秒）  =  10
                                    CG选择模式  =  基于消息的负载均衡
                          GTP'报文CheckSum开关  =  允许
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRTRANSFER.md`
