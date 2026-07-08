---
id: UNC@20.15.2@MMLCommand@RMV UPFPFCPPARA
type: MMLCommand
name: RMV UPFPFCPPARA（删除UPF粒度PFCP参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPFPFCPPARA
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
- 接口管理
- PFCP接口管理
- PFCP路径管理
- UPF粒度PFCP路径参数管理
status: active
---

# RMV UPFPFCPPARA（删除UPF粒度PFCP参数）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于删除指定实例名称的UPF粒度PFCP参数。

## 注意事项

- 该命令执行后立即生效。

- 删除UPF粒度PFCP参数后，会使用PFCPPARA命令中配置的全局PFCP参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFPFCPPARA]] · UPF粒度PFCP参数（UPFPFCPPARA）

## 使用实例

删除实例名称为“upf1”的UPF粒度PFCP参数：

```
RMV UPFPFCPPARA: UPFINSTANCEID="upf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPFPFCPPARA.md`
