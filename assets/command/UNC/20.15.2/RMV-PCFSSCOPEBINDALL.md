---
id: UNC@20.15.2@MMLCommand@RMV PCFSSCOPEBINDALL
type: MMLCommand
name: RMV PCFSSCOPEBINDALL（删除所有的PCF业务服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCFSSCOPEBINDALL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区绑定
status: active
---

# RMV PCFSSCOPEBINDALL（删除所有的PCF业务服务区的绑定关系）

## 功能

![](删除所有的PCF业务服务区的绑定关系（RMV PCFSSCOPEBINDALL）_38569369.assets/notice_3.0-zh-cn_2.png)

删除PCF业务服务区的绑定关系不当，可能导致基于业务服务区选择的PCF不符合预期，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的PCF业务服务区的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [所有的PCF业务服务区的绑定关系（PCFSSCOPEBINDALL）](configobject/UNC/20.15.2/PCFSSCOPEBINDALL.md)

## 使用实例

删除PCFSSCOPEBIND的所有配置。

```
RMV PCFSSCOPEBINDALL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除所有的PCF业务服务区的绑定关系（RMV-PCFSSCOPEBINDALL）_38569369.md`
