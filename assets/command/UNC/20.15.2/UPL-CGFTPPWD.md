---
id: UNC@20.15.2@MMLCommand@UPL CGFTPPWD
type: MMLCommand
name: UPL CGFTPPWD（更新CG FTP密码）
nf: UNC
version: 20.15.2
verb: UPL
object_keyword: CGFTPPWD
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- CG FTP密码
status: active
---

# UPL CGFTPPWD（更新CG FTP密码）

## 功能

**适用NF：NCG**

该命令用于更新FTP PULL分发任务的密码为不可逆加密方式存储。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INPUT | 输入 | 可选必选说明：必选参数<br>参数含义：该参数用于指定输入参数<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGFTPPWD]] · 更新CG FTP密码（CGFTPPWD）

## 使用实例

执行UPL CGFTPPWD更新FTP PULL分发任务的密码为不可逆加密方式存储：

```
UPL CGFTPPWD: INPUT="ncg";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPL-CGFTPPWD.md`
