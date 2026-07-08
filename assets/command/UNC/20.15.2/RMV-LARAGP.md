---
id: UNC@20.15.2@MMLCommand@RMV LARAGP
type: MMLCommand
name: RMV LARAGP（删除位置区群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LARAGP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 位置区管理
- 位置区群组管理
status: active
---

# RMV LARAGP（删除位置区群组）

## 功能

**适用网元：SGSN**

此命令用于删除位置区或路由区类型的区域群记录。

## 注意事项

- 此命令执行后立即生效。
- 删除跟踪区群组时必须首先删除该跟踪区群组下的所有成员，可执行[**RMV LARAGPMEM**](../位置区群组成员管理/删除位置区群组成员(RMV LARAGPMEM)_26145484.md)命令进行删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LARAGPID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区和路由区的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无 |

## 操作的配置对象

- [位置区群组（LARAGP）](configobject/UNC/20.15.2/LARAGP.md)

## 使用实例

删除一个位置区群组，区域群标识为1:

RMV LARAGP: LARAGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除位置区群组(RMV-LARAGP)_72345079.md`
