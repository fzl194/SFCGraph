---
id: UNC@20.15.2@MMLCommand@RMV UPFADDRATTR
type: MMLCommand
name: RMV UPFADDRATTR（删除UPF地址属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPFADDRATTR
command_category: 配置类
applicable_nf:
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

# RMV UPFADDRATTR（删除UPF地址属性）

## 功能

![](删除UPF地址属性（RMV UPFADDRATTR）_99049128.assets/notice_3.0-zh-cn_2.png)

删除该配置可能会导致UPG热备特性和双UPG故障bypass功能失效。

**适用NF：SMF**

该命令用于删除UPF地址属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“NFINSTANCEID”参数取值相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFADDRATTR]] · UPF地址属性（UPFADDRATTR）

## 使用实例

以下命令用于删除实例名称为upf1的UPF地址属性。

```
RMV UPFADDRATTR: NFINSTANCEID="upf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPFADDRATTR.md`
