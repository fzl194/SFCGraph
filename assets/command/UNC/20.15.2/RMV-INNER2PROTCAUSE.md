---
id: UNC@20.15.2@MMLCommand@RMV INNER2PROTCAUSE
type: MMLCommand
name: RMV INNER2PROTCAUSE（删除内部原因值映射为协议原因值的配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INNER2PROTCAUSE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- 内部原因值映射
status: active
---

# RMV INNER2PROTCAUSE（删除内部原因值映射为协议原因值的配置）

## 功能

![](删除内部原因值映射为协议原因值的配置（RMV INNER2PROTCAUSE）_44106693.assets/notice_3.0-zh-cn_2.png)

删除后下发的原因值可能会对终端行为产生影响，对性能指标的统计值产生影响，在配置前请联系华为研发工程师评估影响。

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于删除内部原因值映射为协议原因值的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示记录的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内部原因值映射为协议原因值的配置（INNER2PROTCAUSE）](configobject/UNC/20.15.2/INNER2PROTCAUSE.md)

## 使用实例

删除索引号为1的配置。

```
RMV INNER2PROTCAUSE: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除内部原因值映射为协议原因值的配置（RMV-INNER2PROTCAUSE）_44106693.md`
