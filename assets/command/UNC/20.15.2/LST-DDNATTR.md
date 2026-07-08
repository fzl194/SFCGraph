---
id: UNC@20.15.2@MMLCommand@LST DDNATTR
type: MMLCommand
name: LST DDNATTR（查询DDN消息参数以及Delay信元处理开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNATTR
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- DDN消息携带的属性
status: active
---

# LST DDNATTR（查询DDN消息参数以及Delay信元处理开关）

## 功能

**适用NF：SGW-C**

该命令用来查询Downlink Data Notification消息中是否支持携带EBI和ARP信元，以及控制SGW-C是否基于DownlinkData Notification Ack消息和Modify Bearer Request消息中的Delay信元进行处理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDNATTR]] · DDN消息参数以及Delay信元处理开关（DDNATTR）

## 使用实例

查询Downlink Data Notification消息中的是否支持携带EBI和ARP信元，以及SGW-C是否支持对DownlinkData Notification Ack消息和Modify Bearer Request消息中Delay信元进行处理：

```
%%LST DDNATTR:;%%
RETCODE = 0  操作成功

结果如下
--------
          携带EBI  =  不使能
            EBI值  =  触发DDN消息的承载
          携带ARP  =  不使能
            ARP值  =  触发DDN消息的承载
Delay信元处理开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DDNATTR.md`
