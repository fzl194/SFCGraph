---
id: UNC@20.15.2@MMLCommand@RMV WEAKPWDDICMEM
type: MMLCommand
name: RMV WEAKPWDDICMEM（删除弱口令字典成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: WEAKPWDDICMEM
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 弱口令管理
status: active
---

# RMV WEAKPWDDICMEM（删除弱口令字典成员）

## 功能

**适用NF：NCG**

该命令用于删除弱口令字典中的成员。

## 注意事项

- 该命令执行后即时生效。

- 执行该命令删除的配置项是已经泄露的口令时，请谨慎操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WEAKPWD | 弱口令 | 可选必选说明：必选参数<br>参数含义：用于删除弱口令字典中的成员。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WEAKPWDDICMEM]] · 弱口令字典成员（WEAKPWDDICMEM）

## 使用实例

在弱口令字典中删除“弱口令”“qazQAZ123!@#”。示例如下：

```
RMV WEAKPWDDICMEM: WEAKPWD="qazQAZ123!@#";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除弱口令字典成员（RMV-WEAKPWDDICMEM）_89255128.md`
