---
id: UNC@20.15.2@MMLCommand@LST VLRRESETTIMER
type: MMLCommand
name: LST VLRRESETTIMER（查询VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRRESETTIMER
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 用户上下文管理
status: active
---

# LST VLRRESETTIMER（查询VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置）

## 功能

**适用NF：SMSF**

该命令用于查询VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置（VLRRESETTIMER）](configobject/UNC/20.15.2/VLRRESETTIMER.md)

## 使用实例

运营商希望查询VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置，执行如下命令：

```
LST VLRRESETTIMER:;
%%LST VLRRESETTIMER:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
重发开关 =  打开
重发次数 =  2
VLR等待接收MME SGsAP-RESET-ACK响应(秒) = 5

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置（LST-VLRRESETTIMER）_11591169.md`
