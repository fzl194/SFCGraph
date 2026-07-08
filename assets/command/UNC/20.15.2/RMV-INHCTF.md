---
id: UNC@20.15.2@MMLCommand@RMV INHCTF
type: MMLCommand
name: RMV INHCTF（删除禁止访问NCG的CTF实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INHCTF
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 禁止访问NCG的CTF实例
status: active
---

# RMV INHCTF（删除禁止访问NCG的CTF实例）

## 功能

**适用NF：NCG**

该命令用于删除禁止访问NCG的CTF实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示指定禁止访问NCG的CTF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [禁止访问NCG的CTF实例（INHCTF）](configobject/UNC/20.15.2/INHCTF.md)

## 使用实例

删除NF实例标识为nfinstanceid001的CTF实例：

```
RMV INHCTF:NFINSTANCEID="nfinstanceid001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除禁止访问NCG的CTF实例（RMV-INHCTF）_45110931.md`
