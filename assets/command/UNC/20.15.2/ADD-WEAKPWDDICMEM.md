---
id: UNC@20.15.2@MMLCommand@ADD WEAKPWDDICMEM
type: MMLCommand
name: ADD WEAKPWDDICMEM（增加弱口令字典成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: WEAKPWDDICMEM
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 2000
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 弱口令管理
status: active
---

# ADD WEAKPWDDICMEM（增加弱口令字典成员）

## 功能

**适用NF：NCG**

该命令用于增加弱口令字典成员。

用于配置口令场景，系统口令复杂度校验后，需要再进一步验证所设置口令是否在弱口令字典中。

## 注意事项

- 该命令最大记录数为2000。
- 该命令执行后即时生效。
- 如新增加弱口令字典成员在已配置命令的口令中存在，已配置命令不会受影响。
- 新增弱口令对pull的ftp/sftp的分发任务有影响。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WEAKPWD | 弱口令 | 可选必选说明：必选参数<br>参数含义：用于增加弱口令字典中的成员。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 密码不支持中文字符。<br>- 密码区分大小写。<br>- 最大能添加2000条弱口令字典数据。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@WEAKPWDDICMEM]] · 弱口令字典成员（WEAKPWDDICMEM）

## 使用实例

增加“弱口令”“qazQAZ123!@#”到弱口令字典。示例如下：

```
ADD WEAKPWDDICMEM: WEAKPWD="qazQAZ123!@#";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-WEAKPWDDICMEM.md`
