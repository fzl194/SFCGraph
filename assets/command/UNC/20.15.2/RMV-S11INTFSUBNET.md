---
id: UNC@20.15.2@MMLCommand@RMV S11INTFSUBNET
type: MMLCommand
name: RMV S11INTFSUBNET（删除S11接口子网配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S11INTFSUBNET
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GWIP地址配置
status: active
---

# RMV S11INTFSUBNET（删除S11接口子网配置）

## 功能

**适用网元：MME**

此命令用于删除S11或S11-U接口的子网配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令在版本升级过程中禁止执行。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKIDX | 链路关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本对端IP地址关联索引。<br>取值范围：0~65534<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S11INTFSUBNET]] · S11接口子网配置（S11INTFSUBNET）

## 使用实例

1. 删除关联索引为0的S11接口子网配置，可以用如下命令：
  ```
  RMV S11INTFSUBNET: LNKIDX=0;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S11接口子网配置-(RMV-S11INTFSUBNET)_19337703.md`
