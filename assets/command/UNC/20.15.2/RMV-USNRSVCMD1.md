---
id: UNC@20.15.2@MMLCommand@RMV USNRSVCMD1
type: MMLCommand
name: RMV USNRSVCMD1（删除预埋命令1）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USNRSVCMD1
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 预埋命令
status: active
---

# RMV USNRSVCMD1（删除预埋命令1）

## 功能

**适用网元：MME**

该命令用于删除实现指定的功能所需要的命令名称以及对应的参数信息。

## 注意事项

无

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：功能名称表示，类似普通的MML命令名<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |
| FUNKEY | 功能KEY参数 | 可选必选说明：必选参数<br>参数含义：功能名称对应的KEY参数。<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USNRSVCMD1]] · 预埋命令1（USNRSVCMD1）

## 使用实例

想删除通过命令名称为MOD GLOBALVARIABLE来修改某个全局变量的值的功能，则可以执行以下命令：

RMV USNRSVCMD1: FUNNAME="MOD GLOBALVARIABLE", FUNKEY="TESTKEY";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USNRSVCMD1.md`
