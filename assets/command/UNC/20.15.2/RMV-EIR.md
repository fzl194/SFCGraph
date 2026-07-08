---
id: UNC@20.15.2@MMLCommand@RMV EIR
type: MMLCommand
name: RMV EIR（删除EIR配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EIR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- EIR管理
status: active
---

# RMV EIR（删除EIR配置）

## 功能

**适用网元：MME**

此命令用于删除EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

## 注意事项

- 此命令执行后立即生效。
- 删除后，将导致系统无法找到指定EIR。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [EIR配置（EIR）](configobject/UNC/20.15.2/EIR.md)

## 使用实例

将EIR记录删除：

RMV EIR:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除EIR配置(RMV-EIR)_26145452.md`
