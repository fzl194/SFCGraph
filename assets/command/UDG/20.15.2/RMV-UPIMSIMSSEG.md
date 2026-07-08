---
id: UDG@20.15.2@MMLCommand@RMV UPIMSIMSSEG
type: MMLCommand
name: RMV UPIMSIMSSEG（删除IMSI和MSISDN号段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPIMSIMSSEG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- IMSI MSISDN号段
status: active
---

# RMV UPIMSIMSSEG（删除IMSI和MSISDN号段）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除IMSI/MSISDN号码段。

## 注意事项

- 该命令执行后立即生效。
- 如果号段被绑定，则不能删除IMSI和MSISDN号段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPIMSIMSSEG]] · IMSI和MSISDN号段（UPIMSIMSSEG）

## 使用实例

删除IMSI和MSISDN号段,SEGMENTNAME为huawei，命令为：

```
RMV UPIMSIMSSEG:SEGMENTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IMSI和MSISDN号段（RMV-UPIMSIMSSEG）_85042561.md`
